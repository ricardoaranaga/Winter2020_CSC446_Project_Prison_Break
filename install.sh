#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

sudo ./source_code/Prison_Builder/make_prison_FTP.sh
sudo ./source_code/Prison_Builder/make_prison_SSH.sh

sudo python3 ./source_code/Layer\ -\ 2\ Prison/Layer_2.py
cd source_code/Layer\ -\ 3\ Stegging/
sudo python3 store_normal_rev_Steg.py -b

sudo chown -R billythekid:billythekid /var/prison/home/billythekid
sudo chown -R patgarret:patgarret /var/ftp/patgarret/

echo ALL DONE - CHALLENGE DEPLOYED