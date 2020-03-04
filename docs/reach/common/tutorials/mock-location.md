#Getting Reach coordinates on Android via BT

##Overview

This guide demonstrates how to get precise coordinates from Reach on an Android device over Bluetooth.

!!! tip "Some of the GIS apps for Android used with Reach:"
	* Mobile Topographer Pro
	* PointMan
	* ESRI ArcGIS Collector
	* Mapit GIS
	* LandStar
	* Autocad360


## Video guide

The video below covers the process of connecting Reach to an Android device for data collection.

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/aC3ti1qynk4" frameborder="0" allowfullscreen></iframe></div>

## Text guide

Make sure your Android device provides Bluetooth connectivity.

!!! tip ""
	To output a centimeter accurate position, Reach should be in RTK mode. Refer to the article [How RTK works](rtk-introduction.md) to learn more.

Configure Reach unit to act as a rover in RTK.

??? note "Getting corrections from Reach RS2 base on Reach RS2 rover"
	Set up RTK communication between 2 Reach RS2 units over LoRa radio [following this video guide](https://youtu.be/-K32ayVmH6U).

??? note "Getting corrections from Reach RS+ base on Reach RS+ rover"
	Set up RTK communication between 2 Reach RS+ units over LoRa radio [following this video guide](https://youtu.be/4GfUDoDwEAE). 

??? note "Getting corrections from NTRIP/CORS"
	Configure NTRIP/CORS network as a source of positioning corrections for:

	* [Reach RS2 rover](https://docs.emlid.com/reachrs2/ntrip-workflow/)
	* [Reach M+ or Reach RS/RS+ rover](../quickstart/ntrip-workflow.md)

###Pairing Reach with an Android device

**Access Reach rover using ReachView**

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

* Open **Bluetooth** configuration screen, enable Bluetooth connection and set on the *Always discoverable*

<p style="text-align:center"><img src="../img/reach/mock-location/enable-bt.png" style="width: 800px;"/></p>

!!! note ""
	Reach name is displayed just above its MAC. In this guide, we used the unit named as **Reach**.

**Access an Android device**

* Navigate to the Bluetooth configuration screen. Activate the Bluetooth connection

* Wait for Reach to be listed as an available device

!!! tip ""
	Keep Reach within a few meters from your Android device.

<p style="text-align:center"><img src="../img/reach/mock-location/bt-scanning.jpg" style="width: 800px;"/></p>

**Back to the ReachView app**

* You should now be able to see your Android device listed as an available device. In this guide, we used a device named as **Galaxy Tab A (2017)**

<p style="text-align:center"><img src="../img/reach/mock-location/discoverable-devices.png" style="width: 800px;"/></p>

* Tap the name of the Android device in ReachView

**Back to the Android device**

* You should receive a pairing request from Reach. Confirm it

<p style="text-align:center"><img src="../img/reach/mock-location/pairing-request.jpg" style="width: 800px;"/></p>

<br>

Reach and Android device are now paired:

<p style="text-align:center"><img src="../img/reach/mock-location/android-paired.jpg" style="width: 800px;"/></p>

<p style="text-align:center"><img src="../img/reach/mock-location/reachview-paired.png" style="width: 800px;"/></p>

### Position output from Reach to Android

* In ReachView app, navigate to the **Position output** screen

* Activate *Output 1*, set it to BT and select solution output format to NMEA. After that, click the *Apply* button

<p style="text-align:center"><img src="../img/reach/mock-location/position-output.png" style="width: 800px;"/></p>

!!! note ""
	You might see an error message **Send error (111)**  in some cases. This is fine as long as there is no client connected to the NMEA stream yet.

### Android mock location

We provide a guide on how to use Reach with [Lefebure NTRIP Client](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient).

Besides being an NTRIP Client, this app also allows NMEA data input via Bluetooth and supports Android feature called **mock location**. This feature allows substituting your device's built-in GPS receiver with an external location provider.

!!! note ""
	Lefebure NTRIP Client allows GIS apps in the Android device to use accurate coordinates from Reach.

* Install the app [Lefebure NTRIP Client](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient) in your Android device

* Open *Developer Options* on your Android device and choose *Lefebure NTRIP Client* in *Select mock location app* field

<p style="text-align:center"><img src="../img/reach/mock-location/developer-options.jpg" style="width: 800px;"/></p>

!!! note ""
	It is recommended to switch off the power-saving mode on your phone as it may limit background data usage for the Lefebure NTRIP client app.

*  Launch the Lefebure NTRIP Client app and tap on the *settings* icon (gear in the upper right corner)

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-main-screen.jpg" style="width: 800px;"/></p>

* Go to the *Receiver Settings*

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-settings.jpg" style="width: 800px;"/></p>

!!! check "Inside Receiver Settings:" 
    1. Configure Receiver Connection as *External via Bluetooth*
    2. Change Bluetooth device to the Reach you are paired with  
    3. Change Bluetooth Connection Method to *Secure via Reflection*
    4. Enable *GPS Mock Locations*

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-receiver-settings-1.jpg" style="width: 800px;"/></p>

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-receiver-settings-2.jpg" style="width: 800px;"/></p>

* Go back to the main screen and hit *Connect* button

!!! tip ""
	Check the log messages to confirm the Bluetooth connection got established and the information about satellites is updated.

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-connected.jpg" style="width: 800px;"/></p>

From this moment on, all apps in the Android device that use location services will automatically have access to the positional data streamed from Reach. You can just open a GIS app you want to use and start surveying.

!!! note ""
	Tapping the *Disconnect* button in the Lefebure NTRIP Client will revert back to the Android built-in GNSS.	

##Collecting Data with Reach and ArcGIS

We provide a video tutorial explaining how to use Reach with ArcGIS.

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/_D2Y45JwCgs" frameborder="0" allowfullscreen></iframe></div>
