import os
import re
import sys

dn = sys.argv[1]
dns_name = sys.argv[2]
wallet_name = sys.argv[3]
expiration_time = sys.argv[4]

show_addr_script_path = os.environ.get('SHOW_ADDR_SCRIPT_PATH')
dns_registrar_script = os.environ.get('DNS_REGISTRAR_SCRIPT_PATH')

def get_address(file_base):
    dns_info_path = os.environ.get('DNS_INFO_PATH')
    os.system('fift -s {} {}> {}\n'.format(show_addr_script_path, file_base, dns_info_path))
    with open(dns_info_path) as f:
        content = f.read()
        return re.search('Bounceable address \(for later access\): (.+)', content).group(1)



wallet_address = get_address(wallet_name)
dns_address = get_address(dns_name)

# fu..antastic magic with int added to be able code domain names with \x00
os.system('fift -s {} {} {} {} {} {}\n'.format(dns_registrar_script, (len(dn) / 2 - 1) * 8, int(dn, 16), dns_address, wallet_address, expiration_time))



