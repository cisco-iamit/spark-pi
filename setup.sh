#!/bin/bash
sudo apt-get update
sudo rpi-update
sudo raspi-config update
sudo apt-get install -y gpac git mongodb
pip3 install -r requirements.txt --user
cd app && mkdir tmp
