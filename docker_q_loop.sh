#!/bin/sh
./docker_drop.sh && \
  ./docker_build.sh && \
  ./docker_create.sh && \
  ./docker_ssh.sh

