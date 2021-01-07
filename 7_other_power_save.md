# Raspberry Pi - Power Save

#### HDMI output

Turn OFF HDMI output
```
sudo /opt/vc/bin/tvservice -o
```
Turn ON HDMI output
```
sudo /opt/vc/bin/tvservice -p
```

#### USB chip

Turn OFF USB chip
```
echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/unbind
```
Turn ON USB chip
```
echo '1-1' |sudo tee /sys/bus/usb/drivers/usb/bind
```

#### disable wifi & bluetooth

disable wifi & Bluetooth by adding following lines to /boot/config.txt
```
dtoverlay=pi3-disable-wifi
dtoverlay=pi3-disable-bt
```

#### disable LEDs

diasble leds by adding following lines to /boot/config.txt
```
dtparam=act_led_trigger=none
dtparam=act_led_activelow=on
```

#### throttle cpu

throttle cpu by adding following lines to /boot/config.txt
```
arm_freq_min=250
core_freq_min=100
sdram_freq_min=150
over_voltage_min=0
```
