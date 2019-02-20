Reach supports RTK-enhanced coordinates output to Edge flight controller using **ERB** (Emlid Reach Binary protocol).

Protocol description is available [here](https://files.emlid.com/ERB.pdf).

## Requirements

ERB support is included to ArduPilot starting with the following versions:

* ArduCopter 3.4
* ArduPlane  3.5.0
* APMrover   3.1



## Recommended setup

<div style="text-align: center;"><img src="../../img/reach-integration/reach-edge-connection.png" style="width: 100%;"></div>

The setup we recommend goes as follows:

* Edge with [Emlid Edge image](https://docs.emlid.com/edge/firmware-update/) (v1.3 or higher)
* Base station is a Reach or Reach RS unit connected to PC via USB
* GCS is a laptop with [QGroundControl](https://docs.emlid.com/edge/gcs-installation/#qgroundcontrol-for-edge) (v3.2.4-edge-2.2 or higher)
* Alfa Wi-Fi adapter is plugged in the laptop and connected to Edge's Wi-Fi network
* Rover Reach unit is mounted on a drone and connected to Edge via the GST-to-DF13 wire. This connection type will solve three problems at once: power Reach, allow ArduPilot to pass base corrections and allow Reach to pass RTK solution back.

The following guide will show how to configure both Edge and Reach to work in this setup. If you wish alter to this workflow, it should be fairly easy to do so, as every part of the system is independent of others.


## Connecting Reach to Edge

Connect Reach's upper DF13 port with Edge's **SER1-I2C** port.

<div style="text-align: center;"><img src="../../img/reach-integration/edge-reach-connection.png" style="width: 100%;"></div>

## Connecting Reach M+ to Edge

Connect Reach's JST-GH port with Edge's **SER1-I2C** port.

<div style="text-align: center;"><img src="../../img/reach-integration/edge-reachm.png" style="width: 100%;"></div>

## Configuring Reach to work with Edge

### Base setup

Configure Base mode

* Select `Serial` connection type
* Select `USB-to-PC` device
* Choose the desired baud rate (38400 for default)
* Hit `Apply` button to save settings

<div style="text-align: center;"><img src="../../img/reach-integration/reach-base-mode.png" style="width: 100%;"></div>

Connect base Reach to PC via USB-microUSB cable.

### Rover setup

!!! note
    The serial connection is used to accept base corrections and send solution at the same time.


Start with configuration base correction input:

* Select `Correction input` tab
* Select `Serial`
* Choose `UART` as the device
* Choose the desired baud rate (38400 for default)
* Choose `RTCM3` as base corrections format
* Hit `Apply` button to save settings

<div style="text-align: center;"><img src="../../img/reach-integration/reach-correction-in.png" style="width: 100%;"></div>

Now configure position output:

* Select `Position output` tab
* Select `Serial`
* Choose `UART` as the device
* Choose the desired baud rate (38400 for default)
* Choose `ERB` as position output format
* Hit `Apply` button to save settings

<div style="text-align: center;"><img src="../../img/reach-integration/reach-position-out.png" style="width: 100%;"></div>

!!! note
    **ERB** is a custom protocol, used to send location data to the autopilot.

### Configuring ArduPilot to accept Reach solution

ArduPilot configuration will require setting GPS parameters via QGroundControl:

* Open QGroundControl
* Go to `Vehicle Setup` menu
* Open `Parameters` list on the left.

!!! tip
    To find the desired parameter more quickly, use a search box on top of the list.

* Set **GPS_TYPE2** parameter to "AUTO". This will enable the second GPS input.

<div style="text-align: center;"><img src="../../img/reach-integration/qgc-gps-type.png" style="width: 100%;"></div>

* Then press `Tools` button on the left upper corner and select `Reboot Vehicle`

<div style="text-align: center;"><img src="../../img/reach-integration/qgc-reboot.png" style="width: 100%;"></div>


After everything is done vehicle GPS switches to RTK mode. The new mode is displayed in the GPS status icon

<div style="text-align: center;"><img src="../../img/reach-integration/gps-status.png" style="width: 100%;"></div>
