import os
import re
import time
import sys

def get_address(file_base, is_bounceable):
    os.system('fift -s show-addr.fif {}> "dns_info"\n'.format(file_base))
    with open("dns_info") as f:
        content = f.read()
        non_bounceable_address = re.search('Non-bounceable address \(for init only\): (.+)', content).group(1)
        bounceable_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)
        if (is_bounceable):
            return bounceable_address
        else:
            return non_bounceable_address

# export neccessary env variables
screen_name = os.environ.get('SCREEN_NAME')
query_path = os.environ.get('QUERY_PATH')

# export args
amount_to_send = sys.argv[1]
dns_name = sys.argv[2]
wallet_name = sys.argv[3]
script_name = sys.argv[4]
if (len(sys.argv) > 5):
    attached_boc = '-B {}'.format(sys.argv[4])
else:
    attached_boc = ''

# get dns address

wallet_address = get_address(wallet_name, True)
dns_address = get_address(dns_name, len(sys.argv) > 5)
screen_cmd = 'screen -S {} -p 0 -X stuff '.format(screen_name)
get_seqno_cmd = '"runmethod {} seqno \n"'.format(wallet_address)
send_query = screen_cmd +'"sendfile {}{}-query.boc\n"'
make_hardcopy = 'screen -S {} -p 0 -X hardcopy "{}/hardscreen"\n'.format(screen_name, os.getcwd())
last = '"last\n"'

# get wallet seqno
os.system(screen_cmd + last)
time.sleep(1)   
os.system(screen_cmd + get_seqno_cmd)
time.sleep(1)   
os.system(make_hardcopy)
time.sleep(1)   
with open(os.getcwd() +"/hardscreen") as c:
    content = c.read()
    seqno = re.findall('result:  \[ (.+) \]', content)[-1]

# fund DNS
if 'testgiver.fif':
    wallet_name = ''
os.system('fift -s {}.fif {} {} {} {} {}'.format(script_name, wallet_name, dns_address, seqno, amount_to_send, attached_boc))
os.system(send_query.format(query_path, script_name))
time.sleep(5)

# init DNS
if (len(sys.argv) < 6):
    os.system(send_query.format(query_path, dns_name))


