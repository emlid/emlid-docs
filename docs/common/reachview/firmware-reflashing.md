## When to reflash the firmware

On this page you will find the information on how to reflash Reach firmware.
Please note that you don't need to do this unless you want to bring Reach to its initial state or new firmware image version is released. If your Reach has ReachView version 0.4.9 it is necessary to reflash it with new firmware image in order to receive updates and support.

Most new features are released via ReachView app updates that can be updated simply by pressing an "Update" button in its interface.
!!! note ""
    More information on how to update ReachView app is available in [introduction section](/common/reachview/#updating).

### Emlid Reach RTK firmware download

You can get the latest version here:

[**Reach Image v2.9  ↓**](https://files.emlid.com/images/ReachImage_v2.9.zip), [(md5)](https://files.emlid.com/images/reachview-MD5SUMS)

There are two ways to flash the image. Intel's Edison Board Configuration Tool and a CLI script.

## Flashing process

### GUI guide

!!! danger "Temporary GUI workaround"
    Currently Intel is having troubles​ with their download server and there may be issues installing the driver via Intel Edison Board Configuration Tool.<br> <br>**GUI Tool for Mac and Linux are currently unavailable, please use Terminal guide** <br><br>**For Windows: please [follow the simple workaround](http://files.emlid.com/firmware-reflashing-tool/IntelGUIWindowsWorkaround.pdf) to install the tool**

#### Getting Intel Edison Board Configuration Tool

You can get the tool from the table below. It is available for Windows, Mac and Linux.

| Windows | Mac | Linux |
|---------|-----|-------|
| [Download](https://files.emlid.com/firmware-reflashing-tool/intel_edison_setup_win_v2016.2.007.zip) | [Download](https://files.emlid.com/firmware-reflashing-tool/intel_edison_setup_mac_v2016.2.013.tar.gz) | [Download](https://files.emlid.com/firmware-reflashing-tool/intel_edison_setup_lin_2016.2.002.tar.gz) |

#### Flashing Reach and Reach RS


- Disconnect Reach / Reach RS from your computer. Reach RS must be turned off
- Run Intel Edison Board Configuration Tool. Hit **Next**

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/welcome.png" style="width: 800px;" /></p>

- Read License Agreement, accept the terms of the License and hit **Next** twice

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/license.png" style="width: 800px;" /></p>


- Install drivers (**Only for Windows**) 

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/setupopt.png" style="width: 800px;" /></p>


- After installation hit **Flash Firmware**

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/setup_with_drivers.png" style="width: 800px;" /></p>

- Choose second item: "**Use existing image, located at:**"
- Choose correct path to the image (You will need to point it to a **.json** file for Windows and **.hddimg** for Linux)  
- Hit **Next** 

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/choose_img.png" style="width: 800px;" /></p>

- Plug Reach / Reach RS to this computer when you reach "Connect USB and power cables" step. In case you are reflashing Reach RS hold the power button for 5 seconds after plugging in the cable

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/Intel-tool-reachrs.png" style="width: 800px;" /></p> 

- Proceed to "After flashing"


### Terminal guide

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
2. Run `sudo ./flashall.sh`
3. Plug Reach in
4. Monitor progress in the terminal window
5. Proceed to "After flashing"

#### Linux

Before flashing:

* Unzip downloaded image
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


