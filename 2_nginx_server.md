# Raspberry Pi - nginx webserver

install
```
sudo apt-get install nginx
```

start/stop server:
```
sudo /etc/init.d/nginx start
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx restart
```

testing
```
sudo nginx -t
```

configuration files directory
```
/etc/nginx/
```

configuration files are:
```
/etc/nginx/nginx.conf
/etc/nginx/conf.d/*.conf
/etc/nginx/sites-enabled/*
[#example configuration: /etc/nginx/sites-available/default]
```

website files are located at:
```
/var/www/html/index.html
```

error log:
```
/var/log/nginx/access.log
/var/log/nginx/error.log
```

disable log inside nginx.conf:
```
access_log  /dev/null;
error_log /dev/null;
```

### use user: www-data

change /var/www/ permissions to incorparate user: www-data
```
sudo chown -R root:www-data /var/www/
```
nginx use user: www-data by editing:
```
sudo nano /etc/nginx/sites-enabled/default
```
and adding:
```
user www-data;
```


### add php to nginx

install
```
sudo apt-get install php-fpm
```

edit:
```
sudo nano /etc/nginx/sites-enabled/default
```
by chan changing line to:
```
index index.php index.html index.htm
```
and set comments as follows:
```
	# pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
	location ~ \.php$ {
		include snippets/fastcgi-php.conf;
    	#With php-fpm (or other unix sockets):
		fastcgi_pass unix:/var/run/php/php7.0-fpm.sock;
	#	# With php-cgi (or other tcp sockets):
	#	fastcgi_pass 127.0.0.1:9000;
		}
```

testing:
rename file to index.php
```
sudo mv /var/www/html/index.nginx-debian.html /var/www/html/index.php
```
add following line inside
```
<?php echo phpinfo(); ?>
```
restart server:
```
sudo /etc/init.d/nginx reload
```
now some information about the php setup should be displayed on your index.php web page


### add domain
make directory for files:
```
sudo mkdir /var/www/mysite.net
```
add configuration file:
```
sudo nano /etc/nginx/sites-enabled/mysite.net.conf
```
with content:
```
server {
	listen 80;
	listen [::]:80;
	root /var/www/mysite.net;
	server_name mysite.net;
	index index.php index.html index.htm;
	location / {
		try_files $uri $uri/ =404;
	}
}
```
create content
```
sudo nano /var/www/mysite.net/index.php
```

### set up ssl
```
sudo apt-get install certbot
```
generate certificate (90day valid):
```
sudo certbot certonly --webroot -w /var/www/html -d mysite.net
```
certificates saved at: /etc/letsencrypt/live/mysite.net/fullchain.pem \
edit nginx config file for ssl
```
sudo nano /etc/nginx/sites-enabled/default
```
by adding:
```
#listen for https
listen 443 ssl;
listen [::]:443 ssl;

#ssl
ssl_certificate /etc/letsencrypt/live/mysite.net/fullchain.pem;
ssl_certificate_key your-/etc/letsencrypt/live/mysite.net/privkey.pem;
ssl_session_timeout 5m;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_ciphers ALL:!ADH:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv3:+EXP;
ssl_prefer_server_ciphers on;
```
