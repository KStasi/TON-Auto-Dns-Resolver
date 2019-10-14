#!/bin/sh
cd ~/dich4/tests
echo "send main..."
screen -S lite-client -p 0 -X stuff "sendfile `realpath ./main-wallet-query.boc`^M"
sleep 2
echo "send secondary..."
screen -S lite-client -p 0 -X stuff "sendfile `realpath ./secondary-wallet-query.boc`^M"
