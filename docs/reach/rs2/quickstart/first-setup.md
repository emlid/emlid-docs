## Intro

In this tutorial, we will walk you through the following steps:

* Install the ReachView app
* Connect to Reach RS2
* Perform firmware update
* Set up base and rover connection

To do that, you will need Reach RS2 itself, a Wi-Fi network with Internet access and a smartphone or PC.


## Video guide

The video below covers the process of the first update.

<div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/Miy8L_1AgCQ" allowfullscreen></iframe></div>

For managing Reach RS2, we recommend using ReachView app. Get it from the App Store or Google Play before updating.

<center>

|Google Play|App Store|
|:-------------:|:----------:|
|[Android ReachView app [7.7 MB]](https://play.google.com/store/apps/details?id=com.reachview)|[iOS ReachView app [7.7 MB]](https://apps.apple.com/us/app/reachview/id1295196887)|

</center>

!!! note ""
    If you encounter any issues performing these steps, we will be happy to help at our [**community forum**](http://community.emlid.com/)


## Text guide

### Powering up

Hold the power button for 3 seconds to turn Reach RS2 on. After about 30 seconds Power LEDs will stop blinking. The Network LED will stay solid white. Reach RS2 is now broadcasting Wi-Fi.

<div style="text-align: center;"><img src="../img/quickstart/first-setup/hotspot.png" style="width: 200px;"></div>

### Connecting to Reach RS2

* Open a list of Wi-Fi networks on your smartphone/PC

* Connect to a network named **reach:xx:xx**

* Type network password: **emlidreach**


### Setting up Wi-Fi

??? note "Using Reach with iOS/Android device"

    1. Get the ReachView app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [App Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
    2. Open the app and choose Reach from the list
    4. Tap the *plus* button and enter your Wi-Fi network name, security type, and password
    5. Tap *Save* button
    6. Tap on the added network and then *Connect*

??? note "Using Reach with a web browser from any device"

    1. Launch a web browser (we recommend using Chrome or Mozilla)
    2. Go to 192.168.42.1
    3. Tap the *plus* button and enter your Wi-Fi network name, security type, and password
    4. Tap *Save* button
    5. Tap on the added network and then *Connect*

Reach RS2 will stop broadcasting Wi-Fi and connect to your network. 

The Network LED will blink rapidly while scanning for networks. Once Reach connects to Wi-Fi, the Network LED will be solid blue.

<div style="text-align: center;"><img src="../img/quickstart/first-setup/client-mode.png" style="width: 200px;"></div>

!!! note ""
    If your device did not connect to a Wi-Fi network, it will switch back to a hotspot mode.
    In that case, repeat the steps and double check your network name and password. 


### Accessing Reach RS2 device in a network

!!! danger ""
    Make sure that your smartphone/PC has connected to the same Wi-Fi network as Reach.

??? note "Using Reach with iOS/Android device"

    1. Open ReachView app
    2. Refresh the list of devices
    3. Tap **reach**


??? note "Using Reach with PC"

    After connecting the Reach device to an existing Wi-Fi network, you will need to identify its IP.

    For this you can use:

    * "**Fing**" app for [iOS](https://goo.gl/Ho0qB) or [Android](https://goo.gl/7Wuwu)

    * ["**Nmap**"](https://nmap.org/) on Linux/OS X

    * ["**Zenmap**"](https://nmap.org/zenmap/) on Windows

    <div style="text-align: center;"><img src="../img/quickstart/first-setup/fing.png" style="width: 500px;"></div>

    * Reach will show up as "**Murata Manufacturing**" or "**AMPAK Technology**" device in these apps

    * Put Reach IP in the address bar and go


### Updating ReachView

After connecting to Reach RS2, you will see ReachView Updater again. Wait until it checks for the latest updates.

* If there is an update, press *Update ReachView* button and wait. This process will take a few minutes

* When it is done tap *Reboot and go to the app* button to reboot Reach RS2

* Wait for the blue LED to stop blinking, showing that Reach RS2 has joined your Wi-Fi network again

* Press *Reboot and go to the app* button and wait while device reboots

If you use ReachView app, swipe right to get back to the list of devices, refresh the list and tap **reach**. As for the web browser, just refresh the page with ReachView. You will see the filling EMLID logo indicating the loading process of ReachView.

Your Reach RS2 is ready for work. Do the same with all other units.

[Now you can set up Base and Rover connection by following instruction from our guide.](base-rover-setup.md)
