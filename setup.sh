#!/bin/bash
echo "Check if is root"
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

IP_ADDR=$(hostname -I)
FULL_WEB_PATH = "/var/www/html/arenaweb"
FULL_API_PATH = "/var/www/html/arenaapi"
SERVICE_PATH = "/etc/systemd/system"

pip install -r ./requirements.txt

cp -r ./api $FULL_API_PATH
cp -r ./webapp $FULL_WEB_PATH

cp ./service_files/arenaapi.service $SERVICE_PATH
cp ./service_files/arenaweb.service $SERVICE_PATH

systemctl start arenaapi
systemctl start arenaweb
systemctl enable arenaweb
systemctl enable arenaapi