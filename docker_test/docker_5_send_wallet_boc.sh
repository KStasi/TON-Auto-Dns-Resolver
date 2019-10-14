#!/bin/sh
# source ~/.bashrc not works
docker exec -t -i `cat ../DOCKER_ID` /bin/bash -c "export FIFTPATH=~/lite-client/crypto/fift/lib && cd ~/dich4/prerequirement_scripts && ./5_send_wallet_boc.sh"

