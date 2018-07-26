from channels.auth import login as channels_login
from channels.db import database_sync_to_async 
from django.contrib.auth import get_user_model
from ..utils import create_response


async def login(consumer, data):
    user = await _authenticate(consumer.scope,
                               data.get('username'), 
                               data.get('password'))
    if user:
        await consumer.channel_layer.group_add('__all__', 
                                               consumer.channel_name)
        await consumer.channel_layer.group_add(user.username,
                                               consumer.channel_name)
        return create_response(0, 'Successfully logged in!')
    return create_response(100, 'Invalid username or password')
    


async def _authenticate(scope, username, password):
    user = await _get_user(username, password)
    if not user:
        return None
    await channels_login(scope, user)
    return user


@database_sync_to_async
def _get_user(username, password):
    User = get_user_model()
    user = None
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return
    if user.check_password(password):
        return user
    return None