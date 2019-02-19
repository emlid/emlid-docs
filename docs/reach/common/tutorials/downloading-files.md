#How to download files from Reach

This guide overviews how to download system report, export survey project or save logs from Reach on your PC, laptop, tablet or smartphone.

!!! note ""
	You need to connect to ReachView over Wi-Fi to download files. Files can’t be transferred over USB.

##Turning Reach on

Press Reach power button and wait until it boots. When the red LED and green LED stay solid, check the blue LED status.

* **Blue LED is solid.** Reach is in hotspot mode and you can connect your laptop or phone to it. [Click this link to continue following the guide.](#reach-is-in-hotspot-mode)
* **Blue LED blinks slowly.** Reach is in client mode and connected to the Wi-Fi network. [Proceed to this part of the guide to continue.](#reach-is-in-client-mode)
<br>

|Hotspot mode|Client mode|
|:----------:|:---------:|
|<img src="../img/reach/downloading-files/running-hotspot.png" style="height: 200px;">|<img src="../img/reach/downloading-files/running-client.gif" style="height: 200px;">|

##Connecting to ReachView

### Reach is in hotspot mode

<details close><summary>**Connecting via Reachview app (iOS/Android device)**</summary>

1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [Apple Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
2. Go to Wi-Fi settings on your device
3. Connect to Reach hotspot. It appears as **reach:XX:XX**
4. Enter password **emlidreach**
5. Launch ReachView app
6. Choose Reach from the list

</details>

<details close><summary>**Connecting via a web browser (any device)**</summary>

1. Go to Wi-Fi settings on your device
2. Connect to Reach hotspot. It appears as **reach:XX:XX**
3. Enter password **emlidreach**

	!!! note "Windows OS"
		If Windows suggests you to enter the PIN from the router label to connect to the network, choose **Connect using a security key instead** option.

4. Launch a web browser (we recommend using Chrome or Mozilla)
5. Go to 192.168.42.1

</details>

### Reach is in client mode

<details close><summary>**Connecting via Reachview app (iOS/Android device)**</summary>

1. Connect your mobile device to the same Wi-Fi network as Reach
2. Scan for available Reach devices
3. Choose Reach from the list
<div style="text-align: center;"><img src="../img/reach/downloading-files/Reach-list.PNG" style="width: 800px;"></div>

</details>

<details close><summary>**Connecting via web-browser (any device)**</summary>

1. Connect your device to the same Wi-Fi network as Reach
2. Use one of the [Network Scan utility](https://docs.emlid.com/reachrs/quickstart/#accessing-reach-rsrs-device-in-a-network) or ReachView app to determine the Reach IP address
3. Launch a web browser (we recommend using Chrome or Mozilla)
4. Go to determined Reach IP

</details>

## Downloading files

### System Reports

<div style="text-align: center;"><img src="../img/reach/downloading-files/system-report.PNG" style="width: 800px;"></div>

System reports carry important for issue resolving information about Reach settings and state. There are two types of system reports:

* **Simple report** provides ReachView version, configurations, and network information
* **Full report** includes a more technical device description with system logs

!!! attention ""
	We do not recommend to post Full report publicly as it contains **sensitive information** such as Wi-Fi and NTRIP credentials and location.

To download the system report you just need [to open ReachView Settings tab and follow the instructions from here.](/common/reachview/settings/#system-report)

### Logs

<div style="text-align: center;"><img src="../img/reach/downloading-files/logging.PNG" style="width: 800px;"></div>

You can download logs as well as start or stop logs recording in ReachView “Logging” tab. [Check the Logging section in our docs to download it and learn more about log formats.](/common/reachview/logging/#downloading)

### Survey projects

<div style="text-align: center;"><img src="../img/reach/downloading-files/survey.PNG" style="width: 800px;"></div>

Survey projects contain points you saved during RTK survey. You can find them in ReachView Survey tab. [Proceed to the corresponding article to figure out how you can export them and which formats are available.](/common/reachview/survey/#exporting-data) 

##Where to find downloaded data

Downloading completes successfully. To get the file, go to the folder where your device saves all the downloaded data.

###Laptop or PC workaround

Files from Reach are usually saved to the default **Downloads** folder.

###Smartphone or tablet workaround

* **iOS**: After “Download complete” message appears, you can choose the folder to save file or share it using AirDrop or another app.

<div style="text-align: center;"><img src="../img/reach/downloading-files/download-iPad.PNG" style="width: 800px;"></div>

* **Android**: “Download complete!” message means the file was saved successfully. It’s more likely you will find this file in `My Files/Downloads` or in `My Files/Internal Storage/Download` folders.

<div style="text-align: center;"><img src="../img/reach/downloading-files/download-Android.jpg" style="width: 800px;"></div>