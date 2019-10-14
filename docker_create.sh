#!/bin/sh
DOCKER_ID=`docker run -it -d dns_resolver`
echo "DOCKER_ID = $DOCKER_ID"
echo -n $DOCKER_ID > DOCKER_ID

