## Video Demonstration

A deep gratitude goes to our pro-user [TB_RTK](https://community.emlid.com/users/tb_rtk/activity) for a significant contribution in this tutorial. 

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/yy8EVSMq9Bk" frameborder="0" allowfullscreen></iframe></div>

It is possible to replace internal GPS on your Android device with Reach, this way any positioning app will be able to use precise RTK coordinates. Commonly used apps are Mobile Topographer Pro and ESRI Arcgis Collector.

## Reach configuration

To use Reach with Android app you will need to do the following:

* Pair your Android device with Reach / Reach RS
 
!!! tip
    To do this, make your device discoverable. Then, go to the **Wifi/Bluetooth Tab** and find your device in bluetooth section. Once your device appears in the "discoverable" section, hit it to send a pairing request. Accept the pairing request on your device. Your device will appear in the "paired devices section".


<p style="text-align:center"><img src="../img/reach/mock-location/bluetooth.png" style="width: 800px;"/></p>


* In the "Position output Tab set position output to BT and format to **NMEA**

!!! tip
    Don't forget to Apply the new rover settings

<p style="text-align:center"><img src="../img/reach/mock-location/solution.png" style="width: 800px;"/></p>

## Android mock location

We provide a guide on how to use Reach with [Lefebure NTRIP caster](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient) by Lefebure Design.

Despite being called an NTRIP caster this app allows NMEA data input via bluetooth as well. Also, it supports Android feature called **mock location**, which allows to substitute your device's built-in GPS receiver with an external location provider, Reach in our case.

To connect Reach, do the following:

* Open the app, go to the settings(gear in the upper right corner)

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-main-screen.jpg" style="width: 300px;"/></p>

* Then go to receiver settings

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-settings.jpg" style="width: 300px;"/></p>

!!! check "Inside Receiver Settings:" 
    1. Change Bluetooth device to the Reach you are paired with  
    2. Change Bluetooth Connection Method to **Secure via Reflection**  
    3. Enable **Mock location** if you need to  

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-receiver-settings.jpg" style="width: 300px;"/></p>

* Go back to the main screen, hit **Connect** and watch the connection!

<p style="text-align:center"><img src="../img/reach/mock-location/lefebure-connected.jpg" style="width: 300px;"/></p>


Now coordinates in your Android device are replaced with coordinates from Reach / Reach RS and you can use them in any app.

