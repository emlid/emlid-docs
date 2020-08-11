## Overview

This guide explains how to set up your Reach receivers for PPK mapping with UAV.

!!! tip ""
    To learn more about PPK, check [How PPK works article](ppk-introduction.md) before you start.

For the workflow, you need:

* Reach RS+/RS2 base. [You can find more information about their differences here](single-multi.md)
* Reach M+/M2 rover with GNSS antenna
* Hot shoe adapter (HSA) for a camera
* Any camera that provides hot shoe access (e.g. Sony, Canon, Nikon)

!!! danger ""
    Please note that Reach RS+ can't act as a base for a Reach M2 rover as Reach M2 requires multi-frequency corrections. Still, you can use Reach RS2 as a base for Reach M+. Note that you won't get all advantages of the multi-band receiver in this case.

In this guide, we are mostly focused on the GNSS equipment part of the integration. However, you also need a UAV and a PC with a Ground control station and photogrammetric software. There are 2 main requirements for UAV:

1. The presence or ability to install a camera with a hot-shoe connector
2. Functionality allowing triggering the camera: by camera itself or by autopilot

!!! tip ""
    For PPK mapping, you need a few Ground Control Points (GCPs). To place GCP, a base and a rover are required. Also, you can use one device with a connection to an NTRIP caster or post-process a standalone log in any PPP service. You can learn more about GCPs from [the following paragraphs](#placing-ground-control-points).

## Reach M+/M2 hardware setup

### Connecting Reach M+/M2 to a camera using HSA

HSA allows Reach M+/M2 to precisely record a time mark at every moment the camera takes a photo.

!!! danger ""
    The camera requires to have a hot shoe for integration with Reach M+/M2. If you use DJI Mavic or Phantom which doesn’t provide hot-shoe access, you can always stick [to working with GCPs](#placing-ground-control-points).

To connect Reach to a camera with a hot shoe adapter use 5-pin JST-GH cable that comes with Reach M+/M2. Plug the hot shoe connector in a camera hot shoe and the JST-GH connector in the С1 port on Reach M+/M2.

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/emlid-hotshoe.jpg" style="width: 500px;"></div>

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/reach-c1.jpg" style="width: 500px;"></div>

### Camera triggering

Depending on your application, there are several ways you can trigger a camera.

!!! tip ""
    Each camera uses different ports for triggering. It might be a USB or HDMI port. Read the camera manual to find out how to trigger your camera.

    ??? note "Triggering via camera"

        Some cameras provide a Timelapse feature that allows taking a photo at regular intervals. If your camera supports this option, we recommend using it as it is the easiest and straightforward way.

    ??? note "Triggering via autopilot"

        **Triggering the camera shutter at waypoints**

        Autopilot can trigger the shutter each time the drone reaches a waypoint. If you use a flight controller based on ArduPilot, [check this article from ArduPilot docs for more details](https://ardupilot.org/copter/docs/common-camera-control-and-auto-missions-in-mission-planner.html#common-camera-control-and-auto-missions-in-mission-planner).

        **Triggering camera shutter at regular intervals**

        [Examine the article about camera shutter configurations in ArduPilot docs.](http://ardupilot.org/copter/docs/common-camera-shutter-with-servo.html)

    ??? note "Triggering via Reach"

        Reach M2/Reach M+ has a PWM output pin, that allows triggering cameras at defined intervals. Configure [Reach M+/M2](../reachview/camera-control.md) to trigger the camera. Check [Reach M+/M2](../../../specs#connectors-pinout) pinout to make a DIY cable for it.

The majority of Ground Control Station software allows and even requires a mission plan preparation before the flight. You need to configure your camera and autopilot the way it obtains images with overlaps. This is necessary because common points in adjacent images are required to create an orthogonal mosaic. We recommend the front overlap to be at least about 60% and the side – about 30%.

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/overlap.jpg" style="width: 800px;"></div>

### Antenna placement

GNSS antenna should be placed on a ground plane. Antenna ground plane should be conductive and at least 70 x 70 mm. You can read more about antenna placement for [Reach M+/M2](../../../antenna-placement). A usual metal plate should be good for this purpose.

!!! tip ""
    Helical antennas don't require a ground plane. Still, a ground plane can improve observation quality significantly.

### Isolating Reach M+/M2 from potential interference

In some cases, you might need to isolate your Reach to ensure the best logging quality. The reason is that the transmitted power of GNSS signals is rather low relative to the possible noise from other hardware components installed on your UAV. It means that the antenna signal strength might be unstable and even sometimes interrupted. Interruption and temporary signal loss on RTK receiver are called cycle slip.

To avoid cycle slips we recommend isolating Reach M+/M2 unit and connect it to the ground to eliminate interference. Also, RC components, such as radio transmitters, might affect the signal as well. Reach should be located as far as possible from them.

The effects of bad hardware setup are substantial. Poor signal quality with low SNR values, lots of cycle slips pose issues with getting fixed solutions and missing time marks. Take a look at the figures below that demonstrate examples of good (the left picture) and bad (the right one) satellite reception.

[You can read more about the signal quality assessment in this section of our docs.](../analyzing-logs/#data-assessment)

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/good-and-bad-examples.png" style="width: 800px;"></div>

!!! tip ""
    Create a topic on the [Emlid community forum](https://community.emlid.com) in case you experience any difficulties at this stage.

## Reach RS+/RS2 base setup

Check out the figure below and choose an appropriate location to place Reach RS+/RS2 base station. The basic rules are:

* Good sky angle over 30º
* Away from trees and buildings
* No electricity nearby

[Read more about requirements for base placement by following this link.](placing-the-base.md)

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/Reach-placement-correct-wrong.png" style="width: 800px;"></div>

## Configuring base and rover before the flight

### Reach M+/M2 rover settings

* Power your [Reach M+/M2](../../../power-supply) unit from an external power source or drone battery
* Access Reach M+/M2 in the ReachView app

### Reach is in hotspot mode

??? note "Connecting via Reachview app (iOS/Android device)"

	1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [Apple Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
	2. Go to Wi-Fi settings on your device
	3. Connect to Reach hotspot. It appears as **reach:XX:XX**
	4. Enter password **emlidreach**
	5. Launch ReachView app
	6. Choose Reach from the list


??? note "Connecting via a web browser (any device)"

	1. Go to Wi-Fi settings on your device
	2. Connect to Reach hotspot. It appears as **reach:XX:XX**
	3. Enter password **emlidreach**

		!!! tip "Windows OS"
			If Windows suggests you to enter the PIN from the router label to connect to the network, choose **Connect using a security key instead** option.

	4. Launch a web browser (we recommend using Chrome or Mozilla)
	5. Go to 192.168.42.1


### Reach is in client mode

??? note "Connecting via Reachview app (iOS/Android device)"

	1. Connect your mobile device to the same Wi-Fi network as Reach
	2. Scan for available Reach devices
	3. Choose Reach from the list
	
	<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/Reach-list.PNG" style="width: 800px;"></div>


??? note "Connecting via web-browser (any device)"

	1. Connect your device to the same Wi-Fi network as Reach
	2. Use ReachView app to determine the Reach IP address
	3. Launch a web browser (we recommend using Chrome or Mozilla)
	4. Go to determined Reach IP


* Go to the RTK settings and configure one of the recommended GNSS selection and update rate for time mark logging:

??? note "For Reach M+"

    |GNSS Selection|Reach M+ allowed update rates|
    |:---:|:---:|
    |GPS + GLONASS + GALILEO + SBAS + QZSS|1 Hz|
    |GPS + GLONASS + QZSS|5 Hz|
    |GPS + GALILEO|5 Hz|
    |GPS|10 Hz|


??? note "For Reach M2"

    Reach M2 tracks GPS, GLONASS, GALILEO, QZSS, and BEIDOU satellite systems. The data can be logged with 1 Hz, 5 Hz, or 10 Hz update rate.

    For a drone flight, it is better to set up the update rate to 10 Hz.    

* Enable raw data recording in the Logging tab:

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/logging.png" style="width: 800px;"></div>

!!! tip ""
    Go to the Camera control tab and try to take a photo manually. The value in the Last Time mark field should update at the moment.

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/camera_control.png" style="width: 800px;"></div>

### Reach RS+/RS2 base settings

* Turn on the Reach RS+/RS2 unit
* Access Reach RS+/RS2 in ReachView app
* Go to the RTK settings tab
* Choose the same GNSS as for Reach M+/M2 with 1 Hz update rate
* Enable raw data recording in the Logging tab


## Placing Ground Control Points

Ground Control Points (GCPs) are points with known coordinates on the ground in the area of your interests. GCPs usually help to improve and check the accuracy, get the correct scale and orientation of the map. Also, they are needed for the absolute positioning of your map in relation to the real world around it. [You can read more about absolute and relative accuracy in these docs.](../placing-the-base/#absolute-and-relative-position)

Reach provides centimeter-accurate coordinates in PPK. Also, if you place the base on a point with known coordinates, you will get the coordinates with absolute accuracy. In such a case, GCPs can help you to verify the accuracy. 

GCPs should be clearly visible on the drone's images. Make sure the mark is a contrast to its surroundings and that it's big enough. Place a survey pole with a receiver exactly in the center of the mark to take its coordinates.

Enough quantity of GCPs depends on the site area. Usually, it's 5-10 points. There are some basic rules of checkpoints placing:

* They should be allocated evenly in the area where you survey. For example, if you use 5 points, set per one for each corner and the last in the center of the area
* They must not be on the same line

Also, it's great if you have the possibility to place GCPs at the highest and lowest points on site. It helps to perform the correct flat projection.

<div style="text-align: center;"><img src="../img/reach/configuring-reach-for-mapping/GCP-placing.jpg" style="width: 800px;"></div>

It’s important to meet these requirements if you want to get the same accuracy across the entire plot.

[Follow this guide to place GCPs in RTK.](placing-gcps.md)

## Survey flight

We don't pay much attention to this step due to the differences in the drone flight settings from model to model. Please, check the manual of your drone manufacturer before the flight.

After all the configurations are done, you can proceed to flight with your drone.

!!! danger ""
    Make sure raw data logging on both Reach M+/M2 and Reach RS+/RS2 units are enabled before the flight.

When the flight is finished, you can disable logs recording. Before turning the devices off, please wait until the logs processing is done. 

You can download raw data logs from both base and rover later on. 

As a result of mapping mission with Reach you'll have the following dataset:

1. Raw log from a base
2. Raw log from a rover
3. Set of images from a drone
4. List of GCPs

Now we're ready to proceed to the next step where we prepare the dataset for further processing.

<br>

Further reading:

* [Geotagging photos with GeoSetter](geosetter-tutorial.md)

