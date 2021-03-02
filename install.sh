#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

sudo ./source_code/Prison_Builder/make_prison_FTP.sh
sudo ./source_code/Prison_Builder/make_prison_SSH.sh

sudo python3 ./source_code/Prison_Builder/Layer_2.py 

sudo chown -R billythekid:billythekid /var/prison/home/billythekid
sudo chown -R patgarret:patgarret /var/ftp/patgarret/

echo ALL DONE - CHALLENGE DEPLOYED