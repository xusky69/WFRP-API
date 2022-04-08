# set base image (host OS)
FROM python:3.10 as base

# set working dir to root of the django project
WORKDIR /home/WFRP/

# install linux dependencies
RUN apt-get update && apt-get -y install sqlite3 libsqlite3-dev nginx

# copy the requirements file to the working directory
COPY ./django_project/requirements.txt .

# install python dependencies
RUN pip install -r requirements.txt
# RUN pip install gunicorn
# RUN pip install psycopg2
# RUN pip install psycopg2-binary

# copy the project to the working directory
ADD ./django_project/ .

# remove logs, dev db and old env vars
RUN rm -rf .env db.sqlite3 wfrp/migrations logs
RUN mkdir -p media assets static

# setup python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# setup gunicorn environment variables:
ENV WORKERS=8
ENV TIMEOUT=240

# port exposure
EXPOSE 8000

# setup django environment variables:
RUN cp docker_env_vars .env

RUN echo 'DJANGO_SECRET_KEY=django-insecure-uuhkys9k=@rrh7b!(&zee4jo*1mkxco64i*4-_!o12)0=xduwo' >> local_env_vars
# RUN echo 'urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)' >> WFRP_API/urls.py
# RUN echo 'SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO","https"); USE_X_FORWARDED_HOST = True; USE_X_FORWARDED_PORT = True' >> WFRP_API/settings.py
RUN echo 'CSRF_TRUSTED_ORIGINS = ["http://localhost:1337"]' >> WFRP_API/settings.py


RUN echo "yes" | python manage.py collectstatic
# command to run on container start when nothing else is run:
CMD gunicorn -b 0.0.0.0:8000 --timeout=$TIMEOUT --workers=$WORKERS --env DJANGO_SETTINGS_MODULE=WFRP_API.settings WFRP_API.wsgi
