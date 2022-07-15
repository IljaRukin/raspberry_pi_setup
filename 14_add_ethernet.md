# add ethernet (hanrun w5500 module)

## pinout:

```
3.3V-3.3V[17]
MISO-MISO[21]
MOSI-MOSI[19]
SCS-SPICE0[24]
SCLK-CLK[23]

5V-/
GND-GND[20]
RST-#GPIO24[18]#
INT-GPIO25[22] 
NC-/
```

## configure pi

confirm the presence of:
```
/boot/overlays/anyspi.dtbo
/boot/overlays/w5500.dtbo
```

edit file
```
sudo nano /boot/config.txt
```
by adding the following lines
```
dtoverlay=anyspi,spi0-0,dev="w5500",speed=30000000
dtoverlay=w5500
```

enable spi
```
sudo raspi-config
```

list network devices (for testing)
```
ifconfig
```
under "Interface Options"->"SPI"->"Yes"

### set permanent MAC

read out mac
```
ifconfig
```

make MAC permanent
```
sudo apt-get install macchanger
sudo nano /etc/systemd/system/changemac@.service
```

add text
```
[Unit]
Description=changes mac for %I
Wants=network.target
Before=network.target
BindsTo=sys-subsystem-net-devices-%i.device
After=sys-subsystem-net-devices-%i.device

[Service]
Type=oneshot
ExecStart=/usr/bin/macchanger --mac=e2:ec:fb:70:0b:6b %I
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

enable service
```
sudo systemctl enable changemac@eth0.service
```

display mac (test)
```
macchanger -s eth0
```

then add a manual entry to your router for said MAC

### set up static ip
(did it work ?; don't know!)
edit file
```
sudo nano /etc/dhcpcd.conf
```

add text
```
interface eth0
metric 1
static ip_address=192.168.2.105/24
#static ip6_address=fd51:42f8:caae:d92e::ff/64
static routers=192.168.2.1
static domain_name_servers=192.168.2.1
#static domain_name_servers=192.168.2.1 8.8.8.8 fd51:42f8:caae:d92e::1

interface wlan0
metric 2
static ip_address=192.168.2.130/24
#static ip6_address=fd51:42f8:caae:d92e::ff/64
static routers=192.168.2.1
static domain_name_servers=192.168.2.1
#static domain_name_servers=192.168.2.1 8.8.8.8 fd51:42f8:caae:d92e::1
```

### optional

enable/disable other network interfaces (e.g. wifi)
```
sudo raspi-config
ifconfig wlan0 down
```
