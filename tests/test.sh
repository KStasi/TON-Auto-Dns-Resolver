source ./env

# create wallets
# fift -s new-wallet.fif -1 main-wallet
# fift -s new-wallet.fif -1 secondary-wallet
# echo "Fund wallets before continue!"
# exit 0 

# compile dns code file
# func -P -o dns.fif stdlib.fc  ${AUTO_DNS_PATH}dns-code.fc

# create .boc for two dns
# fift -s ${AUTO_DNS_PATH}new-dns.fif -1 dns1
# fift -s ${AUTO_DNS_PATH}new-dns.fif -1 dns2

# deploy smart contracts
# python ${SCRIPTS_PATH}send-cmd.py 0.5 dns1 main-wallet 
# python ${SCRIPTS_PATH}send-cmd.py 0.5 dns2 secondary-wallet

# create registrar request to main dns resolver 
# python ${SCRIPTS_PATH}create-registrar.py "start" dns1 main-wallet 160
# python ${SCRIPTS_PATH}send-cmd.py 1.5 dns1 main-wallet dns-registrar-query.boc

# check manually dns resolver in the lite client & time expiration
# also try send massage to trigger dns resolver
# results are send to "nowhere"
# fift -s ${AUTO_DNS_PATH}dns-resolver.fif "start" -1
# python ${SCRIPTS_PATH}send-cmd.py 1.5 dns1 main-wallet dns-resolver-query.boc

# crea
python ${SCRIPTS_PATH}create-registrar.py $'\x76\x00\x99' dns2 secondary-wallet 160
# python ${SCRIPTS_PATH}send-cmd.py 1.5 dns1 main-wallet dns-registrar-query.boc
#python ${SCRIPTS_PATH}create-registrar.py 0.5 dns2 secondary-wallet 