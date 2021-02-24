#How to download files from Reach

This guide overviews how to download system report, export survey project or save logs from Reach on your PC, laptop, tablet or smartphone.

!!! note ""
	You need to connect to ReachView 3 over Wi-Fi to download files. Files cannot be transferred over USB.

##Turning Reach on

Press Reach power button and wait until it boots. 

??? note "Reach M+/M2 workflow"

	When the red LED and green LED stay solid, check the blue LED status.

	* **Blue LED is solid.** Reach is in [hotspot mode](#reach-is-in-hotspot-mode) and you can connect your laptop or phone to it. 
	* **Blue LED blinks slowly.** Reach is in [client mode](#reach-is-in-client-mode) and connected to the Wi-Fi network.
	<br>	

	|Hotspot mode|Client mode|
	|:----------:|:---------:|
	|<img src="../img/quickstart/downloading-files/running-hotspot-mplus.gif" style="height: 100px;">|<img src="../img/quickstart/downloading-files/running-client-mplus.gif" style="height: 100px;">|

??? note "Reach RS/RS+ workflow"

	When the red LED and green LED stay solid, check the blue LED status.

	* **Blue LED is solid.** Reach is in [hotspot mode](#reach-is-in-hotspot-mode) and you can connect your laptop or phone to it.
	* **Blue LED blinks slowly.** Reach is in [client mode](#reach-is-in-client-mode) and connected to the Wi-Fi network.
	<br>	

	|Hotspot mode|Client mode|
	|:----------:|:---------:|
	|<img src="../img/quickstart/downloading-files/running-hotspot.png" style="height: 200px;">|<img src="../img/quickstart/downloading-files/running-client.gif" style="height: 200px;">|

??? note "Reach RS2 workflow"

	When the Power LEDs and Power button stay solid, check the Network LED status.

	* **Network LED is solid white.** Reach is in [hotspot mode](#reach-is-in-hotspot-mode) and you can connect your laptop ot phone to it.
	* **Network LED is solid blue.** Reach is in [client mode](#reach-is-in-hotspot-mode) and connected to the Wi-Fi network.
	<br>

	|Hotspot mode|Client mode|
	|:----------:|:---------:|
	|<img src="../img/quickstart/downloading-files/hotspot.png" style="height: 200px;">|<img src="../img/quickstart/downloading-files/client-mode.png" style="height: 200px;">|

##Connecting to ReachView 3

### Reach is in hotspot mode

??? note "Connecting via the Reachview 3 app (iOS/Android device)"

	1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.emlid.reachview3) or [Apple Store](https://apps.apple.com/us/app/reachview-3/id1463967138)
	2. Go to *Wi-Fi settings* on your device
	3. Connect to Reach hotspot. It appears as **reach:XX:XX**
	4. Enter password **emlidreach**
	5. Launch ReachView 3
	6. Choose Reach from the list


??? note "Connecting via a web browser (any device)"

	1. Go to *Wi-Fi settings* on your device
	2. Connect to Reach hotspot. It appears as **reach:XX:XX**
	3. Enter password **emlidreach**

		!!! tip "Windows OS"
			If Windows suggests you to enter the PIN from the router label to connect to the network, choose *Connect using a security key instead* option.

	4. Launch a web browser (we recommend using Chrome or Mozilla)
	5. Go to 192.168.42.1


### Reach is in client mode

??? note "Connecting via the Reachview 3 app (iOS/Android device)"

	1. Connect your mobile device to the same Wi-Fi network as Reach
	2. Scan for available Reach devices
	3. Choose Reach from the list
	
	<div style="text-align: center;"><img src="../img/quickstart/downloading-files/Reach-list.PNG" style="height: 550px;"></div>


??? note "Connecting via web-browser (any device)"

	1. Connect your device to the same Wi-Fi network as Reach
	2. Use ReachView 3 to determine the Reach IP address
	3. Launch a web browser (we recommend using Chrome or Mozilla)
	4. Go to the determined Reach IP


## Downloading files

### System Reports

<div style="text-align: center;"><img src="../img/quickstart/downloading-files/system-report.PNG" style="height: 550px;"></div>

System reports carry important for issue resolving information about Reach settings and state. There are two types of system reports:

* **Simple report** provides ReachView 3 version, configurations, and network information
* **Full report** includes a more technical device description with system logs

!!! attention ""
	We do not recommend to post Full report publicly as it contains **sensitive information** such as Wi-Fi and NTRIP credentials and location.

To download the system report you just need to open the *Settings* tab in ReachView 3 and go to *General settings*.

### Logs

<div style="text-align: center;"><img src="../img/quickstart/downloading-files/logging.PNG" style="height: 550px;"></div>

You can download logs as well as start or stop logs recording in the *Logging* tab in ReachView 3.

### Survey projects

<div style="text-align: center;"><img src="../img/quickstart/downloading-files/survey.PNG" style="height: 550px;"></div>

Survey projects contain points you saved during the RTK survey. You can find them in the *Survey* tab in ReachView 3.

The video below covers the process of exporting data from ReachView 3.

<div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/-X31SxMTd-o" allowfullscreen></iframe></div>

##Where to find downloaded data

Downloading completes successfully. To get the file, go to the folder where your device saves all the downloaded data.

###Laptop or PC workaround

Files from Reach are usually saved to the default **Downloads** folder.

###Smartphone or tablet workaround

* **iOS**: After “Download complete” message appears, you can choose the folder to save file or share it using AirDrop or another app.

<div style="text-align: center;"><img src="../img/quickstart/downloading-files/download-iphone.png" style="height: 550px;"></div>

* **Android**: “Download complete!” message means the file was saved successfully. It’s more likely you will find this file in `My Files/Downloads` or in `My Files/Internal Storage/Download` folders.

<div style="text-align: center;"><img src="../img/quickstart/downloading-files/download-Android.jpg" style="width: 800px;"></div>
