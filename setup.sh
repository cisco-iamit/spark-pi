#!/bin/bash
sudo apt-get update
sudo rpi-update
sudo raspi-config update
sudo apt-get install gpac
pip3 install -r requirements.txt --user
reboot
