# Raspberry Pi - domain ip update dynv6

### setup domain with 
- register at dynv6
- chose hostname
- get secret token

### create ipv6 update script:
```
sudo nano dynv6.sh
```

with the following script:
```
#!/bin/sh
hostname="..."
token="..."
previous_ipv6="$(head -n 1 /var/www/html/ip_update/ipv6.txt)"
current_ipv6="$(ip -6 addr list scope global | grep -v "fd" | sed -n 's/.*inet6 \([0-9a-f:]\+\).*/\1/p' | head -n 1)"

#echo "$current_ipv6"
#echo "$previous_ipv6"

if [ "$current_ipv6" != "$previous_ipv6" ];
	then
	#echo "ipv6 did change"
	wget -O /dev/null -o /dev/null "https://dynv6.com/api/update?hostname=$hostname&ipv6=$current_ipv6&token=$token" > /dev/null 2>&1
	#wget -O- /dev/null "https://dynv6.com/api/update/?hostname=$hostname&ipv4=$current_ipv4&token=$token" > /dev/null 2>&1
	#if last command had no error $?=0
	if [ "$?" != "0" ];
		then
		:
		#echo "no network connection"
	else
		#echo "successful update"
		echo "$current_ipv6" > /var/www/html/ip_update/ipv6.txt
	fi
else
	:
	#echo "ipv6 did not changed"
fi
```
wich updates ip address of your web domain if the ip adress of your raspberry pi changed

make script executable:
```
sudo chmod +x dynv6.sh
```

create new crontab task:
```
crontab -e
```
with update every 5 minutes
```
*/5 * * * * /var/www/html/dynv6.sh
```

list crontabs:
```
crontab -l
```

remove crontabs:
```
crontab -r
```