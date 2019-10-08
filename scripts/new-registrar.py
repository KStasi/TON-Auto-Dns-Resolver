import os
import re
import time

compile_cmd = 'func -P -o dns-resolver.fif stdlib.fc store.fc\n'
new_dns_cmd = "fift -s new-dns-resolver.fif  0 > new_dnsresolver_out\n"
screen_cmd = 'screen -S iced -p 0 -X stuff '
get_seqno_cmd = '"runmethod kQDcBokBQyDW0yhsKn4agtPGgT1XBGEWXrD1O_Ic_nbYdvAU seqno \n"'
prepare_registrar_cmd = 'fift -s wallet.fif  mai-wal '
send_wallet_query = '"sendfile ../auto_dns_resolver/wallet-query.boc\n"'
send_dns_query = '"sendfile ../auto_dns_resolver/new-dns-query.boc\n"'
make_hardcopy = 'screen -S iced -p 0 -X hardcopy "hardscreen"\n'

last = '"last\n"'
prepare_registrar_end = ' 0.1'
code =  ' -B dns-registrar-query.boc'

os.system(compile_cmd)
os.system(new_dns_cmd)
with open('new_dnsresolver_out') as f:
    content = f.read()
    non_bounceable_address = re.search('Non-bounceable address \(for init\): (.+)', content).group(1)
    bounceable_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)
    
os.system(screen_cmd + last)
time.sleep(1)   
os.system(screen_cmd + get_seqno_cmd)
time.sleep(3)   
os.system(screen_cmd + get_seqno_cmd)
time.sleep(1)   
os.system(make_hardcopy)
with open('../smart_contracts_test/hardscreen') as c:
    content = c.read()
    seqno = re.findall('result:  \[ (.+) \]', content)[-1]

os.system(prepare_registrar_cmd + bounceable_address + ' ' + seqno + prepare_registrar_end + code)
os.system(screen_cmd + send_wallet_query)
