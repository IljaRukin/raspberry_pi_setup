# Raspberry Pi - setup firewall
firewall is setup by iptables, ufw is a tool for simple setup of iptables

install ufw
```
sudo apt install ufw
```

enable firewall
```
sudo ufw enable
```

disable firewall
```
sudo ufw disable
```

open port
```
sudo ufw allow #port_nr#
```

disable port
```
sudo ufw deny #port_nr#
```

list all settings
```
sudo ufw status
```

### enable ipv6 by editing config file
```
sudo nano /etc/default/ufw
```
#and adding:
```
IPV6=yes
```

### my setup
```
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw allow 1883
sudo ufw allow 8883
sudo ufw allow 139
sudo ufw allow 445
sudo ufw enable
```
