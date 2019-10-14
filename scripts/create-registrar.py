import os
import re
import time
import sys

SHOW_ADDR_SCRIPT = 'show-addr.fif'
DNS_REGISTRAR_SCRIPT = 'dns-registrar.fif'
DNS_INFO_PATH = './dns_info'

dn = sys.argv[1]
dns_name = sys.argv[2]
wallet_name = sys.argv[3]
expiration_time = sys.argv[4]

os.system('fift -s {} {}> {}\n'.format(SHOW_ADDR_SCRIPT, wallet_name, DNS_INFO_PATH))
with open(DNS_INFO_PATH) as f:
    content = f.read()
    wallet_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)

os.system('fift -s {} {}> {}\n'.format(SHOW_ADDR_SCRIPT, dns_name, DNS_INFO_PATH))
with open(DNS_INFO_PATH) as f:
    content = f.read()
    dns_address = re.search('Bounceable address \(for later access\): (.+)', content).group(1)

os.system('fift -s {} {} {} {} {}\n'.format(DNS_REGISTRAR_SCRIPT, dn, dns_address, wallet_address, expiration_time))



