FROM ubuntu:18.04
WORKDIR /root

RUN echo '14.10.2019' && apt-get update

RUN apt-get install make cmake gcc g++ libssl-dev screen zlib1g-dev python wget curl xz-utils -y

RUN wget https://test.ton.org/ton-test-liteclient-full.tar.xz && \
  tar xf ton-test-liteclient-full.tar.xz

RUN mkdir ~/liteclient-build && \
  cd ~/liteclient-build && \
  cmake ~/lite-client 

RUN cd ~/liteclient-build && cmake --build . --target lite-client 
RUN cd ~/liteclient-build && cmake --build . --target fift
RUN cd ~/liteclient-build && cmake --build . --target func
RUN cd ~/liteclient-build && make install

RUN cd ~/liteclient-build && \
  echo 'export FIFTPATH=~/lite-client/crypto/fift/lib' >> ~/.bashrc && \
  wget https://test.ton.org/ton-lite-client-test1.config.json

RUN cd ~/liteclient-build && \
  echo '#!/bin/sh' > ./lite_client_start.sh && \
  echo './lite-client/lite-client -C ton-lite-client-test1.config.json' >> ./lite_client_start.sh && \
  chmod +x ./lite_client_start.sh 

RUN mkdir dich4

COPY . /root/dich4
COPY docker_env /root/dich4/tests/env

CMD cd ~/liteclient-build && \
  screen -mS lite-client ./lite_client_start.sh
