#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

rm -rf /var/ftp/patgarret
deluser --remove-home patgarret
delgroup --only-if-empty prisoners

# install ftp server
sudo apt-get update
sudo cp /etc/vsftpd.conf  /etc/vsftpd.conf_default
sudo apt install vsftpd

# launch ftp server
sudo systemctl start vsftpd
sudo systemctl enable vsftpd

# add grouo and user
groupadd prisoners
adduser patgarret
adduser patgarret prisoners
sudo mkdir /home/testuser
echo Added prisoners group and patgarret user

# allow incomming connections
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp

files=('/var/prison/etc/passwd' '/var/prison/etc/group')
for file in ${files[@]}; do
sed -i '/root\|prisoners\|billythekid/!d' $file
echo $file modified
done

mkdir /var/prison/home /var/prison/home/billythekid
cp -r /etc/skel/ /var/prison/home/billythekid
mv /var/prison/home/billythekid/skel/.* /var/prison/home/billythekid
rm -rf /var/prison/home/billythekid/skel/

cp .bashrc /var/prison/home/billythekid/
chown -R billythekid:billythekid /var/prison/home/billythekid

cp -r /lib/* /var/prison/lib

source ~/.bashrc

echo PRISON BREAK CREATED

apt install openssh-server

echo Match group prisoners >> /etc/ssh/sshd_config
echo -e '\t' ChrootDirectory /var/prison/ >> /etc/ssh/sshd_config
echo -e '\t' X11Forwarding no >> /etc/ssh/sshd_config
echo -e '\t' AllowTcpForwarding no >> /etc/ssh/sshd_config

service ssh restart

echo SERVER READY FOR JAILED CONNECTIONS 