#!/bin/sh
source ./env

# create wallets
# fift -s new-wallet.fif -1 main-wallet
# fift -s new-wallet.fif -1 secondary-wallet
# echo "Fund wallets before continue!\n"

# compile dns code file
func -P -o dns.fif stdlib.fc  ${AUTO_DNS_PATH}dns-code.fc

# create .boc for two dns
fift -s ${AUTO_DNS_PATH}new-dns.fif -1 ${MAIN_DNS_NAME}
fift -s ${AUTO_DNS_PATH}new-dns.fif -1 ${SECONDARY_DNS_NAME}

# deploy smart contracts

python ${SCRIPTS_PATH}send-cmd.py 0.5 main-wallet ${MAIN_DNS_NAME} 
