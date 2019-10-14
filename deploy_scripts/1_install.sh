#!/bin/bash
cd ~
apt-get update
apt-get install make cmake gcc g++ libssl-dev screen zlib1g-dev python -y
wget https://test.ton.org/ton-test-liteclient-full.tar.xz
tar xf ton-test-liteclient-full.tar.xz

mkdir ~/liteclient-build
cd ~/liteclient-build
cmake ~/lite-client
cmake --build . --target lite-client
cmake --build . --target fift
cmake --build . --target func
make install
echo 'export FIFTPATH=~/lite-client/crypto/fift/lib' >> ~/.bashrc

wget https://test.ton.org/ton-lite-client-test1.config.json

echo '#!/bin/sh' > ./lite_client_start.sh
echo './lite-client/lite-client -C ton-lite-client-test1.config.json' >> ./lite_client_start.sh
chmod +x ./lite_client_start.sh
