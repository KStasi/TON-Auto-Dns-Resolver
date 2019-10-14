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

## Preparation

For deploying and triggering smart the light-client should be installed. The manual installation instructions can be found here https://test.ton.org/README.txt or prerequirement_scripts/1_install.sh can be used. 

As during automatic testing the light-client commands should be executed it is advised to use screen session. Use prerequirement_scripts/2_launch.sh and specify SCREEN_NAME in tests/env.

Two wallets are also needed. Their .addr and .pk can be placed in tests folder or new ones can be generated with prerequirement_scripts/3_create_wallet.sh, funded and then their code may be broadcasted with prerequirement_scripts/5_send_wallet_boc.sh. Note: wallets info should be named "main-wallet" and "secondary-wallet" and stored in tests folder.
 
To sum up:
1.  install light-client;
2.  launch screen session with light-client;
3.  create and fund two wallets;
4.  store their .pk and .addr in tests as main-wallet.* and secondary-wallet.*.

## Deployment

## Auto Testing

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

## Error Management

## How is it working?