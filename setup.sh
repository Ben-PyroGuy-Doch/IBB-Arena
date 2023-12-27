#!/bin/bash
echo "Check if is root"
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

IP_ADDR=$(hostname -I)
# mkdir -p /var/www/html/arenaweb
# mkdir -p /var/www/html/arenaapi
# FULL_WEB_PATH= "/var/www/html/arenaweb"
# FULL_API_PATH= "/var/www/html/arenaapi"
# SERVICE_PATH= "/etc/systemd/system"

pip install -r ./requirements.txt

cp -r ./api "/var/www/html"
cp -r ./webapp "/var/www/html"

cp ./service_files/arenaapi.service "/etc/systemd/system"
cp ./service_files/arenaweb.service "/etc/systemd/system"

systemctl daemon-reload
systemctl start arenaapi
systemctl start arenaweb
systemctl enable arenaweb
systemctl enable arenaapi