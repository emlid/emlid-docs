On this page, you will find the information on how to reflash Reach firmware.

Note that you **do not** need to do this unless you want to bring Reach to its initial state.

!!! tip ""
	Most new features are released via ReachView app and can be updated simply via its interface. More information on how to update ReachView app is available in [introduction section](../../reachview/#updating).

??? note "Firmware Flash Guide for Reach RS2 / RS+ / M+"

	### Reach RS2 / RS+ / M+ firmware download

	Get the latest ReachView image version and unzip it:

	<center>
	
	|For Reach RS2|For Reach RS+ / M+|
	|:-------------:|:-------------:|
	|[**Reach RS2 Image v2.20.6 [ZIP, 342 MB]**](http://files.emlid.com/images/reach-rs2-v2.20.6.zip), [(md5)](http://files.emlid.com/images/reach-rs2-MD5SUMS)|[**Reach RS+/M+ Image v2.18 [ZIP, 347 MB]**](http://files.emlid.com/images/reach-plus-v2.18.1.zip), [(md5)](http://files.emlid.com/images/reach-plus-MD5SUMS)|

	</center>
	

	### Reach Firmware Flash Tool download

	!!! note "" 
		In the meantime, please use **Windows** or **Linux** operating systems to flash your Reach RS2 / RS+ / M+ devices. Flash Tool for **Mac OS X** is coming soon.
	
	* Get the Reach Firmware Flash Tool:

	<center>
	
	|Windows|Linux|
	|:-------------:|:----------:|
	|[Download [EXE, 78.3 MB]](http://files.emlid.com/flash-tools/win/reach-firmware-flash-tool_1.0.2_setup.exe)|[Download [DEB, 51.9 MB]](http://files.emlid.com/flash-tools/linux/reach-firmware-flash-tool_1.0.0_amd64.deb)|

	</center>

	* Double click on the downloaded file
	
	* Follow the instructions to install Reach Firmware Flash Tool on your PC

	### Flashing process

	* Open Reach Firmware Flash Tool and choose Reach model

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step1-device-select.png" style="width: 300px;" /></p>

	<!-- delete part with RS -->

	* Select ReachView firmware .img file

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step2-image-select.png" style="width: 300px;" /></p>

	* Disconnect all Reach units. If there are none, Flash Tool will automatically skip this step
	
	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step3-disconnect-devices.png" style="width: 300px;" /></p>

	* Connect Reach device and turn it on. "Reach connected" message will appear

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step4-connected-reach.png" style="width: 300px;" /></p>

	* Wait until the end of the flashing process

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step5-flashing.png" style="width: 300px;" /></p>

	* After reflashing, Reach will reboot

	!!! danger ""
		Do not unplug the Reach on this step.

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step5-rebooting.png" style="width: 300px;" /></p>

	* When Reach successfully reboots, you'll see "Reach is flashed and ready to use" message

	<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-step5-flashed-reach.png" style="width: 300px;" /></p>

	??? danger ""Flashing failed" error troubleshooting"

		If you faced "Flashing failed" error, we recommend following the next steps:

		<p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/app-flashing-failed.png" style="width: 300px;" /></p>

		??? note "Steps for RS2 device"
			
			* Disconnect **Reach RS2** device from the PC
			
			* Hold the power button for 10 seconds until Reach turns off

			* Press *Try again* button in the Reach Firmware Flash Tool on PC

			* Now you need to enter Firmware Update Mode. To enable it on Reach RS2 press and hold the power button and then plug the USB into PC. All LEDs should blink several times simultaneously, and then start blinking one after another
			<br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/failed-rs2.gif" style="width: 400px;" /></p>


		??? note "Steps for RS+ device"
			
			* Disconnect **Reach RS+** device from the PC
			
			* Hold the power button for 10 seconds until Reach turns off

			* Press *Try again* button in the Reach Firmware Flash Tool on PC

			* Now you need to enter Firmware Update Mode. To enable it on Reach RS+ press and hold the power button and then plug the USB into PC. All LEDs should blink several times simultaneously, and then start blinking one after another 
			<br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/failed-rs-plus.gif" style="width: 400px;" /></p>
		
		
		??? note "Steps for M+ device"
			
			* Disconnect **Reach M+** device from the PC

			* Press *Try again* button in the Reach Firmware Flash Tool on PC

			* Now you need to enter Firmware Update Mode. To enable Firmware Update mode on Reach M+ use a pin to press and hold the button, located in the deepening under the power LED and then plug the USB into PC. No LEDs should blink
			<br> <p style="text-align:center" ><img src="../img/reachview/firmware-reflashing/failed-m-plus.gif" style="width: 400px;" /></p>

	### After flashing

	If the flashing has been completed successfully, you will see "Reach is flashed and ready to use" message. You may disconnect your Reach at this point.

	Proceed to Quickstart section to set up your Reach RS2, RS+ or Reach M+:

	* [Quickstart for Reach RS2](https://docs.emlid.com/reachrs2/quickstart/)
	* [Quickstart for Reach RS+](https://docs.emlid.com/reachrs/quickstart/first-setup)
	* [Quickstart for Reach M+](https://docs.emlid.com/reachm-plus/quickstart/)

??? note "Firmware Flash Guide for Reach RS / RTK"

	### Reach RS / RTK firmware download

	Get the latest ReachView image version:

	<center>
	
	|Download link|
	|:-------------:|
	|[**Reach Image v2.18 [ZIP, 234 MB]**](https://files.emlid.com/images/ReachImage_v2.18.1.zip), [(md5)](https://files.emlid.com/images/reachview-MD5SUMS)|

	</center>

	### Flashing process

	??? note "Steps for Windows"

		#### Windows

		Before flashing:

		* Install [Intel Edison driver](http://files.emlid.com/firmware-reflashing-tool/IntelEdisonDriverSetup1.2.1.exe)
		* Unzip the downloaded image
		* Download copy of [dfu-util.exe](https://files.emlid.com/images/dfu-util/dfu-util.exe) and [libusb-1.0.dll](https://files.emlid.com/images/dfu-util/libusb-1.0.dll)
		* Place these files in the same folder as the image files
		* Unplug Reach if it's plugged in

		To flash:

		1. Navigate to the image directory
		2. Run `flashall.bat`
		3. Plug Reach in
		4. Monitor progress in the terminal window
		5. Proceed to "After flashing" section below


	??? note "Steps for Mac OS X"
		
		#### Mac OS X

		Before flashing:

		* Unzip downloaded image
		* Install **[homebrew](http://brew.sh)**
		* Install dependencies with `brew install dfu-util coreutils gnu-getopt lsusb`
		* Unplug Reach if it's plugged in

		To flash:

		1. `cd` into the image directory
		2. Run `./flashall.sh`
		3. Plug Reach in
		4. Monitor progress in the terminal window
		5. Proceed to "After flashing" section below


	??? note "Steps for Linux"

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
		5. Proceed to "After flashing" section below

	## After flashing

	After the initial process is done, Reach will reboot. 
	
	!!! danger ""
		Do not unplug it until it reboots and goes through the initial setup process completely.


	Proceed to Quickstart section to set up your Reach RS / RTK:

	* [Quickstart for Reach RS](https://docs.emlid.com/reachrs/quickstart/first-setup)
	* [Quickstart for Reach RTK](https://docs.emlid.com/reach/quickstart/)
