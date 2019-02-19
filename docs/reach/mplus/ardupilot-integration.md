Since ReachView version **0.3.0** Reach supports RTK-enhanced coordinates output to Navio and Pixhawk autopilots. To make this possible, we implemented a custom gps protocol we call **ERB**(Emlid Reach Binary protocol).

Here is a demo video with our results:
<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/oq9H19ikAdM" frameborder="0" allowfullscreen></iframe></div>

## ERB Protocol specification

Protocol description is available [here](https://files.emlid.com/ERB.pdf).

## Requirements

ERB support is included to ArduPilot starting with the following versions:

* ArduCopter 3.4
* ArduPlane  3.5.0
* APMrover   3.1

## Recommended setup

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/reachm-ardupilot-scheme.png" style="width: 800px;"></div>

The setup we recommend goes as follows:

* Navio or Pixhawk with the ArduPilot firmware (not less version 3.4.0 for ArduCopter, 3.6.0 for ArduPlane and 3.0.1 for ArduRover). It's preferable to use the last stable version
* Base stations is a Reach RS/RS+ unit in Wi-Fi AP mode, configured as a TCP server
* GCS is a laptop with Mission Planner(version 1.3.35 and higher), connected to the base Reach Wi-Fi hosted network
* Telemetry connection via a serial radio
* Rover Reach M+ unit is mounted on a drone and connected to Navio or Pixhawk via the 6P-to-6P wire. This connection type will solve three problems at once: power Reach, allow ArduPilot board to pass base corrections and allow Reach to pass RTK solution back.

The following guide will show how to configure both Navio or Pixhawk and Reach to work in this setup. If you wish alter to this workflow, it should be fairly easy to do so, as every part of the system is independent of others.




## Connecting Reach M+ to Pixhawk

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/pixhawk-reachm-radio.png" style="width: 500px;"></div>

To provide RTK solution to Pixhawk, Reach needs to be connected via a serial port. You can do that by plugging the serial cable into Reach's JST-GH port and Pixhawk's **"Serial 4/5"** connector.

!!! note ""
	It's recommended to supply Reach M+ from an external power source. Pixhawk may not provide enough power for Reach in some cases.

## Connecting Reach M+ to Navio over UART

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/navio2-reachm.png" style="width: 500px;"></div>

Connect Reach's JST-GH port with Navio's **UART** port.

## Connecting Reach M+ to Navio over USB

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/navio2-reachm-usb.jpg" style="width: 500px;"></div>

Connect Reach's Micro-USB port with RPi's **USB** port.

## Connecting Reach M+ to Edge

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/edge-reachm.png" style="width: 500px"></div>

Connect Reach's JST-GH port with Edge's SER1-I2C port. Edge and Reach M+ integration guide may be found in Edge docs: [Reach integration](https://docs.emlid.com/edge/tutorials/reach-integration/).

## Configuring Reach to work with ArduPilot

### Rover setup

!!! note
    The serial connection is used to accept base corrections and send solution at the same time.

Start with configuration base correction input:

* Select **Correction input** tab
* Select **Serial**
* Choose **UART** or **USB-to-PC** as the device
* Choose the desired baud rate(38400 for default)
* Choose **RTCM3** as base corrections format
* Hit **Apply** button to save settings

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/reach-base-correction-input.png" style="width: 100%;"></div>

Now configure position output:

* Select **Position output** tab
* Select **Serial**
* Choose **UART** or **USB-to-PC** as the device
* Choose the desired baud rate(38400 for default)
* Choose **ERB** as position output format
* Hit **Apply** button button to save settings

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/reach-position-output.png" style="width: 100%;"></div>

!!! note
	**ERB** is a custom protocol, used to send location data to the autopilot.


### Setting up a correction link

Reach supports a number of ways to accept [base corrections](common/reachview/correction-input/#base-correction), including the popular in UAV area serial radios. However, having a separate radio link for base corrections only is highly ineffective.

To solve this, you can use the telemetry radio as a carrier for RTK corrections. GCS can pass these corrections to the autopilot with a feature called **GPS inject**. This funcionality is available in **Mission planner** only.

### Configuring radio for embedding corrections into telemetry

With default settings radio telemetry is not optimised for sending RTK corrections. This may cause correction data delivery delays and even loss. These slips will deteriorate RTK solution quality, so we need to minimize them.

!!! note
    Radio configuration is done with telemetry disconnected.

To change radio settings, make sure **Mavlink connection is disabled**. Then, go to **Initial setup** menu, and select **Sik Radio** in the side menu. Click **Load settings** and wait for the parameters of both radios to load.

You need to clear the field **ECC** and choose **Raw Data** in the Mavlink select field.

After this, click **Save settings**. If your radio's firmware is outdated, update with **Update Firmware(Local)**.


<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-radio-setup.png" style="width: 800px;"></div>

### Configuring ArduPilot to accept Reach solution

!!! attention
    It is recommended to use Reach as a second GPS unit only.

For launch ArduPilot on Navio add to your starting command one of the following arguments:

* For UART connection
```bash
-E /dev/ttyAMA0
```

* For USB connection
```bash
-E /dev/ttyACM0
```
This will enable to use Reach as external GPS.

ArduPilot configuration will require setting some parameters via Mission planner. After connecting, go to **CONFIG/TUNING** menu, then click **Full parameters list** on the left. To find the desired parameter more quickly, use a search box on the right(highlighted in red).

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-full-parameter-list.png" style="width: 800px;"></div>

Start with settings **GPS_TYPE2** parameter to **"1"** - AUTO. This will enable the second GPS input.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-type2-parameter.png" style="width: 800px;"></div>

Next, set **SERIAL4_BAUD** parameter to the same baud rate, as chosen in ReachView solution output. Note the options corresponding to the different baud rates.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-serial4-baud-parameter.png" style="width: 800px;"></div>

Set **GPS_AUTO_SWITCH** to **"1"** - Enabled. Autopilot will automatically switch between the two GPS receivers, picking the one with better solution.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-auto-switch-parameter.png" style="width: 800px;"></div>

Finally, set **GPS_INJECT_TO** parameter to **"1"**. **"1"** here stands for the second GPS input. If you configured Reach as the first input, set this parameter to **"0"**.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-inject-to-parameter.png" style="width: 800px;"></div>

### Configuring Mission planner to inject RTK corrections into telemetry

To enable and configure GPS inject options in Mission planner press **"ctrl+F"** button combination. This will open a window with advanced GCS settings. Click **Inject GPS** button on the right.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-inject-settings.png" style="width: 70%;"></div>

In the new window, choose parameters for base connection. Reach in base mode supports TCP and serial modes. For the sake of this example, **let's assume base corrections are coming from another Reach in base TCP server mode**. This is a setup we usually use in our test flights.

### Base setup

Let's configure our Reach device:

* Open **Base mode** tab on Reach device
* Choose TCP in Correction output options
* Set **Server** in Role field
* Set 9000 as Port
* Hit **Apply** button button to save settings

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/reach-base-mode.png" style="width: 100%;"></div>

In order to connect, choose TCP client mode in Mission Planner.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-inject-connection-type-new.png" style="width: 80%;"></div>

Enter Base Reach's IP address.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-inject-ip-new.png" style="width: 60%;"></div>

And port the server port number.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-inject-port-new.png" style="width: 60%;"></div>

Finally, check the corrections are coming in.

<div style="text-align: center;"><img src="../img/reachm-plus/ardupilot-integration/mp-gps-inject-connected-new.png" style="width: 70%;"></div>
