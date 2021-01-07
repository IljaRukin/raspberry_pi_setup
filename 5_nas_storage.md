# Raspberry Pi - NAS storage

install nas software
```
sudo apt-get install samba
```

### user/password setup
new group
```
sudo addgroup #smbgrp#
```
delete group
```
sudo groupdel #smbgrp#
```
new user
```
useradd #user# -G #smbgrp#
```
new password
```
sudo smbpasswd -a #user#
```

### prepare drive
mount the drive:
```
sudo mount -t auto -o utf8,uid=pi,gid=pi,noatime /dev/sda /media/storage
```
change folder access permission:
```
sudo chown root:#smbgrp# /media/storage
```

### configure samba
to create directory "everyone" to be accessible by everyone and a secure "directory" wich can only be accessed via login/password. edit the config file:
```
sudo nano /etc/samba/smb.conf
```
and add athe the end:
```
[everyone]
path = /media/storage
veto files = /media/storage/Secure
comment = Data
browseable = yes
writeable = yes
read only = no
create mask = 0777
directory mask = 0777
public = yes
guest ok = yes
only guest = no

[secure]
#path = /media/storage/Secure
path = /media/storage
valid user = @#smbgrp#
browseable = yes
writeable = yes
read only = no
```
and restart it
```
sudo service smbd restart
sudo systemctl restart smbd.service
```
