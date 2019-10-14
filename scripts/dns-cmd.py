import os
import re
import time
import sys

CODE_FILE = 'dns-code.fc'
CODE_FILE_OUTPUT = 'dns.fif'
NEW_DNS_SCRIPT = 'new-dns.fif'

DNS_INFO = 'dns_info'
LITE_CLIENT_INFO = 'hardscreen'
DNS_INFO_PATH = './'
LITE_CLIENT_INFO_PATH = '../smart_contracts_test/'
QUERY_PATH = '../auto_dns_resolver/'

SCREEN_NAME = 'iced'
WALLET_ADDRESS = 'kf8H4FjPvnlDT7y7p0dKpU6VkDgtXhh36vLis_Qw2LwNRoSo'

amount_to_send = sys.argv[1]
dns_name = sys.argv[2]
wallet_name = sys.argv[3]
if (len(sys.argv) > 4):
    attached_boc = '-B {}'.format(sys.argv[5])
else:
    attached_boc = ''

screen_cmd = 'screen -S {} -p 0 -X stuff '.format(SCREEN_NAME)
get_seqno_cmd = '"runmethod {} seqno \n"'.format(WALLET_ADDRESS)
send_query = screen_cmd +'"sendfile {}{}-query.boc\n"'
make_hardcopy = 'screen -S {} -p 0 -X hardcopy "{}"\n'.format(SCREEN_NAME, LITE_CLIENT_INFO)

last = '"last\n"'

# get dns address
os.system('func -P -o {} stdlib.fc {}\n'.format(CODE_FILE_OUTPUT, CODE_FILE))
os.system('fift -s {} -1 {}> {}\n'.format(NEW_DNS_SCRIPT, dns_name, DNS_INFO))
with open(DNS_INFO_PATH + DNS_INFO) as f:
    content = f.read()
    non_bounceable_address = re.search('Non-bounceable address \(for init\): (.+)', content).group(1)
    bounceable_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)
    if (len(sys.argv) > 4):
        address = bounceable_address
    else:
        address = non_bounceable_address

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
os.system('fift -s wallet.fif {} {} {} {} {}'.format(wallet_name, address, seqno, amount_to_send, attached_boc))
os.system(send_query.format(QUERY_PATH, 'wallet'))
time.sleep(5)

# init DNS
if (len(sys.argv) < 5):
    os.system(send_query.format(QUERY_PATH, dns_name))


