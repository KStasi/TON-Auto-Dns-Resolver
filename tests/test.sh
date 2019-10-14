#!/bin/sh
source ./env

# create wallets
fift -s new-testgiver.fif -1
fift -s new-wallet.fif -1 main-wallet
fift -s new-wallet.fif -1 secondary-wallet
python ../scripts/send-cmd.py 12 main-wallet new-testgiver "testgiver"
sleep 10
python ../scripts/send-cmd.py 5 secondary-wallet new-testgiver "testgiver"
sleep 10
# echo "Fund wallets before continue!"
# exit 0 

# compile dns code file
func -P -o dns.fif ../auto_dns_resolver/stdlib.fc ../auto_dns_resolver/dns-code.fc

# create .boc for two dns
fift -s ../auto_dns_resolver/new-dns.fif -1 dns1
fift -s ../auto_dns_resolver/new-dns.fif -1 dns2

# deploy smart contracts
python ../scripts/send-cmd.py 0.5 dns1 main-wallet "wallet"
python ../scripts/send-cmd.py 0.5 dns2 secondary-wallet "wallet"
sleep 10

# create registrar request to main dns resolver (for domain name "start\0")
python ../scripts/create-request.py registrar 0x7374617274 dns2 main-wallet 160
python ../scripts/send-cmd.py 1.5 dns1 main-wallet "wallet" dns-registrar-query.boc
sleep 10

# check manually dns resolver in the lite client & time expiration
# also try send massage to trigger dns resolver
# results are send to "nowhere"
fift -s ../auto_dns_resolver/dns-resolver.fif 40 0x7374617274 -1
python ../scripts/send-cmd.py 1.5 dns1 main-wallet "wallet" dns-resolver-query.boc
sleep 10

# register two-level domain name ("start\0end\0")
python ../scripts/create-request.py registrar 0x737461727400656E64 dns1 main-wallet 160
python ../scripts/send-cmd.py 1.5 dns1 main-wallet "wallet" dns-registrar-query.boc
sleep 10

# check if two-level domain name ("start\0end\0") can be resolved & 
# 0x656E64 ("end") was registred on dns2 manually
# also try send massage to trigger dns resolver
# results are send to "nowhere" but search will trigger both dns 
fift -s ../auto_dns_resolver/dns-resolver.fif 72 0x737461727400656E64 0
python ../scripts/send-cmd.py 1.5 dns1 main-wallet "wallet" dns-resolver-query.boc
sleep 10

# change record
# note: it would be better to store current dns record info before continue
# to check that it is really changed
python ../scripts/create-request.py changerecord 0x7374617274 dns2 secondary-wallet 
python ../scripts/send-cmd.py 1.5 dns1 main-wallet "wallet" dns-changerecord-query.boc
sleep 10

# change expiration time
# note: it would be better to store current dns record info before continue
# to check that it is really changed
python ../scripts/create-request.py changetime 0x7374617274 200
python ../scripts/send-cmd.py 1.5 dns1 secondary-wallet "wallet" dns-changeretime-query.boc
sleep 10
