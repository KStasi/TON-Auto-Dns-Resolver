#!/bin/bash
FAUCET_WALLET="kf-BdKbgJX301tRz0Z1wGRU2kdMFOqniu1TXOVpyhGWYmK9A"
curl "https://test.ton.org/testnet/account?workchain=&shard=&seqno=&roothash=&filehash=&account=$FAUCET_WALLET" 2>/dev/null | grep amount
