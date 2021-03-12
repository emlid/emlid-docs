## Downloading configured Raspbian image

Navio requires a preconfigured Raspbian to run. We provide a unified SD card image for Raspberry Pi 2, 3 and 4. The OS is headless, i.e. it comes without GUI as it is not required for drone applications.

[Download SD card image with the latest Raspbian release (Buster)](https://files.emlid.com/images/emlid-raspbian-20200922.img.xz), [(md5)](https://files.emlid.com/images/MD5SUMS)

## Writing image to SD card

* Get the latest Emlid Raspbian Image.
* Download, extract and run [Etcher](https://etcher.io/) with administrator rights.
* Select the archive file with image and sd card drive letter.
* Click “Flash!”. The process may take a few minutes.

<iframe  title="Emlid manuals" width="680" height="380" src="https://www.youtube.com/embed/i8_TFYWYt_M" allowfullscreen></iframe>

More detailed instructions are available [here](http://www.raspberrypi.org/documentation/installation/installing-images/).

## Configuring Wi-Fi access

Raspberry Pi 3 and 4 have an internal Wi-Fi module, while Raspberry Pi 2 requires an external USB Wi-Fi dongle. An extensive list of supported dongles is available [here](http://elinux.org/RPi_USB_Wi-Fi_Adapters).

Wi-Fi networks can be configured by editing the wpa_supplicant.conf file located on SD card (/boot partition). To add your network simply add the following lines to it:

```bash
network={
  ssid="yourssid"
  psk="yourpasskey"
  key_mgmt=WPA-PSK
}
```

To get access to this file use one of the following methods:

### Edit configuration on SD card

Simply plug an SD card in your computer. After getting access to SD card contents, open wpa_supplicant.conf located on /boot partition (with root privileges on Linux) and edit the file as described above.

### Use monitor and keyboard

Connect HDMI monitor and USB keyboard to your Raspberry, power it up and you will get access to the console, where you can use text editor to modify wpa_supplicant.

!!! note ""
	Use the default username `pi` and the default password `raspberry` to get access to your RPi.

After logging into the system, type:

```bash
sudo nano /boot/wpa_supplicant.conf
```

Modify the file as described above, save it and reboot.
This method may be problematic because some keyboards are not compatible with this kernel. If your keyboard does not work, try another one or use another method.

### Use Ethernet

You can connect to Raspberry Pi over Ethernet by plugging it using Ethernet cable to a switch, router or directly to your computer.

### Trying to connect using Zeroconf

There's a pretty good chance you'll be able to ssh into your Raspberry Pi using Zeroconf.

You can try either ```ssh pi@navio.local``` on Mac or Linux or type navio.local in Putty on Windows.

If that doesn't work out for you, read a section below.

### Finding an IP address

To find an IP address of your Raspberry Pi use nmap utility.

It can be run from the console on your desktop:
nmap -sn 192.168.1.*

You can use it with a GUI such as Zenmap or Fing application on your phone.

Look for the hostname ”navio”.

### wpa_passphrase on Linux

If you edit the file on a Raspberry or on a Linux computer you can populate **wpa_supplicant.conf** with a utility called **wpa_passphrase** like this:

```sudo bash -c "wpa_passphrase SSID password" >> /boot/wpa_supplicant.conf```

## Upgrading

If required you can now upgrade your system by running:

```sudo apt-get update && sudo apt-get dist-upgrade```

## Expanding rootfs

!!! note ""
	Emlid Raspbian Buster makes auto-expanding on a first boot.

By default when Emlid Raspbian for the Rapsberry Pi is installed the file system
will only expand to occupy 3GB of storage. If you don’t have space left on yor device,
you should expand your file system. To do so, just type

```sudo raspi-config --expand-rootfs```

and reboot.
