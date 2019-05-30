### Intro

In this tutorial we will go through the next steps:

* Connecting Reach RS/RS+ to another Wi-Fi network
* Updating ReachView for the first time
* Setting up a rover and a base to work in RTK mode with correction link over Lo-Ra radio

The video below covers the process of the first update: powering Reach RS/RS+ on, connecting to a Wi-Fi and installing the latest version of ReachView app. After completing the video instructions continue the tutorial on [Placing Reach RS/RS+](#placing-reach-rsrs-module) step or follow through the video guide [Base and Rover setup](#base-and-rover-setup).

???+ note "My Reach RS/RS+ has the ReachView app sticker on top"
    <div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/fIY__hNjcNI" allowfullscreen></iframe></div>

??? note "My Reach RS has no sticker on top"
    <div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/HCOqtSUumow" allowfullscreen></iframe></div>


!!! tip ""
    If you encounter any issues performing these steps, we will be happy to help at our [**community forum**](http://community.emlid.com/).

This tutorial only covers one use case. To get more information, follow these links:

* [Mechanical specs](../specs/#mechanical-specs)
* [Electrical specs](../specs/#electrical-specs)
* [ReachView app](common/reachview/index.md)

## Powering up

* To power on Reach RS/RS+ hold Power button for 3 seconds. Power LED is on to show Reach RS/RS+ is turned on. Solid network state LED (blue) indicates Reach RS/RS+ has launched its own Wi-fi hotspot.

!!! note  ""
    Reach RS/RS+ has internal battery designed for 30-hours of autonomous work. Reach RS/RS+ may be charged on the go with the micro-usb cable coming within the package. Battery status check is available through ReachView interface.

## Connecting to Reach RS/RS+

When Reach RS/RS+ is powered for the first time it will create a Wi-Fi hotspot.

* Open a list of Wi-Fi networks on your smartphone, tablet or laptop.

* Connect to a network named **reach:xx:xx** (ex. reach:66:ac).

* Type network password: **emlidreach**.

## Setting up Wi-Fi

After connecting to the network hosted by reach, open a web browser on your smartphone, tablet or laptop.

* Type either **http://reach.local** or **http://192.168.42.1** in the address bar and you will see ReachView Updater.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_updater_main.png" style="width: 350px;"></div><br>

!!! note ""
    If your interface looks different, you need to reflash Reach device with v2.3 image by following [this guide](common/reachview/firmware-reflashing.md). You only need to do this if your device was purchased before 1 March 2017.

* Press plus button and enter your Wi-Fi network name, security type and password. Press Save button

!!! danger "Assure you are connecting to the existing network (such as home wi-fi, mobile phone hotspot, etc)"
    Use your Wi-Fi network name and password. The name of the network on the screenshot below is an example. 

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_updater_wifi.png" style="width: 350px;"></div><br>

* Press on your added network and click Connect. 

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_updater_wifi_connect.png" style="width: 600px;"></div><br>

* After that Reach device will attempt to connect your Wi-Fi network.

!!! tip ""
    If your device did not connect to Wi-Fi network it will switch to hotspot mode.
    You can find Reach on **http://reach.local** or **http://192.168.42.1**.
    Check your network name and password and try again.  

## Accessing Reach RS/RS+ device in a network

After connecting Reach device to an existing Wi-Fi network, you will need to identify it's IP. You may either use network scanning tools or use ReachView app for Android/iOS. 

### Network scanning tools

For this you can use:

* "**Fing**" app for [iOS](https://goo.gl/Ho0qB) or [Android](https://goo.gl/7Wuwu).

* ["**Nmap**"](https://nmap.org/) on Linux/OS X.

* ["**Zenmap**"](https://nmap.org/zenmap/) on Windows. 

<div style="text-align: center;"><img src="../img/reachrs/quickstart/fing.png" style="width: 500px;"></div><br>

* Reach will show up as "**Murata Manufacturing**" device in these apps.

* Put Reach IP in address bar and go.

Read more on resolving IP addresses in the [ReachView section](common/reachview/index.md#resolving-ip).

### App for iOS/Android

Since ReachView v.2.8.0 you can connect to your Reach device with an app using your Android or iOS device.


| Download links |  |
|-------------|----------|
|[Google Play](https://play.google.com/store/apps/details?id=com.reachview)|[App Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)|

After launching the app you'll see the list of the available receivers in your network. 

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_ios_android.png" style="width: 400px;"></div><br>

!!! danger "Reach can't work on the 192.168.2.xx subnet "
    As 192.168.2.x subnet is reserved inside Reach for Ethernet connections, you will need to perform initial setup in a different Wi-Fi or change router settings. Routers usually have a setting to change the subnet address, so you can set it to 192.168.1.xx.

## Updating ReachView

After connecting to Reach RS/RS+ you will see ReachView Updater again which will install latest updates.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_updater_finish.png" style="width: 350px;"></div><br>

* Press **Reboot and go to the app!** button. Wait while device reboots.

* In about a minute refresh the page with ReachView app.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_loading.png" style="width: 800px;"></div><br>

## Base and Rover setup

This tutorial will guide you through the setup process of two Reach RS units as rover and base station and will help you to configure communication between them via LoRa radio in RTK mode.

<div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/4GfUDoDwEAE" allowfullscreen></iframe></div>

## Placing Reach RS/RS+ module

 
* Reach RS/RS+ may be placed on a tripod with a 1/4" mount thread. Each package comes with an adapter to 5/8" survey pole thread.

!!! danger "Attention"
    There **should be no** obstacles near the antenna that could block the sky view higher than 30 degrees above horizon.
    **Do not** test the device indoors or near buildings, do not cover the skyview for the antennas with laptops, cars or yourself. RTK requires good satellite visibility and reception.

A guide how to properly place the antennas is available in [Reach RS/RS+ placement](common/placement.md) section.


## Working with ReachView app

### Battery status check

You may check Reach RS/RS+ battery status by clicking on the sign in the upper right corner.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/battery.png" style="width: 450px;"></div><br>

### Interface walkthrough

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_status_menu.png" style="width: 800px;"></div><br>

ReachView menu consists of 9 tabs, but we only need three of them to start work:

* **Status** tab which shows current satellite levels, RTK parameters, coordinates and map.

* **Base mode** tab is used to set correction output type, base coordinates and RTCM3 messages.

* **Correction input** tab is used to set base correction for the rover.

### Setting up base station

* Connect to Reach RS/RS+ you want to use as a base.

* Go to settings and change the name to "reach-base". This will help to simplify the work in field when you need to switch between the devices.

* Navigate to **Base mode** tab and turn on Correction output box toggle.

* Select LoRa tab and set frequency between 862 MHz and 1020 Mhz and set output power. 

!!! tip ""
    Using LoRa modulation it is possible to hit up to 19km in line of sight or a few km in urban areas with just 20 dBm power output.


!!! danger ""
    Make sure to select appropriate output power and frequency according to your local regulations. 

* Next set the parameter of air rate. 

!!! tip ""
    The lower the air rate, the longer the working distance will be. In order to unlock lower air rates disable correction messages or reduce rate. 

* Apply settings and wait until base averages it's position in Base coordinates box.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reachrs-lora-base.png" style="width: 1200px;"></div><br>


### Setting up rover

* Connect to the second Reach. 

* Go to settings and change the name to "reach-rover".

* Navigate to **Correction input** tab. 

* Choose LoRa correction mode.

* Frequency and air rate settings must match what was configured on the base. 

* Apply changes and you will see rover is connected to base.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reachrs-lora-rover.png" style="width: 1200px;"></div><br>

* The base now is sending corrections on rover via LoRa radio in RTCM 3 format. 

### Viewing results

* Go to **Status** tab of the app on the rover device.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_status_menu_correction.png" style="width: 800px;"></div>

You can see a bar chart with satellite levels, RTK parameters, positioning mode and solution status, current coordinates of rover and base in LLH format, velocity and map. In this quick tutorial, positioning mode is set to "Kinematic" which is the main RTK mode.

* If everything has been set up correctly, **Solution status** will be **Float** and **you should see grey bars near satellite levels bars**. 

!!! note ""
    **Float** means that base corrections are now taken into consideration and positioning is relative to base coordinates, but the integer ambiguity is not resolved.  

    If you see **"-"** or **Single** in **Solution status** box on this step, that means that some settings are incorrect.  

    **"-"** means there is no information for the software to process. Either not enough time has passed or the antenna is not placed correctly.  

    **Single** means that rover has found a solution relying on it's own receiver and base corrections are not taken into consideration yet. If rover is started in single mode, this will also be the result.

* If everything has been set up correctly and base and rover have good sky visibility, you should see **Solution status** change to **Fix** in a few minutes. **Fix** means that positioning is relative to the base and the integer ambiguity is resolved.

<div style="text-align: center;"><img src="../img/reachrs/quickstart/reach_view_status_menu_fix.png" style="width: 800px;"></div><br>

* Now you can see <font color="green"> green </font> points on the map below. <font color="orange"> Orange </font> points show **Float** solution. <font color="red"> Red </font> - **Single** solution.

* You're ready to go!

## More reading

Congratulations on finishing the quickstart tutorial! Continue to learn about setting up different correction links in the [ReachView section](common/reachview/index.md).

