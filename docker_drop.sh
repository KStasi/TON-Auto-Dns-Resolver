#!/bin/bash
read -p 'are you sure? (press any key to continue)'
docker stop `cat ./DOCKER_ID`
docker rm   `cat ./DOCKER_ID`
