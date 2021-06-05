# Raspberry Pi - mounting drive

install ntfs and exfat drivers
```
sudo apt-get install ntfs-3g
sudo apt-get install exfat-fuse exfat-utils
```

list devices
```
sudo blkid -o list
```

create directory for storage device mounting point
```
sudo mkdir /media/storage
```

mount device
```
sudo mount -t auto -o utf8,uid=pi,gid=pi,noatime /dev/sda /media/storage
```

if formation is known use instead auto following keywords
```
FAT32		vfat
NTFS		ntfs-3g
HFS+		hfsplus
exFAT		exfat
ext4		ext4
```

unmount device
```
sudo umount /media/sda
```

### mount on start
by editing
```
sudo nano -Bw /etc/fstab
```
and adding:
```
UUID=52867E21867E062F /media/storage auto default,user,nofail 0 2
```
and changing permissions
```
sudo chmod -R 0777 /media/storage
```
