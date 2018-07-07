FROM python:3.6.3

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y locales && dpkg-reconfigure locales
RUN echo "es_ES.UTF-8 UTF-8" >> /etc/locale.gen
RUN echo "ca_ES.UTF-8 UTF-8" >> /etc/locale.gen
RUN /usr/sbin/locale-gen
RUN apt-get install gettext -y

COPY ./requirements.txt requirements.txt
RUN pip install -U -r /requirements.txt

COPY ./compose/django/entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./compose/django/start-server.sh /start-server.sh
RUN sed -i 's/\r//' /start-server.sh
RUN chmod +x /start-server.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
