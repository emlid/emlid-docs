##Overview

In this tutorial, you will find the information on how to survey in RTK with senseFly drones and Reach RS2.

!!! note ""
    Step-by-step guide can be also found on [senseFly Knowledge Base](https://sensefly.zendesk.com/hc/en-us/articles/360011254199-Emlid-Reach-RS2-RTK-Workflow).

##Setting up Reach RS2

In this part, we will explain how to configure Reach RS2 to transmit corrections to the PC via Bluetooth.

###Placing the Reach RS2 receiver

The video below demonstrates how to place the Reach RS2 base over a known point.

<div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/FilRoPVDjCs" allowfullscreen></iframe></div>

To find out other ways of placing the local base station, [consult this guide](../common/tutorials/placing-the-base/).

The general steps for placing the base receiver are described below.

* Make sure you choose an appropriate location to place Reach RS2 base station. Take a look at 2 pictures below. The left picture demonstrates desirable conditions for the base location. The right one is an example of bad surrounding conditions such as the reduced view of the sky, possible obstructions or vegetation nearby

<div style="text-align: center;"><img src="../img/reachrs2/sensefly-rtk/Reach-base-position-correct-wrong.png" style="width: 600px;"></div>

* Make sure your Reach RS2 is placed precisely above the marked point on the tripod and leveled

* If you are setting up base coordinates manually, measure the antenna height offset

!!! note ""
    Antenna height is measured as the distance between the mark and the antenna reference point (ARP).

For Reach RS2, consider the antenna height as the distance between the mark and the bottom of Reach RS2 (h on the figure below) plus 134 mm.

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/placing-reach.png" style="width: 800px;"/></p>

!!! note ""
    If you require absolute centimeter-level accuracy, you need to calculate an absolute base coordinate.

    If you require relative centimeter-level accuracy, you can average base position.

###Pairing with PC

* Connect to your Reach RS2 using the ReachView App

??? note "Steps for connecting via hotspot"

    * Open a list of Wi-Fi networks on your PC

    * Connect to a network named **reach:xx:xx**

    * Type network password: **emlidreach**

    **For smartphone:**

    * Choose Reach RS2 from the list of available devices in the ReachView App

    **For PC:**

    * Launch a web browser (we recommend using Chrome or Mozilla)

    * Go to 192.168.42.1

??? note "Steps for connecting via Wi-Fi"

    * Make sure that your smartphone/PC has connected to the same Wi-Fi network as Reach RS2

    **For smartphone:**

    * Open ReachView app

    * Refresh the list of devices

    * Tap **reach**

    **For PC:**

    * After connecting the Reach device to an existing Wi-Fi network, you will need to identify its IP

    For this you can use:

    1. "**Fing**" app for [iOS](https://goo.gl/Ho0qB) or [Android](https://goo.gl/7Wuwu)

    2. ["**Nmap**"](https://nmap.org/) on Linux/OS X

    3. ["**Zenmap**"](https://nmap.org/zenmap/) on Windows

    <div style="text-align: center;"><img src="../img/reachrs2/sensefly-rtk/fing.png" style="width: 500px;"></div>

    * Reach will show up as "**Murata Manufacturing**" or "**AMPAK Technology**" device in these apps

    * Put Reach IP in the address bar and go

* Configure constellation select in the [RTK Settings tab.](../common/reachview/rtk-settings) For working with eBee drones, enable GPS and GLONASS at 1 Hz

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/rtk-settings.png" style="width: 600px;"/></p>

* Go to the Logging tab

* Enable the raw data log in UBX format

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/logging-tab.png" style="width: 600px;"/></p>

* Go to the Bluetooth tab

* Enable Bluetooth and enable *Always discoverable* option

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/bluetooth-open.png" style="width: 600px;"/></p>

* Enable Bluetooth on your PC

* Open Bluetooth settings

* Click on *Add Bluetooth or other device*

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/open-bluetooth.png" style="width: 400px;"/></p>

* Choose the Bluetooth option in the *Add a device* window

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/add-device.png" style="width: 400px;"/></p>

* Make sure your Reach RS2 is discoverable and can be seen in the list of devices

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/find-device.png" style="width: 400px;"/></p>

* Once you can see Reach RS2 in the list, connect to it

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/connecting-to-reach.png" style="width: 400px;"/></p>

* If the connection is successful, you will get a message "Your device is ready to go!"

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/connected.png" style="width: 400px;"/></p>

* Now you can proceed to the next step

###Configuring correction output

* Go to Base mode tab

* Turn on the correction output via Bluetooth

* Choose the base position mode and averaging time. In the example below, it is Average Single. You can find out more about different base position modes in [this guide.](../common/tutorials/placing-the-base/)

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/correction-output-bt.png" style="width: 600px;"/></p>

* Choose transmitted RTCM3 messages

<center>

|RTCM3 messages|Message type|
|:---:|:---:|
||**Minimal required messages**|
|1006|ARP station coordinate   |
|1074|GPS MSM4      |
||**Optional messages for other GNSS **|
|1084|GLONASS MSM4|
|1094|Galileo MSM4|
|1124|BeiDou MSM4|

</center>

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/base-rtcm3.png" style="width: 600px;"/></p>

### Checking the connection

You will need to find out what COM port on your PC is used by Reach RS2. For that, we recommend using the PuTTY client for Windows.

* [Download and install PuTTY](https://www.putty.org/)

* Open Device Manager on your computer

* Check available Standard Serial over Bluetooth link ports

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/device-manager.png" style="width: 400px;"/></p>

* Open PuTTY

* Go to the Session tab

* Specify the COM port in the *Serial line*

* Choose speed at 9600

* Choose the connection type Serial

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/putty-open.png" style="width: 400px;"/></p>

You can do the same in the Serial tab:

* Go to the Serial tab

* Specify the COM port in the *Serial line to connect to*

* Choose speed at 9600

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/putty-show.png" style="width: 400px;"/></p>

* Press *Open*

If you have chosen the correct port, you will see the corrections from Reach RS2 in the RTCM3 format on the screen. If you cannot see the data coming, choose another COM port in Serial line.

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/pc-connection/putty-result.png" style="width: 400px;"/></p>

* Now you are ready to configure the RTK link in eMotion3

## Connecting to eMotion3

Now we will show you how to establish an RTK link with Reach RS2 base on your eBee drone.

* Launch [eMotion3](https://www.sensefly.com/software/emotion/)

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-open.png" style="width: 800px;"/></p>

* Create mission and go to the Mission tab

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-mission.png" style="width: 800px;"/></p>

* Press the *Connect* button. Connect to the drone by pressing *Connect to your drone* or simulate your flight by pressing *Start a simulation*

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-connect.png" style="width: 800px;"/></p>

* Activate your RTK/PPK license in the *eBee plus upgrade* tab of the Drone's panel. To activate a license for simulation, tick an *Activate update for simulator* box

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-license.png" style="width: 400px;"/></p>

Now you can see the RTK tab enabled on your Mission panel on your left.

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-mission-rtk.png" style="width: 300px;"/></p>

* Go to the RTK tab in the Mission panel

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-setup-rtk.png" style="width: 300px;"/></p>

* Press *Set-up RTK/PPK* to configure your base

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-local-base.PNG" style="width: 300px;"/></p>

* In the opened window, you can specify either a base station, reference points or a VRS. To configure the base station, press *Add base +* in the Base tab

* Set Reach RS2 to a Base name

* Set Other to a Base manifacturer

* Set Connection type to Serial

* Choose the COM port that you checked on the previous step

* Set the same baudrate for all connected devices

* Press *OK*

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/configure-base.png" style="width: 500px;"/></p>

* Once you configured the connection, you can choose the base station in the RTK tab

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/connect-to-reach.png" style="width: 300px;"/></p>

* Press on the chosen base station to see the *Set up Local Base* window

* Press *Open base-drone datastream*

!!! note ""
    If you are testing the setup inside, the GPS and GLONASS fields will show *Not sufficient* message

* Check the base position the drone receives

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/connect-base.png" style="width: 400px;"/></p>

* Go to the Drone's panel

* In the Instruments tab, you can see that the drone provides centimeter-level accuracy and the mode is *RTK-fixed*

<p style="text-align:center"><img src="../img/reachrs2/sensefly-rtk/emotion-connection/emotion-rtk-fixed.png" style="width: 400px;"/></p>

Now you have successfully configured RTK corrections on your drone from Reach RS2!
