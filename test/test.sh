#!/bin/sh

cd ..
docker-compose up -d
cd -
py.test -v
cd ..
docker-compose stop
