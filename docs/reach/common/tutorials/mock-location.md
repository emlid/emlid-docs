#Getting Reach coordinates on Android via BT

!!! danger ""
	iOS devices don't support getting a location over Bluetooth from third-party hardware.

##Overview

This guide demonstrates how to get precise coordinates from Reach on an Android device over Bluetooth.

!!! tip "Commonly used GIS apps for Android used with Reach:"
	* Mobile Topographer Pro
	* ESRI ArcGIS Collector
	* Mapit GIS
	* LandStar
	* Autocad360


## Video Demonstration

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/yy8EVSMq9Bk" frameborder="0" allowfullscreen></iframe></div>

<div style="text-align: center;">Video by <a href="https://community.emlid.com/users/tb_rtk/activity">TB_RTK</a></div>

## Before you start

Make sure your Android device provides Bluetooth connectivity.

!!! tip ""
	To output a centimeter accurate position, Reach should be in RTK mode. Refer to the article [How RTK works](rtk-introduction.md) to learn more.

Configure Reach RS+ unit to act as a rover in RTK:

??? note "Getting corrections from Reach RS+ base"
	Set up RTK communication between 2 Reach RS+ units over LoRa radio [following this video guide](https://youtu.be/4GfUDoDwEAE) 

??? note "Getting corrections from NTRIP/CORS"
	Configure [NTRIP/CORS network as a source of positioning corrections](ntrip-workflow.md) for Reach rover.

##Pairing Reach RS+ with an Android device

**Access Reach RS+ rover using ReachView**

??? note "Connecting to Reach with iOS/Android device"

	1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [Apple Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
	2. Go to Wi-Fi settings on your device
	3. Connect to Reach hotspot. It appears as **reach:XX:XX**
	4. Enter password **emlidreach**
	5. Launch ReachView app
	6. Choose Reach from the list

??? note "Connecting via a web browser from any device"

	1. Go to Wi-Fi settings on your device
	2. Connect to Reach hotspot. It appears as **reach:XX:XX**
	3. Enter password **emlidreach**
	4. Launch a web browser (we recommend using Chrome or Mozilla)
	5. Go to 192.168.42.1

* Open **Bluetooth** configuration screen, enable Bluetooth connection and set on the **Always discoverable** option

<p style="text-align:center"><img src="../img/reach/mock-location/enable-bt.png" style="width: 800px;"/></p>

!!! note ""
	Reach RS+ name being displayed just above its MAC. In this guide, we used the unit named as **Reach**

**Access an Android device**

* Navigate to the Bluetooth configuration screen. Activate the Bluetooth connection

* Wait for Reach RS+ to be listed as an available device

!!! tip ""
	Keep Reach RS+ within a few meters from your Android device

<p style="text-align:center"><img src="../img/reach/mock-location/bt-scanning.jpg" style="width: 800px;"/></p>

**Back to the ReachView app**

* You should now be able to see your Android device listed as an available device. In this guide, we used a device named as **Galaxy Tab A (2017)**

<p style="text-align:center"><img src="../img/reach/mock-location/discoverable-devices.png" style="width: 800px;"/></p>

* Tap the name of the Android device in ReachView

**Back to the Android device**

* You should receive a pairing request from Reach RS+. Confirm it

<p style="text-align:center"><img src="../img/reach/mock-location/pairing-request.jpg" style="width: 800px;"/></p>

<br>

Reach RS+ and Android device are now paired:

<p style="text-align:center"><img src="../img/reach/mock-location/android-paired.jpg" style="width: 800px;"/></p>

<p style="text-align:center"><img src="../img/reach/mock-location/reachview-paired.png" style="width: 800px;"/></p>

## Position output from Reach to Android

* Using the ReachView app, navigate to the **Position output** screen

* Activate **Output 1**, set it to **BT** and select **NMEA** as the format. After that, click the **Apply** button

<p style="text-align:center"><img src="../img/reach/mock-location/position-output.png" style="width: 800px;"/></p>

!!! note ""
	The error message **Send error (111)** will be displayed. This is normal as there is no client connected to the NMEA stream yet.

## Android mock location

We provide a guide on how to use Reach with [Lefebure NTRIP Client](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient).

Besides being an NTRIP Client, this app also allows NMEA data input via Bluetooth and supports Android feature called **mock location**. This feature allows substituting your device's built-in GPS receiver with an external location provider, Reach in our case.

!!! note ""
	Lefebure NTRIP Client allows GIS apps in the Android device to  use accurate coordinates from Reach

* Install the app [Lefebure NTRIP Client](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient) in your Android device

* Open **Developer Options** on your Android device and choose **Lefebure NTRIP Client** in **Select mock location app** field

<p style="text-align:center"><img src="../img/reach/mock-location/developer-options.jpg" style="width: 800px;"/></p>

*  Launch the Lefebure NTRIP Client app and tap on the **settings** icon (gear in the upper right corner)

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-main-screen.jpg" style="width: 800px;"/></p>

* Go to the **Receiver Settings**

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-settings.jpg" style="width: 800px;"/></p>

!!! check "Inside Receiver Settings:" 
    1. Configure Receiver Connection as **External via Bluetooth**
    2. Change Bluetooth device to the Reach you are paired with  
    3. Change Bluetooth Connection Method to **Secure via Reflection**  
    4. Enable **GPS Mock Locations** 

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-receiver-settings-1.jpg" style="width: 800px;"/></p>

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-receiver-settings-2.jpg" style="width: 800px;"/></p>

* Go back to the main screen and hit **Connect** button

!!! tip ""
	Check the log messages to confirm the Bluetooth connection got established and the information about satellites is updated every second

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-connected.jpg" style="width: 800px;"/></p>

From this moment on, all apps in the Android device that use location services will automatically have access to the positional data streamed from Reach. You can just open a GIS app you want to use and start surveying.

!!! note ""
	Tapping the **Disconnect** button in the Lefebure NTRIP Client will revert back to the Android built-in GNSS	