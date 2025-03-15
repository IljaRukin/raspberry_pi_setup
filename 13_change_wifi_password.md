# change wifi password

open wifi config file
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

and change ssid & psk to yours
then restart pi
```
sudo reboot
```

---

or use the network manager
```
nmtui
```
start if, if it is not running prior
```
sudo systemctl start NetworkManager
```
