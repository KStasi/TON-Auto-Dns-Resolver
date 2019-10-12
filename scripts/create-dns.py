import os
import re
import time

compile_cmd = 'func -P -o dns.fif stdlib.fc dns-code.fc\n'
new_dns_cmd = "fift -s new-dns.fif -1 > new_dnsresolver_out\n"
screen_cmd = 'screen -S iced -p 0 -X stuff '
get_seqno_cmd = '"runmethod kf8H4FjPvnlDT7y7p0dKpU6VkDgtXhh36vLis_Qw2LwNRoSo seqno \n"'
prepare_registrar_cmd = 'fift -s wallet.fif main-wallet '
send_wallet_query = '"sendfile ../auto_dns_resolver/wallet-query.boc\n"'
send_dns_query = '"sendfile ../auto_dns_resolver/new-dns-query.boc\n"'
make_hardcopy = 'screen -S iced -p 0 -X hardcopy "hardscreen"\n'

last = '"last\n"'
prepare_registrar_end = ' 0.5'

os.system(compile_cmd)
os.system(new_dns_cmd)
with open('new_dnsresolver_out') as f:
    content = f.read()
    non_bounceable_address = re.search('Non-bounceable address \(for init\): (.+)', content).group(1)
    bounceable_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)
    
os.system(screen_cmd + last)
time.sleep(1)   
os.system(screen_cmd + get_seqno_cmd)
time.sleep(1)   
os.system(make_hardcopy)
time.sleep(1)   
with open('../smart_contracts_test/hardscreen') as c:
    content = c.read()
    seqno = re.findall('result:  \[ (.+) \]', content)[-1]

os.system(prepare_registrar_cmd + non_bounceable_address + ' ' + seqno + prepare_registrar_end)
os.system(screen_cmd + send_wallet_query)
time.sleep(5)   
os.system(screen_cmd + send_dns_query)


