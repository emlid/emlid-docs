On this page, you will find the information on how to reflash Reach firmware.

Note that you **do not** need to do this unless you want to bring Reach to its initial state as all the data are erased during the reflashing procedure.

!!! tip ""
	Most new features are released via ReachView app and can be updated simply via its interface. More information on how to update ReachView app is available in [introduction section](../../reachview/#updating).

## Reach Firmware Flash Tool installation

!!! note "" 
	In the meantime, please use **Windows** or **Linux** operating systems to flash your Reach devices. Flash Tool for **Mac OS X** is coming soon.
	
* Get the Reach Firmware Flash Tool:

<center>
	
|Windows|Linux|
|:-------------:|:----------:|
|[Download [EXE, 81.9 MB]](http://files.emlid.com/flash-tools/win/reach-firmware-flash-tool_1.2.0_setup.exe)|[Download [DEB, 109.8 MB]](http://files.emlid.com/flash-tools/linux/reach-firmware-flash-tool_1.2.0_amd64.deb)|

</center>

### Window installation

* Double click on the downloaded file
	
* Follow the instructions to install Reach Firmware Flash Tool on your PC

* If you have got Reach RS / RTK devices, install the [Intel Edison Driver](http://files.emlid.com/firmware-reflashing-tool/IntelEdisonDriverSetup1.2.1.exe)

* Reboot your PC

### Linux installation

We recommend using the terminal to install the Flash Tool on your Linux PC. Follow these steps to accomplish it:

* Press `Ctrl+Alt+T` to open the terminal
* Navigate to the directory with the downloaded file with `cd ~/Downloads` command
* Run `sudo dpkg -i reach-firmware-flash-tool_1.2.0_amd64.deb` to start installation

!!! danger ""
	Please confirm adding the current user to `plugdev`, `dialout` and `lpadmin` groups during the installation process. In case of a negative answer, the application might not work as expected.

* Reboot your PC

## Firmware reflashing

??? note "Firmware Flash Guide for Reach RS2 / RS+ / M+"

	### Reach RS2 / RS+ / M+ firmware download

	Get the latest ReachView image version and unzip it:

	<center>
	
	|For Reach RS2|For Reach RS+ / M+|
	|:-------------:|:-------------:|
	|[**Reach RS2 Image v2.20.8 [ZIP, 369.7 MB]**](http://files.emlid.com/images/reach-rs2-v2.20.8.zip), [(md5)](http://files.emlid.com/images/reach-rs2-MD5SUMS)|[**Reach RS+/M+ Image v2.20.8 [ZIP, 369.8 MB]**](http://files.emlid.com/images/reach-plus-v2.20.8.zip), [(md5)](http://files.emlid.com/images/reach-plus-MD5SUMS)|

	</center>

	### Flashing process

	* Open Reach Firmware Flash Tool and choose Reach model

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step1-device-select.png" style="width: 300px;" /></p>

	* Connect Reach in Firmware Update mode

		??? note "Steps for RS2 device"
			
			* Make sure that **Reach RS2** is turned off
			
			* Press and hold the power button
			
			* Plug the USB cable into PC

			* Release the power button

			* All LEDs should blink several times simultaneously, and then start blinking one after another
			<br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/connect_fel_rs2.webp" style="width: 400px;" /></p>

		??? note "Steps for RS+ device"
			
			* Make sure that **Reach RS+** is turned off

			* Press and hold the power button
			
			* Plug the USB cable into PC

			* Release the power button

			* All LEDs should blink several times simultaneously, and then start blinking one after another 
			<br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/connect_fel_rsplus.webp" style="width: 400px;" /></p>
		
		??? note "Steps for M+ device"
			
			* Make sure that **Reach M+** is disconnected from the PC

			* Use a pin to press and hold the button located in the deepening under the power LED

			* Plug the USB into PC. No LEDs should blink

			* Release the button
			<br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/connect_fel_mplus.webp" style="width: 400px;" /></p>

	* Select ReachView firmware .img file and click on _Flash_
	
	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step3-select-firmware-rs2.png" style="width: 300px;" /></p>

	* Wait until the end of the flashing process

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step4-flashing-rs2.png" style="width: 300px;" /></p>

	* After reflashing, Reach will reboot

	!!! danger ""
		Do not unplug the Reach on this step.

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step5-rebooting-rs2.png" style="width: 300px;" /></p>

	* When Reach successfully reboots, you'll see "Reach is flashed and ready to use" message

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step5-flashed-rs2.png" style="width: 300px;" /></p>

??? note "Firmware Flash Guide for Reach RS / RTK"

	### Reach RS / RTK firmware download

	Get the latest ReachView image version:

	<center>
	
	|For Reach RS / RTK|
	|:-------------:|
	|[**Reach Image v2.20.8 [ZIP, 252.3 MB]**](http://files.emlid.com/images/ReachImage_v2.20.8.zip), [(md5)](https://files.emlid.com/images/reachview-MD5SUMS)|

	</center>

	### Flashing process

	* Open Reach Firmware Flash Tool and choose Reach model

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step1-device-select.png" style="width: 300px;" /></p>

	* Connect Reach. Follow the steps for your device

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step2-connect-rs.png" style="width: 300px;" /></p>

	??? danger ""Not suitable USB port" error" 
		If you face "USB port not suitable for flashing" error, disconnect Reach, turn it off and try another USB port.
		<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step2-choose-usb-rs.png" style="width: 300px;" /></p>


	* Select ReachView firmware .zip file and press _Flash_

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step3-select-firmware-rs.png" style="width: 300px;" /></p>

	* Wait until the end of the flashing process

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step4-flashing-rs.png" style="width: 300px;" /></p>

	* After reflashing, Reach will reboot

	!!! danger ""
		Do not unplug the Reach on this step.

	* When Reach successfully reboots, you'll see "Reach is flashed and ready to use" message

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step4-flashed-rs.png" style="width: 300px;" /></p>

## After flashing

Proceed to Quickstart section to set up your Reach device:

* [Quickstart for Reach RS2](https://docs.emlid.com/reachrs2/quickstart/)
* [Quickstart for Reach RS+](https://docs.emlid.com/reachrs/quickstart/first-setup)
* [Quickstart for Reach M+](https://docs.emlid.com/reachm-plus/quickstart/)
* [Quickstart for Reach RS](https://docs.emlid.com/reachrs/quickstart/first-setup)
* [Quickstart for Reach RTK](https://docs.emlid.com/reach/quickstart/)
