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
former the initial login data was:
```
login: pi
password: raspberry
```
with the new version no default user exist. therefore a user should be defined in a file "/boot/userconf" with the content
```
username:hashed-password
```
to generate the hashed password run the python script "generate_hash.py"

### edit users
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
