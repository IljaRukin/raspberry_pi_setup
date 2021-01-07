# Raspberry Pi - first setup

### enable ssh
paste (empty) file "ssh" into /boot/ssh on sdcard

### setup wifi
paste file /boot/wpa_supplicant.conf with your ssid login on sd card
```
country=DE 
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev 
update_config=1 
network={
     ssid="#WLAN SSID#"
     scan_ssid=1
     psk="#WLAN PASSWORT#"
     key_mgmt=WPA-PSK
}
```

###  login data
initial
```
login: pi
password: rasberry
```
change password
```
passwd
```
add user:
```
sudo adduser #name#
```
remove user (close all processes, remove user, remove home folder of user):
```
sudo pkill -u #name#
sudo deluser #name#
sudo deluser -remove-home #name#
```

### change network name
```
sudo raspi-config
*network options
*hostname
```

### install micro text editor
install:
```
wget https://getmic.ro
bash index.html
sudo mv /home/pi/micro /bin/
```
open file with micro text editor :
```
micro file.txt
```
