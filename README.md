## Abstract

The current document aims to describe how the proposed Automatic DNS Resolver designed, how to deploy the smart contract and trigger its functions. The instructions are supposed to be launched on macOS but it should be suitable for most of Unix systems.

## Project layout

The project has the following structure:
dich4/
	auto_dns_resolver/
	prerequirement_scripts/
	scripts/
	tests/

**auto_dns_resolver** contains smart contract and fift scripts for deployment and triggering it (also some debug scripts can be found in git history inside this folder).
**prerequirement_scripts** contains shell scripts to prepare environment for smart contract deployment and triggering.
**scripts** contains useful scripts for quick interaction with smart contract (actually, wrappers for fift scripts).
**tests** contains scripts for testing smart contract functionality. 

## Smart Contract Folder

The Automatic DNS Resolver smart contract is stored in dns-code.fc. IT depends on stdlib.fc.

dns.fif is compiled a version of dns-code.fc

new-dns.fif takes <workchain-id> and creates new dns resolver init msg. It depends on dns.fif.

dns-registrar.fif takes <domain-name-length> <domain-name> <identifier> <owner> <expirational-time> and creates msg-body for dns registrar request.

dns-resolver.fif takes <domain-name-length> <domain-name> <category> and creates msg-body for dns resolver request (it is quite different from getter as it provides recursive research among other resolvers if neccessary).

dns-changerecord.fif takes <domain-name-length> <domain-name> <identifier> <owner>  and creates msg-body for request to change dns record.

dns-changetime.fif takes <domain-name-length> <domain-name> <extra-time>   and creates msg-body for request to expand dns record expiration time.

Note: the domain name has integer (or hex) representation in order to avoid issues with \x00. But for this approach domain name length also id needed.

## DNS Code

Lets consider each function. 

There are two function for loading and storing data: `(int, cell, int, int, int, int, int, int, int) load_data()` & `(int, cell, slice) load_short_data()` and `() store_data(int seqno, cell dnst, int pk, int std_time, int std_payment, int std_change_payment, int ext_tm_payment, int ext_bit_payment, int ext_ref_payment)` & `() store_short_data(int seqno, cell dnst, slice other)`. Not all persistant data are used with the same frequency so in order not to load to many unnesessary data and fill out the stack with separate instances the shortes version was created for the most common slice parts. But friendly speaking, it probably would be better to store "rare" values in ref.

There some internal masseges with simmilar structure so the function to send them was implemented as  `() send_message(int type, int type_len, slice addr, int op, int query_id, slice msg_body, int grams, int mode)`. 

The function for subdomain name registration is `() dnsregistrar(int query_id, int msg_value, slice in_msg)`. It checks whether there is no active subdomain (time is expires) with this name, send request to next subdomain if necessary and checks if msg_value is enough for payment. If all is right new record is added. The entrails of record aren't validated. Owner may add any values he wishes. He pays for bits and refs number not for the content. Nevertheless note: category -3 is allways redefined with expiration time. 

`() changerecord(int query_id, int msg_value, slice s_addr, slice in_msg)` allows owner to modify their records and extend the registration period. 

For now `() recv_external(slice in_msg)` allows owner to execute any actions. This method is expected to be used to withdraw DNS resolver profit.

`() recv_internal(int msg_value, cell in_msg_cell, slice in_msg)` expects the massege body with the following structure:

```
dns_registratr$_  domain_name:^Cell
	dns_record:(HashmapE 16 ^DNSRecord) extra_registrar_time:uint32 = Params;
```

```
dns_change_record$_  domain_name:^Cell
	data:(Either (HashmapE 16 ^DNSRecord) uint32) = Params;
```

```
dns_resolver$_  domain_name:^Cell
	cathegory:uint32 = Params;
```

```
msg_body$_ {X:Type} op:uint32
	query_id:uint64 body:Params = X;
```

`(int, int, int, int, int, int) getpayment()` is a getter for standart registration time and payments for each bit, ref and extra registration time along with price for modification record in the future.

To predict the total price for dsubdomain registration the getter `(int) calc_cost(int et, int cdn_bits, int cdn_refs)` was implemented.

To look up for subdomain info `(int, cell) dnsresolve(slice dn, int c)` was inmblemented, it takes subdomain and cathegory to look up and returns the result or next resolver info for the biggist sequence found.

The expiration time of some subdomain can be found with `(int) getexpirationtime(slice dn)`.

And standart `int seqno()` was also added.

## Testing on Host

### Preparation For Testing

For deploying and triggering smart the light-client should be installed. The manual installation instructions can be found here https://test.ton.org/README.txt or prerequirement_scripts/1_install.sh can be used. 

As during automatic testing the light-client commands should be executed it is advised to use screen session. Use prerequirement_scripts/2_launch.sh and specify SCREEN_NAME in tests/env.

Deprecated: Two wallets are also needed. Their .addr and .pk can be placed in tests folder or new ones can be generated with prerequirement_scripts/3_create_wallet.sh, funded and then their code may be broadcasted with prerequirement_scripts/5_send_wallet_boc.sh. Note: wallets info should be named "main-wallet" and "secondary-wallet" and stored in tests folder.

For now wallets are created during testing and are funded with own test giver (it isn't very rich but enough for few test iterations, yoi may fund it as well;)).
 
To sum up:
1.  install light-client;
2.  launch screen session with light-client.

### Auto Testing

Open terminal and go to tests/.

Configure the env file. The variables must be mentioned:
	SCREEN_NAME - name of the light-client screen session
	QUERY_PATH - path to place where generated .boc files are stored (  for testing, should be the absolute path to tests/ .

Add executable permissions for test.sh
```
chmod +x test.sh 
```
run it:
```
./test.sh
```
Test descriptions are placed in file itself. Note: it uses sleep 10 to wait for the transaction is executed but it may not be enough or any other connection error can occur. We don't pretend it is a great way for testing.
 
## Manual Testing

## DNS persistent data

The data is stored as folloving:

```
storage$_ seqno:uint32 dns_table:PrefixxDictionary owner_pk:uin32
	std_registration_time:uint32 std_registration_payment:uint6, std_change_payment:uint6, extra_time_payment:uint6, int extra_bit_payment::uint6, extra_reference_payment:uint6 = Storage;
```

As for the payment it stores power of 2 which we need to calculate real price. It allowes to store data compactly. Howewer it is less flexible. 

## Error Management

## How is it working?