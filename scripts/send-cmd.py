import os
import re
import time
import sys

SHOW_ADDR_SCRIPT = 'show-addr.fif'

LITE_CLIENT_INFO = 'hardscreen'
DNS_INFO_PATH = './dns_info'
LITE_CLIENT_INFO_PATH = '../smart_contracts_test/'
QUERY_PATH = '../auto_dns_resolver/'

SCREEN_NAME = 'iced'

amount_to_send = sys.argv[1]
dns_name = sys.argv[2]
wallet_name = sys.argv[3]
if (len(sys.argv) > 4):
    attached_boc = '-B {}'.format(sys.argv[5])
else:
    attached_boc = ''

os.system('fift -s {} {}> {}\n'.format(SHOW_ADDR_SCRIPT, wallet_name, DNS_INFO_PATH))
with open(DNS_INFO_PATH) as f:
    content = f.read()
    wallet_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)

screen_cmd = 'screen -S {} -p 0 -X stuff '.format(SCREEN_NAME)
get_seqno_cmd = '"runmethod {} seqno \n"'.format(wallet_address)
send_query = screen_cmd +'"sendfile {}{}-query.boc\n"'
make_hardcopy = 'screen -S {} -p 0 -X hardcopy "{}"\n'.format(SCREEN_NAME, LITE_CLIENT_INFO)

last = '"last\n"'

# get dns address
os.system('fift -s {} {}> {}\n'.format(SHOW_ADDR_SCRIPT, dns_name, DNS_INFO_PATH))
with open(DNS_INFO_PATH) as f:
    content = f.read()
    non_bounceable_address = re.search('Non-bounceable address \(for init only\): (.+)', content).group(1)
    bounceable_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)
    if (len(sys.argv) > 4):
        dns_address = bounceable_address
    else:
        dns_address = non_bounceable_address

# get wallet seqno
os.system(screen_cmd + last)
time.sleep(1)   
os.system(screen_cmd + get_seqno_cmd)
time.sleep(1)   
os.system(make_hardcopy)
time.sleep(1)   
with open(LITE_CLIENT_INFO_PATH + LITE_CLIENT_INFO) as c:
    content = c.read()
    seqno = re.findall('result:  \[ (.+) \]', content)[-1]

# fund DNS
os.system('fift -s wallet.fif {} {} {} {} {}'.format(wallet_name, dns_address, seqno, amount_to_send, attached_boc))
os.system(send_query.format(QUERY_PATH, 'wallet'))
time.sleep(5)

# init DNS
if (len(sys.argv) < 5):
    os.system(send_query.format(QUERY_PATH, dns_name))


