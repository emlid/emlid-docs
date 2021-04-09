## Correction output

<p style="text-align:center"><img src="../img/reachview/base-mode/output.png" style="width: 800px;"/></p>

Reach outputs correction in industry standard RTCM3 format. Correction data can be sent via Serial, TCP, NTRIP or LoRa.

### Serial
Serial port connection is available through several hardware connection options. All of them support the following baud rates: 9600, 19200, 38400, 57600, 115200, 230400.

#### UART
Corresponds to the lower JST-GH port (S1) on Reach M2. Common way to connect to radio to send correction data.

#### USB-to-PC
When connected over USB to a PC Reach will show up as several devices, one of them will be a serial port. You can use this serial port to send correction data to the PC.

#### USB OTG
Use a micro-USB OTG cable to connect USB accessories. In this mode only USB devices that emulate a serial port could be used. Example of popular chips that are supported: FT232, CP2102. There are numerous devices built on these chips that will provide you a TTL UART or RS232 port. 

### NTRIP
NTRIP is industry standard way of transferring GNSS corrections over Internet, with ReachView you can use any public service or your own private caster. NTRIP does not support point-to-point communication e.g. you can not use it to transfer corrections from one Reach to another directly. In NTRIP terminology there are servers, clients and caster. Server sends correction to a caster and clients can receive them by connecting to that caster.

In order to send correction to NTRIP caster you need to know: 

- IP address or domain name of the caster
- Port
- Password
- Mount point

When connecting via NTRIP in base mode Reach acts as a NTRIP server.

### TCP
Typical scenario for using TCP is sending correction data to an application on the same network or to a server with public IP. 

TCP supports two roles:

#### Server
You need to specify port and after that clients will be able to connect to this device on it’s IP address. Many clients can be connected to the same server.
#### Client
You need to specify IP address of the server and port number.

If ReachView does not allow to set a certain port number it means that it is reserved for internal use.

### LoRa Radio
Reach M2 use external LoRa radio module for receiving or sending corrections. It can be connected via USB or S1/S2 port. The radio works only in one way, it could either be configured to send corrections (on base) or to receive them (on rover). Using LoRa modulation it is possible to hit up to 8 km in line of sight or a few km in urban areas with just 20 dBm power output. As long as frequency and air rate settings match an unlimited number of rovers can listen for correction from the same base.

The lower the air rate, the longer the working distance will be. Depending on your RTCM3 messages selection ReachView will automatically block insufficient air rates. Disable correction messages or reduce rate in order to unlock lower air rates. Air rate on transmitting Reach and on receiving must match.

Make sure to select appropriate output power and frequency according to your local regulations.

### Bluetooth
You can use Bluetooth for correction output. Note that you can’t set both position output and base correction output to Bluetooth at the same time.

## RTCM3 messages

The minimal subset that is required for RTK to function is 1074 message for 1Hz with GPS observations and 1006 message for 0.1Hz with base station antenna position. Enabling more messages or higher rates requires higher connection bandwidth.

| RTCM3 messages                       | Message type                         |
|:------------------------------------:|:------------------------------------:|
| **Minimal required messages**                                              ||
| 1006                                 | ARP station coordinate               |
| 1074                                 | GPS MSM4                             |
| **Optional messages for other GNSS**                                       ||
| 1084                                 | GLONASS MSM4                         |
| 1094                                 | Galileo MSM4                         |
| 1124                                 | BeiDou MSM4                          |
| **Messages for legacy third-party rovers**                              ||
| 1004                                 | GPS                                  |
| 1008                                 | Antenna descriptor and Serial Number |
| 1012                                 | GLONASS                              |
| 1033                                 | Receiver and antenna descriptors     |

