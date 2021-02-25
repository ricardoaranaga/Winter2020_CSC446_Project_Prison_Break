#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

./Prison_Builder/make_prison_SSH.sh
./Prison_Builder/make_prison_FTP.sh

python3 Layer\ -\ 2\ Prison/Layer_2.py 

sudo chown -R billythekid:billythekid /var/prison/home/billythekid
sudo chown -R patgarret:patgarret /var/ftp/patgarret/