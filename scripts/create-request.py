import os
import re
import sys

dns_action = sys.argv[1]
dn = sys.argv[2]
if dns_action == "changetime":
    expiration_time = sys.argv[4]
else:
    dns_name = sys.argv[3]
    wallet_name = sys.argv[4]
    if dns_action == "registrar":
        expiration_time = sys.argv[5]


def get_address(file_base):
    dns_info_path = os.environ.get('DNS_INFO_PATH')
    os.system('fift -s show-addr.fif {}> {}\n'.format(file_base, dns_info_path))
    with open(dns_info_path) as f:
        content = f.read()
        return re.search('Bounceable address \(for later access\): (.+)', content).group(1)

wallet_address = get_address(wallet_name)
dns_address = get_address(dns_name)

# fu..antastic magic with int added to be able code domain names with \x00
if dns_action == "registrar":
    os.system('fift -s {} {} {} {} {} {}\n'.format("../auto_dns_resolver/dns-registrar.fif", (len(dn) / 2 - 1) * 8, int(dn, 16), dns_address, wallet_address, expiration_time))
elif dns_action == "changerecord":
    os.system('fift -s {} {} {} {} {}\n'.format("../auto_dns_resolver/dns-changerecord.fif", (len(dn) / 2 - 1) * 8, int(dn, 16), dns_address, wallet_address))
elif dns_action == "changetime":
    os.system('fift -s {} {} {} {} {}\n'.format("../auto_dns_resolver/dns-changetime.fif", (len(dn) / 2 - 1) * 8, int(dn, 16), expiration_time))

