import logging
import importlib

from django.conf import settings
from django.views import View

from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


logger = logging.getLogger(__name__)


def create_response(code, message):
    return {
        'response': {
            'code': code,
            'message': message
        }
    }

def get_services(which_type):
    services = []
    configured_services = getattr(settings, 'BMS_SERVICES')
    if not configured_services:
        logger.warning('No service configured, check your settings!')
        return

    for service_id, service in configured_services.items():
        service_type = service.get('type')
        if not service_type:
            logger.warning('Service {} has no type specified'.format(
                service_id))
            continue
        clazz = service.get('class')
        if not clazz:
            logger.warning('Service {} has no class specified'.format(
                service_id))
            continue

        label = service.get('label', service_id)
        per_user = service.get('per_user', False)
        kwargs = service.get('kwargs', {})

        if service_type != which_type:
            continue

        try:
            module_name, clazz_name = clazz.rsplit('.', 1)
            module = importlib.import_module(module_name)
            Clazz = getattr(module, clazz_name)

            if service_type == 'collector':
                instance = Clazz(**kwargs)
                if not getattr(instance, 'collect', None):
                    logger.warning('Service {} of type collector has not a "collect" method'.format(service_id))
                    continue
                services.append({
                    'id': service_id,
                    'label': label,
                    'per_user': per_user,
                    'instance': instance
                })                

            elif service_type == 'webhook':
                if not issubclass(Clazz, View):
                    logger.warning('Service {} of type webook is not a subclass of  "django.views.View'.format(service_id))
                    continue
                services.append({
                    'id': service_id,
                    'label': label,
                    'clazz': Clazz
                })
            else:
                logger.warning('Service type {} is not supported'.format(service_type))
                continue


        except Exception as e:
            logger.warning('Cannot instantiate service {}: {}'.format(
                service_id, e
            ))
    return services


def notify(service_id, value, per_user, **kwargs):
    channel_layer = get_channel_layer()
    if not kwargs:
        async_to_sync(channel_layer.group_send)('__all__', {
            'type': 'bms.notify', 
            'message': {
                'service_id': service_id,
                'value': value
            }
        })
        return
    else:
        User = get_user_model()
        try:
            user = User.objects.get(**kwargs)
            async_to_sync(channel_layer.group_send)(user.username, {
                'type': 'bms.notify', 
                'message': {
                    'service_id': service_id,
                    'value': value
                }
            })
        except User.DoesNotExist:
            logger.warning('no user found %s', kwargs)

