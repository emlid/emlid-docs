## Video Streaming with Navio2

Streaming real-time video from a drone powered by a Raspberry Pi 2 has never been easier.  There is only a handful of actions that you need to make to get a drone streaming real-time video to a remote PC, tablet, phone or whatnot.

## Hardware

This instructions are for Raspberry Pi Camera Module.
Please note that Raspberry Pi Camera Module emits a lot of RF noise which may affect GPS performance. To workaround that wrap Camera Module and its cable using tape and alumnium\copper foil (use tape to keep foil from short curcuiting Camera Module pcb).

## Raspberry PI2

First things first. You need to _expand filesystem_ and _enable camera_ using Raspberry Pi configuration tool. Type the following command in console:
```bash
pi@navio: ~ $ sudo raspi-config
```  
Raspi-config menu will appear on your screen. After changing the options press the *Finish* button. Expand filesystem and enable camera options require a reboot to take effect. Raspi-config will ask if you wish to reboot now when you select the *Finish* button.

After the installation has completed you can choose whatever platform you want to stream FPV to.

## Ubuntu

If you're going to stream to a Ubuntu PC, install the some packages locally beforehand.
```bash
user@ubuntu: ~ $ sudo apt-get update
user@ubuntu: ~ $ sudo apt-get install gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-bad
```

## Android

* Download and install [QGroundControl](https://play.google.com/store/apps/details?id=org.mavlink.qgroundcontrol) for Android.

* Find IP address of your device in preferences. You'll need it in order to connect to the phone from your RPi.

* Use [our tutorial](http://docs.emlid.com/Navio-APM/installation-and-running/) to run ArduPilot using the IP you just found out.

* Run QGroundControl and it will automatically detect your vehicle.

* [Launch](#launching) video streaming on your Raspberry and the pictute will appear in left bottom corner of application screen. Tap it to run fullscreen mode.

*Note: default port for video in QGC application is 5600*

Here's the app in action
![capture](img/qgc-app-video.jpg)

## Mac OS X

The simplest way is to use brew. To install it run the following in your Mac terminal:

```bash
user@mac: ~ $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
user@mac: ~ $ brew update
user@mac: ~ $ brew install gstreamer gst-libav gst-plugins-ugly gst-plugins-base gst-plugins-bad gst-plugins-good
```

## Windows

Download and install [gstreamer for Windows](http://gstreamer.freedesktop.org/data/pkg/windows/1.4.5/gstreamer-1.0-x86_64-1.4.5.msi).

## Launching

Now everything is ready for streaming.

### On your computer

For Ubuntu/Mac OS X:
```bash
user@mac ~ $ gst-launch-1.0 -v udpsrc port=9000 caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=f
```
For Windows:

```bash
gst-launch-1.0 -v udpsrc port=9000 caps="application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264" ! rtph264depay ! avdec_h264 ! videoconvert ! autovideosink sync=f
```
From now on, your computer will be waiting for the input stream from Raspberry PI2. Once it gets a stream, you'll see the real-time video from your drone.

### On Raspberry

```bash
pi@navio: ~ raspivid -n -w 1280 -h 720 -b 1000000 -fps 15 -t 0 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=10 pt=96 ! udpsink host=<remote_ip> port=9000
```
where ```<remote_ip>``` is the IP of the device you're streaming to.

Adjust bitrate with ***-b*** switch or ***-fps*** if your video lags behind.


#### Autostarting on boot

To automatically start videostreaming on boot you need to create systemd service:
```bash
sudo touch /etc/systemd/system/raspicam.service
```
Edit the service to make it look like this:
```
[Unit]
Description=raspivid
After=network.target

[Service]
ExecStart=/bin/sh -c "/usr/bin/raspivid -n -w 1280 -h 720 -b 1000000 -fps 15 -t 0 -o - | gst-launch-1.0 -v fdsrc ! h264parse ! rtph264pay config-interval=10 pt=96 ! udpsink host=<remote_ip> port=9000"

[Install]
WantedBy=default.target
```
Don't forget to set IP of the device you're streaming to. 

After that run these commands:
- `sudo systemctl daemon-reload` - to let systemd know of this service
- `sudo systemctl enable raspicam` - to enable on boot
- `sudo systemctl start raspicam` - to test it out

From now on raspivid will start automatically on boot. To disable autostart run this command: 
```bash
sudo systemctl disable raspicam
```

Feel free to ask on our [forum](http://community.emlid.com) if you stumble upon any problems. We're always there at your convenience.  
