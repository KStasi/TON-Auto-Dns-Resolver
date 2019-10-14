#!/bin/sh
cd ~/dich4/tests
export MAIN_WALLET=`cat main-wallet.log | grep "Non-bounceable address" | awk '{print $5}'`
export SECONDARY_WALLET=`cat secondary-wallet.log | grep "Non-bounceable address" | awk '{print $5}'`

echo "MAIN_WALLET      = $MAIN_WALLET"
fift -s testgiver.fif $MAIN_WALLET 0 0.5
screen -S lite-client -p 0 -X stuff "sendfile `realpath ./testgiver-query.boc`^M"

echo "SECONDARY_WALLET = $SECONDARY_WALLET"
fift -s testgiver.fif $SECONDARY_WALLET 0 0.5
screen -S lite-client -p 0 -X stuff "sendfile `realpath ./testgiver-query.boc`^M"
