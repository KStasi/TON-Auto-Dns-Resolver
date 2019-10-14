#!/bin/sh
cd ~/dich4/tests
fift -s new-wallet.fif -1 main-wallet | tee main-wallet.log

fift -s new-wallet.fif -1 secondary-wallet | tee secondary-wallet.log


export MAIN_WALLET=`cat main-wallet.log | grep "Non-bounceable address" | awk '{print $5}'`
export SECONDARY_WALLET=`cat secondary-wallet.log | grep "Non-bounceable address" | awk '{print $5}'`
echo "MAIN_WALLET      = $MAIN_WALLET"
echo "SECONDARY_WALLET = $SECONDARY_WALLET"
echo "Fill both with gramms to proceed"
