#!/bin/sh
cd ~/liteclient-build
screen -dmS lite-client ./lite_client_start.sh
echo "Open new terminal and open lite-client with"
echo "  screen -R lite-client"
