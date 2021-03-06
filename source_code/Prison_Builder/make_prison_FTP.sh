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
echo -e "\e[96m \e[5m \e[4m \e[1m Type the following password for patgarret = BillyTheKid \e[0m"
adduser --gecos --guiet patgarret 
adduser --gecos --guiet patgarret prisoners
sudo mkdir /home/patgarret
sudo mkdir /var/ftp/patgarret
echo Added prisoners group and patgarret user

# change home path
mount --bind /home/patgarret /var/ftp/patgarret/
usermod -d /var/ftp/patgarret/ patgarret

# allow incomming connections
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp

# configuring the ftp server
touch /etc/vsftpd.chroot_list 
echo chroot_local_user=YES >> /etc/vsftpd.conf
echo chroot_list_enable=YES >> /etc/vsftpd.conf
echo allow_writeable_chroot=YES >> /etc/vsftpd.conf
echo chroot_list_file=/etc/vsftpd.chroot_list >> /etc/vsftpd.conf

# restart servers
systemctl restart vsftpd
systemctl restart vsftpd.service


echo PATGARRET PRISON CREATED