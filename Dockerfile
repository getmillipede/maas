FROM python:2.7
MAINTAINER Pierre Wacrenier

ADD . /code
WORKDIR /code

RUN pip install -r requirements/prod.txt
RUN pip install uwsgi

CMD uwsgi --http :9090 --module maas --callable app
