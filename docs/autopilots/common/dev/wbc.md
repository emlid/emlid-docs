## Wi-Fi broadcast

Emlid Raspbian images comes with pre-installed WBC.

!!! danger
    It's an experimental feature. Please test it on ground before lifting off.

### What is Wi-Fi broadcast?

Wifibroadcast is a project aimed at the live transmission of HD video (and other) data using wifi radios.
One prominent use case is to transmit camera images for a first person view (FPV) of remote controlled aircrafts.
In contrast to a normal wifi connection wifibroadcast tries to mimic the advantageous properties of an analog
link (like graceful signal degradation, unidirectional data flow).

Wifibroadcast puts the wifi cards into monitor mode. This mode allows to send and receive arbitrary packets
without association between devices. Additionally, it is also possible to receive erroneous frames (where the checksum does not
match).

### Overview


Transmitter hardware configuration:

* Raspberry Pi
* Wi-Fi card *compatible with wifibroadcast*
* Camera

Receiver hardware configuration:

* Raspberry Pi
* Wi-Fi card *compatible with wifibroadcast*
* Display

### Wi-Fi cards

Not all wifi cards are compatible with wifibroadcast. This is because wifibroadcast uses injection mode which
not fully supported by many wifi chipsets.

#### 2.4GHz

!!! warning
    2.4Ghz is used by RC and hence should be used with caution. Please, verify that your RC transmitter doesn't interfere with Wi-Fi broadcast-enabled dongles. Consider using 5Ghz dongles to eliminate risks altogether.

Recommended dongles:

* TP-LINK TL-WN722N V1
* Alfa AWUS036NHA

You can find a list of wifi cards using this chip [here](https://wikidevi.com/wiki/Atheros_AR9271).

#### 5GHz

For 5GHz operation Ralink RT5572 based devices are recommended since they work out of the box.
Recommended dongles:

* CSL-300:
* ALFA AWUS051NH **v2**
* TP-LINK TL-WDN3200


For more cards refer to [here](https://wikidevi.com/wiki/Ralink_RT5572).

### Powering

**Transmitter**

Navio should be powered by a power module connected to the “POWER” port on Navio. Navio will provide
power to the Raspberry Pi.

**Receiver**

Connect 5V 1A power adapter to the Raspberry Pi’s microUSB port. Please do not power it
from laptop USB port.

## How to get your hands on: step by step

### Configuration 

Wi-Fi broadcast settings are stored in  ```/etc/default/wbc```.

```bash
pi@navio:~$ cat /etc/default/wbc
#!/bin/bash


# Camera image settings
WIDTH=1280
HEIGHT=720
FPS=48
BITRATE=4000000
KEYFRAMERATE=48



# Transmission and recording settings
CHANNEL2G="13"
CHANNEL5G="13"
NICS=`ls /sys/class/net | grep wlan`
SAVE_PATH="/media/usb0/video"




##################################
#change these only if you know what you are doing (and remember to change them on both sides)
BLOCK_SIZE=8
FECS=4
PACKET_LENGTH=1024
PORT=0
##################################
```

Make changes in this file if you need to adjust broadcast seettings.

### Receiver setup

To start broadcast on receiver:
```bash
sudo systemctl start wbcrxd
```

### Transmitter setup

To start broadcast on transmitter:
```bash
sudo systemctl start wbctxd
```
