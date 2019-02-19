## Intro

In this quick tutorial we will show you how to two set up two Reach devices as a base and a rover with correction link over Wi-Fi.

!!! tip
    If you encounter any issues performing these steps, we will be happy to help
    at our [**community forum**](http://community.emlid.com/).


This tutorial only covers one use case. To get more information, follow these links:

* [Mechanical specs](specs/#mechanical-specs)
* [Electrical specs](specs/#electrical-specs)
* [Hardware integration](hardware-integration)
* [ReachView app](common/reachview/)

## Powering up

* Take **Micro-USB <--> USB cable** that is coming with the package.

* Plug **Micro-USB end** of the cable into **Micro-USB port** on Reach and plug another end into 5V power source such as USB power bank, USB wall adapter or USB port of a computer.

!!! danger
    Do not plug two power supplies at the same time as it may damage the device.

More on power supply you can read [here](power-supply/).

## Connecting and placing GPS antenna

* Plug antenna cable into MCX socket on Reach. 

* Place antenna on a ground plane. It could be a cut piece of metal > 100mm in diameter, roof of a car or metal roof of a building. 

!!! warning
    There **should be no** obstacles near the antenna that could block the sky view higher than 30 degrees above horizon.
     **Do not** test the device indoors or near buildings, do not cover the skyview for the antennas with laptops, cars or yourself. RTK requires good satellite visibility and reception.

A guide how to properly place the antennas is available in [Antenna Placement](antenna-placement) section.

## Connecting to Reach

When Reach M+ is powered for the first time it will create a Wi-Fi hotspot.

* Open a list of Wi-Fi networks on your smartphone, tablet or laptop.

* Connect to a network named **reach:xx:xx** (ex. reach:66:ac).

* Type network password: **emlidreach**.

## Setting up Wi-Fi

* Get ReachView app for your mobile device:

| Download links |  |
|-------------|----------|
|[Google Play](https://play.google.com/store/apps/details?id=com.reachview)|[App Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)|

* Launch the app and choose available Reach M+ from the list. You will see ReachView updater.

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_updater_main.png" style="width: 350px;"></div><br>

* Press plus button and enter your Wi-Fi network name, security type and password. Press Save button

!!! danger "Assure you are connecting to the existing network (such as home wi-fi, mobile phone hotspot, etc)"
    Use your Wi-Fi network name and password. The name of the network on the screenshot below is an example. 

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_updater_wifi.png" style="width: 350px;"></div><br>

* Press on your added network and click Connect. 

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_updater_wifi_connect.png" style="width: 350px;"></div><br>

* After that Reach device will attempt to connect your Wi-Fi network.

!!! tip 
    If your device did not connect to Wi-Fi network it will switch to hotspot mode. Check your network name and password and try again.


* After connecting Reach device to an existing Wi-Fi network you can reconnect with your mobile device to the same network and see your Reach M+ in iOS/Android ReachView app.

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_ios_android.png" style="width: 400px;"></div><br>


Read more on resolving IP addresses in the [ReachView section](common/reachview/).

!!! danger "Reach can't work on the 192.168.2.xx subnet "
    As 192.168.2.x subnet is reserved inside Reach for Ethernet connections, you will need to perform initial setup in a different Wi-Fi or change router settings. Routers usually have a setting to change the subnet address, so you can set it to 192.168.1.xx.

## Updating ReachView

After connecting to Reach you will see ReachView Updater again which will install latest updates.

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_updater_finish.png" style="width: 350px;"></div><br>

* Press **Reboot and go to the app!** button. Wait while device reboots.

* In about a minute refresh the page with ReachView app.

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_loading.png" style="width: 800px;"></div><br>


## Working with ReachView app


### Interface walkthrough

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_status_menu.png" style="width: 800px;"></div><br>

ReachView menu consists of 9 tabs, but we only need three of them to start work:

* **Status** tab which shows current satellite levels, RTK parameters, coordinates and map.

* **Base mode** tab is used to set correction output type, base coordinates and RTCM3 messages.

* **Correction input** tab is used to set base correction for the rover.

### Setting up base station

* Connect to Reach you want to use as a base.

* Navigate to **Base mode** tab and turn on Correction output box toggle.

* Wait until base averages it's position in Base coordinates box.

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_base_mode_menu.png" style="width: 1200px;"></div><br>

By default, base output stream will be available on a **TCP port 9000**.


### Setting up rover

* Connect to the second Reach. 

* Navigate to **Correction input** tab. 

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_correction_input_tab.png" style="width: 800px;"></div><br>

* Choose TCP correction mode.

* Choose **Client** in **Role** field.

* Add base IP in **Address** field.

* Add base correction port in **Port** field. Default one is **9000**.

* Choose correction input **Format**. Default one is **RTCM3**. 

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_correction_input_tcp.png" style="width: 800px;"></div><br>

* Save settings by pushing **Apply** button.


### Viewing results

* Go to **Status** tab of the app on the rover device.

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_status_menu_correction.png" style="width: 800px;"></div><br>

You can see a bar chart with satellite levels, RTK parameters, positioning mode and solution status, current coordinates of rover and base in LLH format, velocity and map. In this quick tutorial, positioning mode is set to "Kinematic" which is the main RTK mode.

* If everything has been set up correctly, **Solution status** will be **Float** and **you should see grey bars near satellite levels bars**. 

!!! warning ""
    **Float** means that base corrections are now taken into consideration and positioning is relative to base coordinates, but the integer ambiguity is not resolved.  

    If you see **"-"** or **Single** in **Solution status** box on this step, that means that some settings are incorrect.  

    **"-"** means there is no information for the software to process. Either not enough time has passed or the antenna is not placed correctly.  

    **Single** means that rover has found a solution relying on it's own receiver and base corrections are not taken into consideration yet. If rover is started in single mode, this will also be the result.

* If everything has been set up correctly and base and rover have good sky visibility, you should see **Solution status** change to **Fix** in a few minutes. **Fix** means that positioning is relative to the base and the integer ambiguity is resolved.

<div style="text-align: center;"><img src="../img/reachm-plus/quickstart/reach_view_status_menu_fix.png" style="width: 800px;"></div><br>

* Now you can see <font color="green"> green </font> points on the map below. <font color="orange"> Orange </font> points show **Float** solution. <font color="red"> Red </font> - **Single** solution.

* You're ready to go!

## More reading

Congratulations on finishing the quickstart tutorial! Continue to learn about setting up different correction links in the [ReachView section](common/reachview).
