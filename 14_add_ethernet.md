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
dtoverlay=W5500LAN,spi0-0,dev="w5500",speed=30000000
dtoverlay=w5500
```

list network devices (for testing)
```
ifconfig 
```

enable/disable other network interfaces (e.g. wifi)
```
sudo raspi-config
```
