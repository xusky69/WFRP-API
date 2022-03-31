# test argument
ARG test=FALSE

# set base image (host OS)
FROM python:3.10 as base

# set working dir to root of the django project
WORKDIR /home/WFRP/

# install linux dependencies
RUN apt-get update && apt-get -y install sqlite3 libsqlite3-dev nginx

# copy the requirements file to the working directory
COPY ./requirements.txt .

# install python dependencies
RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install psycopg2
RUN pip install psycopg2-binary

# copy the project to the working directory
ADD ./django_project/ .

# remove logs, dev db and old env vars
RUN rm -rf .env db.sqlite3 migrations logs reports song_data
RUN mkdir media_root assets static

# setup gunicorn environment variables:
ENV WORKERS=8
ENV TIMEOUT=240

# port exposure
EXPOSE 8000

# setup django environment variables:
FROM base as branch-test-TRUE
RUN cp test_env_vars .env

FROM base as branch-test-FALSE
RUN cp prod_env_vars .env

FROM branch-test-${test} AS final
RUN echo "yes" | python manage.py collectstatic
# command to run on container start when nothing else is run:
CMD gunicorn -b 0.0.0.0:8000 --timeout=$TIMEOUT --workers=$WORKERS --env DJANGO_SETTINGS_MODULE=WFRP_API.settings WFRP_API.wsgi