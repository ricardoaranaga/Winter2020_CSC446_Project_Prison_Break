#!/bin/bash

if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

rm -rf /var/prison
deluser --remove-home billythekid
delgroup --only-if-empty prisoners

./source_code/Prison_Builder/jail.sh /bin/{ls,cat,echo,bash,mkdir,touch} /usr/bin/{vim,whoami,scp} /etc/hosts

#add useful “special” files:
mkdir /var/prison/dev
mknod -m 0666 /var/prison/dev/null c 1 3
mknod -m 0666 /var/prison/dev/random c 1 8
mknod -m 0444 /var/prison/dev/urandom c 1 9
echo Added usefull special files

# add grouo and user
groupadd prisoners
echo -e "\e[96m \e[5m \e[4m \e[1m Type the following password for billythekid = PatGarret \e[0m"
adduser --gecos --guiet billythekid
adduser --gecos --guiet billythekid prisoners
echo Added prisoners group and billythekid user

cp /etc/passwd /etc/group /var/prison/etc/

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

echo BILLYTHEKID PRISON CREATED

apt install openssh-server

echo Match group prisoners >> /etc/ssh/sshd_config
echo -e '\t' ChrootDirectory /var/prison/ >> /etc/ssh/sshd_config
echo -e '\t' X11Forwarding no >> /etc/ssh/sshd_config
echo -e '\t' AllowTcpForwarding no >> /etc/ssh/sshd_config

service ssh restart

echo SERVER READY FOR JAILED CONNECTIONS 