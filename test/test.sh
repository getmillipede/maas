#!/bin/sh

BASEDIR=$(dirname $0)
PROJECT_DIR=${BASEDIR}/..

cd ${PROJECT_DIR}
docker-compose up -d
py.test -v
docker-compose stop
