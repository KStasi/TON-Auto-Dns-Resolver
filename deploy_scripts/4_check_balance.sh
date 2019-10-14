#!/bin/sh
cd ~/dich4/tests
export MAIN_WALLET=`cat main-wallet.log | grep "Non-bounceable address" | awk '{print $5}'`
export SECONDARY_WALLET=`cat secondary-wallet.log | grep "Non-bounceable address" | awk '{print $5}'`

echo "MAIN_WALLET      = $MAIN_WALLET"
echo "SECONDARY_WALLET = $SECONDARY_WALLET"

echo "MAIN:"
curl "https://test.ton.org/testnet/account?workchain=&shard=&seqno=&roothash=&filehash=&account=$MAIN_WALLET"      2>/dev/null | grep amount
echo "SECONDARY:"
curl "https://test.ton.org/testnet/account?workchain=&shard=&seqno=&roothash=&filehash=&account=$SECONDARY_WALLET" 2>/dev/null | grep amount

echo "WARNING make sure that balance is not empty"
echo "e.g. amount:(var_uint len:5 value:20000000000))"
