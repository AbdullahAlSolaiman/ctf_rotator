#/bin/bash

sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-pip
sudo pip install pyfiglet
python rotator.py

