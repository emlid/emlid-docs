On this page, you will find the information on how to reflash Reach firmware.

Note that you **do not** need to do this unless you want to bring Reach to its initial state as all the data are erased during the reflashing procedure.

!!! tip ""
	Most new features are released via Reach Panel app and can be updated simply via its interface. More information on how to update Reach Panel app is available in [introduction section](../../reachview/#updating).

## Reach Firmware Flash Tool installation
	
* Get the Reach Firmware Flash Tool:

<center>
	
|Windows|Ubuntu|macOS|
|:-------------:|:----------:|:-----------:|
|[Download [EXE, 81.9 MB]](https://files.emlid.com/flash-tools/win/reach-firmware-flash-tool_1.4.1_setup.exe)|[Download [DEB, 104.0 MB]](https://files.emlid.com/flash-tools/linux/reach-firmware-flash-tool_1.4.1_amd64.deb)| [Download [DMG, 56.0 MB]](https://files.emlid.com/flash-tools/macos/Reach%20Firmware%20Flash%20Tool%201.4.1.dmg)|

</center>

### Windows installation

* Double click on the downloaded file
	
* Follow the instructions to install Reach Firmware Flash Tool on your PC

* Reboot your PC

### Ubuntu installation

We recommend using the terminal to install the Flash Tool on your PC. Follow these steps to accomplish it:

* Press `Ctrl+Alt+T` to open the terminal
* Navigate to the directory with the downloaded file with `cd ~/Downloads` command
* Run `sudo dpkg -i reach-firmware-flash-tool_1.3.0_amd64.deb` to start installation

!!! danger ""
	Please confirm adding the current user to `plugdev` and `dialout` groups during the installation process. In case of a negative answer, the application might not work as expected.

* Reboot your PC

### macOS installation

* Double click on the downloaded file
* Follow the instructions to install Reach Firmware Flash Tool on your Mac
* Drag the application icon to the Applications folder

## Firmware Flash Guide

Reach Firmware Flash Tool will ask you to download the latest Reach Panel image version. You can also get it here:





<center>
	
|For Reach RS+|For Reach RS|
|:-------------:|:----------:|
|[**Reach RS+ Firmware 26 [ZIP, 370 MB]**](http://files.emlid.com/images/reach-plus-v26.0.zip), [(md5)](http://files.emlid.com/images/reach-plus-MD5SUMS)|[**Reach RS Firmware 26 [ZIP, 185 MB]**](http://files.emlid.com/images/reach-rs-v26.0.zip), [(md5)](http://files.emlid.com/images/reachview-MD5SUMS)|

</center>








### Flashing process

* Open Reach Firmware Flash Tool and choose Reach RS/RS+

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/common/app-step1-device-select.png" style="width: 300px;" /></p>







* Connect Reach RS/RS+

??? note "Connect Reach RS+ in Firmware Update mode"
			
	* Make sure that **Reach RS+** is turned off

	* Press and hold the power button
			
	* Plug the USB cable into PC

	* Release the power button

	* All LEDs should blink several times simultaneously, and then start blinking one after another 
	<br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/reachrs/connect_fel.webp" style="width: 400px;" /></p>

??? note "Connect Reach RS"

	* Connect Reach RS

	* Follow the instructions
	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/reachrs/app-step2-connect.png" style="width: 300px;" /></p>

	??? danger " "Not suitable USB port" error"
		If you face "USB port not suitable for flashing" error, disconnect Reach, turn it off and try another USB port.
		<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/common/app-step2-choose-usb-rs.png" style="width: 300px;" /></p>





* Download the proposed Reach Panel firmware .zip file. You can also select image file from your disk. If the image version is outdated, the Flasher tool will show you a warning message. Click on _Flash_

!!! note ""
	You can either unpack the image yourself and select a .img file or just select a .zip file. In the latter case, the Flasher will unzip it.
	
<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/reachrs/app-step3-select-firmware.png" style="width: 300px;" /></p>

!!! note ""
	Reach Firmware Flash Tool creates 2 folders: one to download the image and another one to unpack it. Once you close the Flasher tool, the folder with the unpacked image will be deleted.

	??? note "Folder Paths for Windows"
		Downloads folder: `C:\Users\<username>\Downloads\Reach Firmware Flash Tool`  
		Unpacking folder: `C:\Users\<username>\AppData\Local\Temp\Reach Firmware Flash Tool`

	??? note "Folder Paths for Linux"
		Downloads folder: `/home/<username>/Downloads/Reach Firmware Flash Tool`  
		Unpacking folder: `/tmp/Reach Firmware Flash Tool`

* Wait until the end of the flashing process

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/reachrs/app-step4-flashing.png" style="width: 300px;" /></p>



* After reflashing, Reach RS/RS+ will reboot

!!! danger ""
    Do not unplug the Reach RS/RS+ on this step.

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/reachrs/app-step5-rebooting.png" style="width: 300px;" /></p>



* When Reach RS/RS+ successfully reboots, you will see "Reach is flashed and ready to use" message

<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/reachrs/app-step5-flashed.png" style="width: 300px;" /></p>

## After flashing

Proceed to [the First setup guide](../../quickstart/first-setup) to set up your Reach RS/RS+ device.
