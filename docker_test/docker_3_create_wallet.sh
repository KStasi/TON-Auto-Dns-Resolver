#!/bin/sh
# source ~/.bashrc not works
docker exec -t -i `cat ../DOCKER_ID` /bin/bash -c "export FIFTPATH=~/lite-client/crypto/fift/lib && cd ~/dich4/prerequirement_scripts && ./3_create_wallet.sh"

