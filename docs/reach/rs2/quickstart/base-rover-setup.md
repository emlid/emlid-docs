## Video guide

This tutorial will show how to set up two Reach RS2 units as rover and base and how to make them work over LoRa radio in RTK mode.

For setting NTRIP base corrections, [follow the steps from "Working with NTRIP service" guide](../ntrip-workflow.md).

<div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/-K32ayVmH6U" allowfullscreen></iframe></div>


## Text guide

### Renaming Reach devices

By default, every Reach has the same name, and the first thing we will do is renaming them so it is easier to distinguish base and rover in the field.

!!! note "How to define Reach?"
    There is an easy way to understand which unit you are connected to. Just open the menu and tap the lamp-shaped button. Power Button LED will start to blink.

* Connect to Reach RS2 you want to use as a base

* Go to settings and change the name to **reach-base**. This name will also be used as a Wi-Fi network label when Reach is in hotspot mode

* Press *Save*

!!! tip ""
    Use a special sticker from a package to mark the unit.

Do the same with the second Reach RS2. However, use **reach-rover** name instead of **reach-base**.


### Setting up base station

Now we will configure RTK settings and communication between base and rover. Let’s start with the base.

* Connect to the base unit

* Open **RTK Settings** tab and pick each of the satellite systems

* Set the update rate at 1 Hz

<div style="text-align: center;"><img src="../img/quickstart/base-rover-setup/reachrs2-base-rtk-settings.png" style="width: 800px;"></div>


Now we will set up LoRa radio on Reach RS2 base to broadcast RTK corrections.

* Go to **Base mode** tab and in the **Corrections output** section select **LoRa**

* Set the output power to **20 dBm** and air rate at **9.11 kb/s**

<div style="text-align: center;"><img src="../img/quickstart/base-rover-setup/reachrs2-base-lora.png" style="width: 800px;"></div>

* In the list of RTCM3 messages select to output **ARP station coordinates** at **0.1 Hz** and others at **1 Hz**

<div style="text-align: center;"><img src="../img/quickstart/base-rover-setup/reachrs2-base-rtcm3.png" style="width: 800px;"></div>

!!! danger ""
    Make sure to select appropriate output power and frequency according to your local regulations. In case there are restrictions, frequency band limitations will be applied automatically. 

* Apply settings and wait until base averages its position in Base coordinates box


### Setting up rover

* Connect to the rover unit

* Go to **RTK settings** tab

* Set the positioning mode to **Kinematic**

* Select the same GNSS systems as for the base, set 5 Hz update rate and press *Apply*

<div style="text-align: center;"><img src="../img/quickstart/base-rover-setup/reachrs2-rover-rtk-settings.png" style="width: 800px;"></div>

Now we will configure LoRa radio on the rover unit to receive the corrections. 

* Go to **Correction input** tab

* In the **Base correction** pick **LoRa**

* Frequency and air rate settings must match what was configured on the base

* Apply changes and you will see rover is connected to the base

<div style="text-align: center;"><img src="../img/quickstart/base-rover-setup/reachrs2-rover-lora.png" style="width: 800px;"></div>

!!! tip ""
    To make sure that corrections are passing from base to rover, you can put both receivers by the window for a few minutes to provide the sky visibility. Go to the status tab on the rover unit. Colorful bars are standing for available satellites. If LoRa is configured correctly, they will be accompanied by grey bars. These are standing for the corrections received from the base station.


### Placing Reach RS2 module

Once the units are configured, we can move to the field. For the field works, you will need a tripod and survey pole.

Mount Reach RS2 base and accurately level the tripod. Put the rover on the pole and attach the LoRa antennas. Turn on the devices.

!!! danger "Attention"
    There **should be no** obstacles near the antenna that could block the sky view higher than 30 degrees above the horizon.
    **Do not** test the device indoors or near buildings, do not cover the sky view for the antennas with laptops, cars or yourself. RTK requires good satellite visibility and reception.

A guide on how to properly place the antennas is available in [Reach RS2 placement](../placement.md) section.

Let’s set up the base station.

* Connect to the base

* Go to **Base mode** tab

* In the **Base coordinates** section select **Average single** and set averaging time. The longer you choose to accumulate data, the more accurate base position you get. Don’t move the base while Reach is accumulating data

* Once the position is calculated, press *Apply*

* Go to the **Status** tab on the base station to assure ReachView shows plenty of green satellites

Connect to the rover and check the status tab. If everything is configured correctly, you will see a lot of green satellites accompanied by grey bars.

<div style="text-align: center;"><img src="../img/quickstart/base-rover-setup/reachrs2-status-correction.png" style="width: 800px;"></div>


## Viewing results

Go to the **Status** tab of the app on the rover device.

Below the SNR chart, you’ll see the current solution status.

* **Single** means that rover has found a solution relying on its own receiver and base corrections are not applied. Precision in standalone mode is usually meter-level

* **Float** means that the base corrections are now taken into consideration

* **Fix** status means all ambiguities are resolved and RTK solution is centimeter-level accurate

After a short period of time, the rover gets a fixed solution. In good environments, it will take a few seconds to get a fixed solution. In tough conditions, it may take a little longer. Once rover gets fix status, we are all set for work.

Scroll the status tab down to see your location in the real-time.