Here is some information about each message from RTCM STANDARD 10403.3<sup>[1](#myfootnote1)</sup>:

- **Message Type 1006** provides the earth-centered, earth-fixed (ECEF) coordinates of the antenna reference point (ARP) for a stationary reference station and the height of the ARP above a survey monument. It is the mandatory message to turn on.

- **Messages 1074 (GPS), 1084(GLONASS), 1094 (Galileo), 1124 (BeiDou)** are MSM4 (Multiple Signal Messages). MSM4 messages provide the same information for each GNSS system: pseudorange, phase-range, SNR. That means that you should turn on only one message of the choosen system to get all data about it. It is recommended to keep enabled at least GPS 1074 message.

- **Messages** **1004 (GPS)** and **1012 (GLONASS)** provide the same information for both GNSS systems: pseudorange, phase-range, SNR for L1 and L2 signals.

- **Messages 1008** and **1033** provide antenna data.

### Messages for Reach rovers

When using another Reach as a rover, pick the following messages:

* 1006 ARP Station Coordinates, 0.1 Hz
* 1074 GPS MSM4, 1 Hz
* 1084 GLONASS MSM4, 1 Hz
* 1094 Galileo MSM4, 1 Hz
* 1124 BeiDou MSM4, 1 Hz

!!! note ""
    Minimal required messages are 1006 and 1074.

### Messages for legacy third-party rovers

When using Reach RS2 as a base for legacy third-party receivers, pick the following messages:

* 1006 ARP Station Coordinates, 0.1 Hz
* 1008 Antenna descriptor and Serial Number, 0.1 Hz
* 1004 GPS, 1 Hz
* 1012 GLONASS, 1 Hz

!!! note ""
    Minimal required messages are 1006, 1008, and 1004.

!!! danger ""
    Always set the base update rate in the *RTK* settings at 1 Hz before turning any of the messages on.

## Base position


!!! tip ""
    [Check the Placing the base guide](https://docs.emlid.com/reachrs2/common/tutorials/placing-the-base/) to learn about different ways to set up your base.  

<p style="text-align:center"><img src="../img/reachview/base-mode/position.jpg" style="width: 800px;"/></p>

There are two main options how to specify base station position. Note that RTK positioning is relative to the base station, so any inaccuracy in it’s position will result in a constant shift of rover coordinates. For many applications it is not critical and averaged single coordinate of the base could be used. If your application requires absolute accuracy for rover position an accurate  base coordinate must be entered.

### Manual
In this mode you supply an a priori known coordinate by locating the unit above surveyed point. Coordinate has to be supplied in ECEF XYZ or in WGS84 Latitude and Longitude and WGS84 ellipsoid height. Antenna height offset is entered at this stage as well, offset is limited to 6.5535 m by the RTCM message.

You can change position format in the top right corner of Base coordinates frame.

<p style="text-align:center"><img src="../img/reachview/base-mode/manual.jpg" style="width: 800px;"/></p>

### Average 
By default Reach will average base position every time it starts. This feature significantly simplifies initial setup in a new location, however it will not provide an accurate absolute coordinate.

ReachView has a unique feature that allows it to determine base station position while working as a rover from another base. This is done by obtaining RTK Fixed solution, averaging it over a period of time and this way obtaining an accurate position for the base. A typical scenario would involve setting up a local base station by determining its coordinate from NTRIP and then broadcasting correction locally, thus reducing the baseline for rovers and improving positioning performance.

If the reference station is too far away it is possible to average float and still improve the accuracy of the position.

In case no correction is available when setting up base or absolute accuracy is not required averaged single coordinates could be used.

**Save averaged position to manual**  
After you have successfully obtained averaged position you might want to save it for future use. Click on the “save coordinates” icon and position will be saved as if it was entered in manual mode. Now every time Reach starts it will broadcast this position in correction messages.

**Repeat averaging**  
If you would like to restart base position averaging process you can click on “repeat averaging” icon. This is especially useful in a situation when you accidentally moved Reach during averaging.

<p style="font-size:70%;"><a name="myfootnote1">1</a>: Radio Technical Commission for Maritime Services. 2016. RTCM STANDARD 10403.3 DIFFERENTIAL GNSS (GLOBAL NAVIGATION SATELLITE SYSTEMS) SERVICES – VERSION 3. Virginia: Radio Technical Commission for Maritime Services, pp. 108-262</p>


