#!/bin/bash
echo "Check if is root"
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

IP_ADDR=$(hostname -I)
WLANINT="wlan1"
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
apt install dnsmasq hostapd

systemctl daemon-reload
systemctl start arenaapi
systemctl start arenaweb
systemctl enable arenaweb
systemctl enable arenaapi
systemctl stop dnsmasq
systemctl stop hostapd

cat << EOF >> /etc/dhcpcd.conf
interface $WLANINT
    static ip_address=192.168.7.1/24
    nohook wpa_supplicant
EOF

cat << EOF >> /etc/dnsmasq.conf
interface=$WLANINT
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
EOF

cat << EOF >> /etc/hostapd/hostapd.conf
country_code=GB
interface=$WLANINT
ssid=IBB_Arena
channel=9
auth_algs=1
wpa=2
wpa_passphrase=Activate!
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP CCMP
rsn_pairwise=CCMP
EOF

cat << EOF >> /etc/default/hostapd
interface=$WLANINT
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
EOF

sed -i "s/^#DAEMON_CONF.*/DAEMON_CONF="/etc/hostapd/hostapd.conf"/" "/etc/default/hostapd"

service dhcpcd restart
systemctl start dnsmasq
systemctl unmask hostapd
systemctl enable hostapd
systemctl start hostapd