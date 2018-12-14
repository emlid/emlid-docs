## When to reflash the firmware

On this page you will find the information on how to reflash Reach firmware.
Note that you don't need to do this unless you want to bring Reach to its initial state or new firmware image version is released. If your Reach has ReachView version 0.4.9 it is necessary to reflash it with new firmware image in order to receive updates and support.

Most new features are released via ReachView app updates that can be updated simply by pressing an "Update" button in its interface. More information on how to update ReachView app is available in [introduction section](/common/reachview/#updating).

<details close>
<summary>**Firmware Flash Guide for Reach and Reach RS**</summary>

## Emlid Reach RTK firmware download

Get the latest version:

[**Reach Image v2.16  ↓**](https://files.emlid.com/images/ReachImage_v2.16.0.zip), [(md5)](https://files.emlid.com/images/reachview-MD5SUMS)


## Flashing process

#### Windows

Before flashing:

* Install [Intel Edison driver](http://files.emlid.com/firmware-reflashing-tool/IntelEdisonDriverSetup1.2.1.exe)
* Unzip downloaded image
* Download copy of [dfu-util.exe](https://files.emlid.com/images/dfu-util/dfu-util.exe) and [libusb-1.0.dll](https://files.emlid.com/images/dfu-util/libusb-1.0.dll)
* Place these files in the same folder as the image files
* Unplug Reach if it's plugged in

To flash:

1. Navigate to the image directory
2. Run `flashall.bat`
3. Plug Reach in
4. Monitor progress in the terminal window
5. Proceed to "After flashing"

#### Mac OS X

Before flashing:

* Unzip downloaded image
* Install **[homebrew](http://brew.sh)**
* Install dependencies with `brew install dfu-util coreutils gnu-getopt`
* Unplug Reach if it's plugged in

To flash:

1. `cd` into the image directory
2. Run `./flashall.sh`
3. Plug Reach in
4. Monitor progress in the terminal window
5. Proceed to "After flashing"

#### Linux

Before flashing:

* Unzip downloaded image
* Install dfu-util with `sudo apt-get install dfu-util`
* Unplug Reach if it's plugged in

To flash:

1. `cd` into the image directory
2. Run `sudo ./flashall.sh`
3. Plug Reach in
4. Monitor progress in the terminal window
5. Proceed to "After flashing"

## After flashing

After the initial process is done, Reach will reboot. **Do not unplug it until it reboots and goes through the initial setup process completely**.


Proceed to Quickstart section to set up your Reach / Reach RS:

* [Quickstart for Reach](https://docs.emlid.com/reach/quickstart/)
* [Quickstart for Reach RS](https://docs.emlid.com/reachrs/quickstart/)

</details>

<details close>

<summary>**Firmware Flash Guide for Reach M+ and Reach RS+**</summary>

## Emlid Reach M+ and Reach RS+ firmware download

Get the latest version:

[**Reach Plus Image v2.16  ↓**](http://files.emlid.com/images/reach-plus-v2.16.0.zip), [(md5)](http://files.emlid.com/images/reach-plus-MD5SUMS)

## Flashing process

!!! note "" 
	In the meantime, please use Windows operating system to flash your Reach M+ or Reach RS+ device. Flash tool for Mac OS X and Linux are coming soon.

Get Firmware Flash tool for Windows: [Reach Firmware Flash Tool](https://files.emlid.com/rs-plus-flasher/Reach%20Firmware%20Flash%20Tool.zip).

#### Flashing Reach M+ and Reach RS+

Before the first launch of Flash tool you need to install USB driver using Zadig tool. You can find Zadig.exe file in Firmware Flash tool zip-folder. Reach should be connected in Firmware Update mode.

##### Entering Firmware Update Mode

To enable Firmware Update mode on **Reach RS+** press and hold the power button and then plug the USB into PC. All three LEDs should blink several times simultaneously, and then start blinking one after another. <br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/flashing-mode.gif" style="width: 400px;" /></p>

To enable Firmware Update mode on **Reach M+** use a pin to press and hold the button, located in the deepening under the power LED and then plug the USB into PC. No LEDs should blink. <br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/flashing-mode-m.gif" style="width: 400px;" /></p>

After connecting Reach in Firmware Update mode run Zadig.exe and wait for '1 device found' message in the bottom left corner. 

!!! tip ""
	You have to install the driver with Zadig on your PC just once. During the next firmware update, you can skip this step.

Then press '**install driver**' button.

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/zadig-tool.PNG"/></p>

!!! note ""
	Tick the "Edit" checkbox on the right hand side and enter any USB device name you like. Later it will help to distinguish your device from other USB entries in the Device Manager.


To flash:

* Unzip downloaded image and Firmware Flash tool to **C:\Emlid**
* Run **Reach Firmware Flash Tool.exe** as an administrator
* Connect Reach in Firmware Update mode to PC and wait until eMMC is initialized
* In the "**Image File**" field select Reach image
* Check disk letter in "**Device**" field to ensure you are flashing Reach, not another device

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/reachplus-flasher.PNG"/></p>

* Hit **Start**. It will initiate flash process
* Proceed to "After flashing"

## After flashing

If flashing has been completed successfully you will see 'Device is rebooting...' message. You may disconnect your Reach M+ or RS+ at this point.

The LEDs are off while device is rebooting. They will glow up approximately in 1 minute.

Proceed to Quickstart section to set up your Reach M+ or Reach RS+:

* [Quickstart for Reach M+](https://docs.emlid.com/reachm-plus/quickstart/)
* [Quickstart for Reach RS+](https://docs.emlid.com/reachrs/quickstart/)

</details>


