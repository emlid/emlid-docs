# Glossary

## Absolute positioning

Absolute positioning shows your actual global coordinates relative to the Earth’s surface. Absolute positioning is a key to RTK surveys where you need absolute geographical accuracy (e.g, mapping, surveying the borders of the property, etc). In this case, your base absolute position is crucial for high accuracy results. 

## Accuracy

Accuracy is the closeness of the measurements to a specific value. In surveying, accuracy refers to whether the coordinates you collected are true relative to the global coordinates. Not to be confused with [Precision](#precision).

## Age of differential

Age of differential is the measure of how old are the corrections your receiver is getting. It is calculated by subtracting the time when the correction message has been generated from the current receiver time. The standard Age of Differential for RTK is normally 1-2 seconds.

## Antenna Phase Center

Antenna Phase Center could be referred to as the antenna’s source of radiation. All GNSS measurements referred to the phase center. The phase center does not correspond to the physical center of the antenna and its real position depends on the direction of the coming radio signal. In addition, every band has its own phase center respectively.

## Antenna Reference Point

The antenna reference point is the center point on the bottom of the receiver. It is used for calculation of the antenna height.

## AR ratio

This is a result of the ratio test performed on the potential “Fix” solution, it shows how many times is the best solution better than the next one. If this number is more than 3, Reach will consider RTK solution Fixed.

This parameter corresponds to single-band Reach devices only (Reach RS/RS+, Reach Module/M+).

## Base

Base is one of the receivers that act as a reference station in RTK or PPK scenarios. It is a static unit with the determined coordinates that sends corrections to the moving unit or [rover](#rover). If the base is set over the known point, it provides absolute accuracy.

## Base Correction log

This log contains the corrections from the base station in RTCM3 format.

## Baseline

Baseline is the distance between a rover and a base. If the baseline is bigger than recommended, the solution will be less accurate, the fix time will be longer or it won't be calculated at all.

## BeiDou

BeiDou is a Chinese navigation system. Back in 2000, BeiDou-1 was only covering China. Then, in 2012, BeiDou-2 began covering the Asia-Pacific region. Since 2015, BeiDou offers global coverage. We recommend using this system if you are located in the Asia-Pacific region.

## Client mode

The client mode means that Reach is connected to an external Wi-Fi network.

## Continuous

Continuous is a strategy for solving the ambiguities in RTK and PPK. In this case, ambiguities are resolved epoch by epoch. Less stable than [Fix-and-Hold](#fix-and-hold), but no risk of holding a false fix.

## Coordinate system

Coordinate system is a coordinate-based local, regional or global system used to locate geographical entities. A spatial reference system defines a specific map projection, as well as transformations between different spatial reference systems.

## Correction input

This is the part of the rover's settings that is responsible for configuring the acceptance of the corrections. Using the correction input configuration in the [ReachView app](#reachview), you can choose the way your rover receives the corrections: via [Serial](#serial-port-uart-usb-rs-232), [TCP](#tcp), [NTRIP](#ntrip), Bluetooth, or [LoRa](#lora-radio). Reach receivers support the correction input in [RTCM3](#rtcm3) format.

## Corrections

The corrections are the data that is used to eliminate ionospheric and tropospheric delays, and satellite clock errors. The static base transmits corrections to the moving rover in the RTK scenario.

## CORS

Continuously Operating Reference Stations or CORS network is the network of the static stations that provide exact GNSS data (carrier phase, code range, etc) and corrections as well. Surveyors can access this information to increase the accuracy of their post-processed survey data or to work in RTK on site.

## Dilution of Precision or DOP

Dilution of Precision or DOP is the term used to evaluate the geometrical position of the satellites relative to the receiver. When the satellites are too close to each other in the field of view, it means the satellite geometry is weak (a high DOP value). If the distance between the satellites is sufficient and they are allocated evenly and cover more space, the geometry is considered strong, therefore, the DOP value is low. The lower the DOP, the more accurate your data is. A good DOP value is considered to be below 2.

## Elevation mask

Elevation mask can be configured in RTK settings in the ReachView app. Satellites lower than set elevation will be excluded from the computation. The default setting is 15 degrees. Usually, satellites with a lower elevation provide too noisy measurements as the signal passes through the most atmosphere. 

## ENU

One of the formats for position output available for Reach devices. Simple text protocol for East, North and UP components of the baseline as well as solution status.

## ERB

One of the formats for position output available for Reach devices. Used for communication to Ardupilot. ERB states for Emlid Reach Binary protocol.

## Fix-and-Hold

Fix-and-Hold is a strategy for solving the ambiguities in RTK and PPK. After the first ambiguity fix holds them constrained. Fix is more stable but in case first initialization was not correct it will take longer to recover and initialize correctly. You can think of it as if Fix had inertia. 

## Full System report

A full system report is a tool used to facilitate issues reports. It comes in ZIP archive, and contains system logs and technical details of your device as well as some sensitive information like your NTRIP credentials or network passwords. That is why we do not recommend sharing the report publicly. These are used to debug complicated cases in support. 

## Galileo

Galileo is a European satellite navigation system. It first started operating in 2011 and now has global coverage.

## Ground Control Point or GCP

Ground Control Point is a point on a surface with known coordinates. The GCPs are actively used in aerial mapping and photogrammetry. The surveyors set GCPs over the area, mark them so they can be visible from the drone. The GCPs are then surveyed to find their exact coordinates and used as reference points for future data processing.

## GIS

Geographic Information System or GIS is a system for collecting, storing, analyzing, and graphically visualizing spatial data and related information about required objects.

## GLONASS

GLONASS is a global satellite navigation system. It was created as an alternative to GPS in Soviet Union and first launched in 1982. 

## GLONASS AR mode

A processing parameter enabling to turn on and off the ambiguity resolution for the GLONASS signal separately. Contrary to GPS, all GLONASS satellites transmit on different frequencies, which results in Inter Channel Biases (ICB) that are unique for each receiver model.

Reach devices can correct GLONASS ICBs, allowing for GLONASS AR with non-Reach bases such as NTRIP casters. The general recommendation is to always have GLONASS AR set to on.

This parameter corresponds to single-band Reach devices only (Reach RS/RS+, Reach Module/M+).

## GNSS

Global Navigation Satellite System or GNSS is a system designed to determine the location (geographical coordinates) of land, water, and air objects. Such systems consist of space equipment, a ground segment called control systems, and individual receivers. The operation of GNSS is based on measuring the distance from the antenna on the object (receiver) to satellites whose position is known with great accuracy. 

## GPS

Global Positioning System or GPS is a global satellite navigation system that measures distance, time, and location in the WGS 84 world coordinate system. The system was developed in 1978, and is operated by the United States.

## Ground plane

A ground plane is a conductive plate providing insulation for the antenna. It may be a piece of metal, a roof of a car, a metal roof of a building, and etc. It is recommended to use at least a 70x70 mm ground plane.

## Hot-shoe adapter

Hot-shoe is a point on the top of a camera that is used to attach accessories or other equipment to the camera. Using hot-shoe adapter, you can connect your camera to Reach M+/M2 for UAV mapping. 

## Hotspot mode

The hotspot mode means that the Reach is broadcasting its own Wi-Fi network.

## Kinematic Positioning

Kinematic positioning is one of two positioning modes. It implies that the rover is moving during the positioning process. 

## LLH

One of the formats for position output available for Reach devices. Simple text protocol for Latitude, Longitude, and Height as well as solution status.

## LoRa radio

Long Range or LoRa radio is used for Reach receivers to send or receive corrections without an Internet connection. Reach RS+/RS2 is equipped with internal Lora radio. Reach M+/M2 has external LoRa radio available: you can connect it via S2 port. The radio works only one way: it either sends correction or receives them. Using LoRa modulation it is possible to hit up to 19km (11.8 miles) in line of sight. 

## Mock location

Mock location feature of Android devices enables you to manually change the location of your device to any other place. In the case of Reach devices, it enables the GPS collector apps to get the GPS observations directly from the receiver instead of the internal GPS of the unit.

## Mount Point

Mount point is the physical base station that provides you with NTRIP corrections.

## Multi-band receiver

A multi-band receiver is a receiver that can accept signals from the satellite on more than one frequency band. It means the receiver takes less time to establish the first fix solution, has a longer baseline, and has more chances to maintain fix solution in the blocked sky view conditions. 

## Multipath

Multipath is an effect occurring when the GPS signal is deflected from the obstacles, so the GNSS receiver detects signals not only directly from the satellites but also from the local objects. Multipath effect results in an error in pseudo-range measurements and thus affects the positional accuracy.

## Night mode

Night mode allows you to turn off the LEDs until the next reboot of the Reach device.

## NMEA 0183

One of the formats for position output available for Reach devices. The most popular standard in the industry. Supported messages: GNRMC, GNGGA, GPGSA, GLGSA, GAGSA, GPGSV, GLGSV, GAGSV, GNGST, GNVTG, GNZDA.

## NTRIP

The Networked Transport of RTCM via Internet Protocol or NTRIP network is an alternative source of corrections. NTRIP allows your rover to accept corrections over the Internet with no need for the second local receiver acting as a base. A reference station collects data, then sends it to NTRIP caster, where it is retransmitted through the Internet port to the client rover connected via a particular port and authorized.

## Point cloud

Point cloud is a set of vertexes in a three-dimensional coordinate system. Point clouds are created with 3D scanners and are used in photogrammetry and 3D-modeling. 

## Point Collection

Point collection is a feature in ReachView app that allows you to find the exact coordinates of the point. The receiver determines the coordinates (x, y, z) of a ground point and records it to your project for further processing .

## Point Stakeout

Point stakeout is a feature in ReachView app that allows finding points with known coordinates on the site. 

## Pole Height

When preparing for point collection, configure the height of your survey pole in ReachView. It will help the app to automatically calculate the antenna height. 

## Position log

This log contains positional information. Reach devices can log their position in [LLH](#llh), [XYZ](#xyz), [ENU](#enu), [NMEA](#nmea-0183), and [ERB](#erb) formats.

## Position output

Reach devices can send the position data to third-party GIS apps and external devices including tractors, drones, robots, and more. The position could be out shared via [Serial](#serial-port-uart-usb-rs-232), [TCP](#tcp), and Bluetooth. Various applications require different formats of the positional data, that is why Reach outputs its position in [LLH](#llh), [XYZ](#xyz), [ENU](#enu), [NMEA](#nmea-0183), and [ERB](#erb).

## PPK

Post-Processed Kinematic is one of the techniques used for highly accurate surveys. Same as in [RTK](#rtk), one needs two units: a [base](#base) and a [rover](#rover). The core difference is that in PPK scenario there is no need for a real-time connection between two units. Base and rover record logs separately, and these logs are processed together later using specific post-processing software, for example, RTKLib.

## PPP

Precise Point Positioning or PPP is a technique used for determining the centimeter-level accurate coordinates of the point. The receiver put over a point is recording data for a certain period. Then this data is sent to the PPP services. 

## Precision

Precision is the closeness of two or more measurements to each other. Precision means that the coordinates you collected are true relatively to another object. In this case, you do not need exact georeferencing coordinates of the points, you only need to know that the collected points are, say, situated on the same distance from each other. Not to be confused with [Accuracy](#accuracy).

## Raw data log

A raw data log contains GNSS observations from the receiver without the calculation of accurate coordinates. It can be recorded in UBX or directly in industry-standard RINEX format.

## ReachView

ReachView is the mobile app created by Emlid. It is used to control and configure the Reach receivers, create projects, collect points, etc. 

## Relative positioning

Relative positioning shows your coordinates relatively to another reference object. The base sends information about its absolute position to the rover. Using this information, the rover determines its position relative to the base with centimeter accuracy. 

## RINEX

RINEX is a standard raw-data format that allows storing satellite observations and navigational data measurements made by the receiver. It also allows the post-processing of the received data by various applications from different manufacturers of receivers and programs.

## RMS

The square root of the average of the squared error. The RMS calculations are used to evaluate the accuracy of the position measurement. A horizontal or vertical delusion of precision multiplied by three RMS could give the horizontal or vertical precision value respectively.

## Rover

Rover is one of the two GNSS receivers that is used for collecting data in RTK or PPK scenarios. Rover is a moving unit: the surveyor uses rover to record the points, while rover receives the corrections from the static [base](#base).

## RTCM3

RTCM3 is an industry standard format for correction output. 

## RTK

Real-Time Kinematic or RTK is one of the techniques used to improve the accuracy of the data collected from the satellites by the receiver. For RTK one needs two receivers: a [base](#base) and a [rover](#rover). The base sends corrections to the moving rover during data collection. 

## RTKCONV

RTKCONV is a tool in RTKLIB that converts UBX raw data or RTCM3 base correction data from a receiver to [RINEX](#rinex) format. 

## RTKLIB

RTKLIB is an open-source program package for standard and precise positioning with GNSS. It is used for PPK data processing. Works with signals from GPS, GLONASS, Galileo, QZSS, BeiDou, and SBAS. Emlid produces the version of RTKLib tailored for Reach products.

## RTKPLOT

RTKPLOT is a tool in RTKLIB that allows viewing and plotting the position solutions from RTKPOST as well as observation data from RTKCONV.

## RTKPOST

RTKPOST is a tool for post-processing raw logs in RTKLIB. The result is stored in the position solution file in LLH WGS 84 – POS file. In this file, we will get centimeter-accurate track of the receiver.

## Serial Port (UART, USB, RS-232)

A serial communication interface in which the information transfers in or out sequentially one bit at a time. That kind of communication could be realized via various devices like UART, USB, or RS-232. Reach receivers can use a serial port to exchange the position and correction data with 3rd party devices.

## Signal-to-noise ratio

Signal-to-Noise Ratio or SNR is the primary indicator of how good the reception is. The value is equal to the ratio of the power of the useful signal to the noise power. You can find the SNR indicator on the main screen of the ReachView app. When the SNR of a satellite is over 45, it will be marked green. Grey bars indicate SNR of the base station. The more satellites are in a green zone, the more precise your measurements are and the faster your ambiguity resolution is.

## Simple System report

A Simple System report is a tool used to facilitate issues reports. It provides information about the ReachView version, configurations, and network in a plain text format. 

## Single-band receiver

A Single-band receiver is a device that accepts signals from the satellite on one frequency band. It has the same level of accuracy as the multi-band one. Single-band receiver has shorter baseline in comparison to multi-band, and might not even find fix solution in blocked sky view conditions. 

## SNR mask

Signal-to-Noise ratio mask or SNR mask is a tool that filters the satellites used for the fix solution. Satellites with low SNR will be excluded from the computation. The default setting in ReachVIew app is 35.

## Solution status (fix, float, single)

Solution status defines the precision that can be achieved at the moment. There are three solution statuses you can see when working with Reach devices. 

**Fix** solution means that positioning is relative to the base and the integer ambiguity is resolved. Precision in standalone mode is centimeter-level. 

**Float** means that base corrections are now taken into consideration and positioning is relative to base coordinates, but the integer ambiguity is not resolved. Precision in float mode is submeter-level.

**Single** means that the rover has found a solution relying on itself with no base corrections applied. Configuring positioning mode to Single will also result in this status. Precision in standalone mode is on meters-level.

## Static Positioning

Static positioning is one of the positioning modes. It assumes that the Reach rover is static. Constraining the system helps to resolve ambiguities faster as well as produce measurements with higher precision.

## TCP

Transmission Control Protocol or TCP is one of the main Internet data transfer protocols designed to control data transfer. Typical scenario for using TCP is sending correction data to an application on the same network or to a server with public IP.

## Time mark

The time mark function verifies the exact moment when the camera takes a photo. After the flight, you can process the raw logs from the base and a rover to get an «*_events.pos» file. This file includes information about the time and coordinates of each photo. You can use geotagging software to write this information to the photos' EXIF data.

## UBX

UBX is the GNSS raw data format. The UBX protocol is a u-blox proprietary binary protocol that outputs in hexadecimal format.

## Update rate

The update rate is a value that shows how frequently the receiver calculates and reports its position. For Reach receivers, we recommend having 1 Hz update rate on the base and 5 Hz on the rover.

## VRS

Virtual Reference Station or VRS is a useful tool for long baselines. It is an imaginary, unoccupied reference station generated nearby the RTK user. The rover sends data back to the NTRIP caster. NTRIP allows the uniting of the data from your rover and the data from dense NTRIP bases and models a virtual base next to you. 

## WGS 84

World Geodetic System 1984 or WGS 84 is the global system of geodetic parameters of the Earth, including the system of geocentric coordinates. It was accepted in 1984 and defines coordinates relative to the Earth's center of mass, with an error of less than 2 cm.

## XYZ

One of the formats for position output available for Reach devices. Simple text protocol for X, Y, Z ECEF coordinates as well as solution status.