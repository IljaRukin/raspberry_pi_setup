# Raspberry Pi - bluetooth

install
```
sudo apt-get install bluetooth bluez blueman
sudo reboot
```

#bluetooth options
```
sudo systemctl start hciuart
sudo bluetoothctl
```

#turn agent on
```
agent on
default-agent
```

#scan for available bluetooth devices
```
scan on
```

#pairing
```
pair #MAC#
```
