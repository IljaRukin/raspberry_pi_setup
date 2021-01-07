# Raspberry Pi - hdd power save

install 
```
sudo apt-get install hdparm
```
list devices
```
sudo blkid -o list
```
put into standby
```
sudo hdparm -y /dev/sda
```
return power mode
```
sudo hdparm -C /dev/sda
```
get drive info
```
sudo hdparm -I /dev/sda
```

### set power save (for supported drives)

set power save modes direct
```
sudo hdparm -B1 /dev/sda
```
or edit configuration
```
sudo nano /etc/hdparm.conf
```
by adding:
```
/dev/sda {
	write_cache = on
	#1 min spindown
	spindown_time = 12
}
```

-----

### power save alternative (for not supported drives)
run cronjob to power down drive every 10min

create script:
```
sudo nano hdd_standby.sh
```
with content:
```
#!/bin/bash
# This script looks for recent disk access, and if nothing has changed, puts /dev/"drive" into spindown mode.
# This should be used only is the hdparm power management function is not working.
# Call this script with cron or manually as desired
#
#
#
# Change which drive this script looks at by changing the drive variable below:
drive="sda1"
#
#
current=`date`
caller=$(ps ax | grep "^ *$PPID" | awk '{print $NF}')
filename="/tmp/diskaccess.txt"
if [ -f "$filename" ]; then
    stat_old=`cat "$filename" | tr -dc "[:digit:]"`
#    stat_new=`cat /sys/block/"$drive"/stat | tr -dc "[:digit:]"`
    stat_new=`cat /sys/block/sda/stat | tr -dc "[:digit:]"`
    if [ "$stat_old" == "$stat_new" ]; then
        stat="0"
        echo "The disk hasn't been used; spinning down /dev/$drive"
        echo $stat_old
        sudo hdparm -y /dev/$drive > /dev/null
    else
        stat="1"
        echo $stat_old
        echo $stat_new
        echo "The drive has been used..."
        echo $stat_new > $filename
    fi
else
    echo "/tmp/diskaccess.txt file does not exist; creating it now."
    echo $stat_new > $filename
fi
echo $stat " - " $drive " - " $current " - by: " $caller >> /tmp/diskaccesslog.txt
```
make executable
```
sudo chmod +x hdd_standby.sh
```
and add cronjob
```
crontab -e
*/10 * * * * /home/pi/hdd_standby.sh
```
