# Raspberry Pi - Camera

enable interface
```
sudo raspi-config
*interfacing options
*p1 camera
*enable
```

take picture
```
raspistill -o image.jpg
```
take 10000ms video
```
raspivid -o video.h264 -t 10000
```