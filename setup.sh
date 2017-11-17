#!/bin/bash
sudo apt-get update
sudo apt-get install -y git mongodb
sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xzvf Python-3.6.2.tgz
cd Python-3.6.2/
./configure
make
sudo make install
rm -rf Python-3.6.2/ Python-3.6.2.tgz
pip3 install -r requirements.txt --user