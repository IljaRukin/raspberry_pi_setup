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

### 
```
sudo raspi-config
```

### 
```
\boot\config.txt
```

### 
```
dtoverlay=w5500
```
