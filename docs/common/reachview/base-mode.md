## Correction output

<p style="text-align:center"><img src="../img/reachview/base_mode/output.png" style="width: 800px;"/></p>

Reach outputs correction in industry standard RTCM3 format. Correction data can be sent via Serial, TCP, NTRIP or LoRa for Reach RS.

### Serial
Serial port connection is available through several hardware connection options. All of them support following baud rates: 4800, 9600, 14400, 19200, 28800, 38400, 56000, 57600, 115200, 128000, 153600, 230400, 256000, 460800, 921600

#### UART
Corresponds to TTL UART on Reach module or to RS232 port on Reach RS extension connector. Common way to connect to radio to send correction data.

#### USB-to-PC
When connected over USB to a PC Reach will show up as several devices, one of them will be a serial port. You can use this serial port to send correction data to the PC.

#### USB OTG
Use a micro-USB OTG cable to connect USB accessories. In this mode only USB devices that emulate a serial port could be used. Example of popular chips that are supported: FT232, CP2102. There are numerous devices built on these chips that will provide you a TTL UART or RS232 port. 

### NTRIP
NTRIP is industry standard way of transferring GNSS corrections over Internet, with ReachView you can use any public service or your own private caster. NTRIP does not support point-to-point communication e.g. you can not use it to transfer corrections from one Reach to another directly. In NTRIP terminology there are servers, clients and caster. Server sends correction to a caster and clients can receive them by connecting to that caster.

In order to send correction to NTRIP caster you need to know: 

- IP address or domain name of the caster
- Port
- Username
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

### LoRa Radio (RS only)
Reach RS has internal LoRa radio which is used for receiving or sending corrections. The radio works only in one way, it could either be configured to send corrections (on base) or to receive them (on rover). Using LoRa modulation it is possible to hit up to 19km in line of sight or a few km in urban areas with just 20 dBm power output. As long as frequency and air rate settings match an unlimited number of rovers can listen for correction from the same base.

The lower the air rate, the longer the working distance will be. Depending on your RTCM3 messages selection ReachView will automatically block insufficient air rates. Disable correction messages or reduce rate in order to unlock lower air rates. Air rate on transmitting Reach RS and on receiving must match.

Make sure to select appropriate output power and frequency according to your local regulations.

## RTCM3 messages

<p style="text-align:center"><img src="../img/reachview/base_mode/messages.png" style="width: 800px;"/></p>



|  RTCM3 messages    |  Minimal required messages  |    @    |
|------|-----------------------------|---------|
| 1002 |    GPS L1 observations      |  1 Hz   |
| 1006 |    ARP station coordinate   | 0.1 Hz  |



|   RTCM3 messages   | Optional messages for other GNSS systems |
|------|------------------------------------------|
| 1010 |         GLONASS L1 observation           |
| 1097 |			  GALILEO MSM				  |
| 1107 |              SBAS MSM                    |
| 1117 |              QZSS MSM                    |
| 1127 |              BeiDou MSM                  |



|  RTCM3 messages    | Specific messages for not-typical applications |
|------|------------------------------------------------|
| 1008 |                  Antenna type                  |
| 1019 |              GPS Ephemeris                     |
| 1020 |              GLONASS Ephemeris                 |


The minimal subset that is required for RTK to function is 1002 for GPS observation and 1006 for base station position. Enabling more messages or higher rates requires higher connection bandwidth.

Here is an estimation of bps when messages are configured at 1 Hz:

|   RTCM3 messages   | Data rate, bps |
|--------------------|----------------|
| 1002 		         |      156       |
| 1006	  			 |		21		  |
| 1008				 |		68		  |
| 1010				 |		126.125   |
| 1019				 |		976		  |
| 1020				 |		540		  |
| 1097				 |		754		  |
| 1107				 |		520		  |
| 1117				 |		520		  |
| 1127				 |		1573	  |


!!! tip
	Remember, that you can not use 1127 BeiDou and 1010 GLONASS messages.

Here is some information about each message from RTCM STANDARD 10403.3 (Radio Technical Commission for Maritime Services, 2016):

- **Message Type 1002** supports single-frequency RTK operation and includes an indication of the GPS satellite carrier-to-noise ratio (CNR) as measured by the reference station.
- **Message Type 1006** provides the earth-centered, earth-fixed (ECEF) coordinates of the antenna reference point (ARP)
for a stationary reference station and the height of the ARP above a survey monument.
- **Message Type 1008** provides an ASCII descriptor of the reference station antenna and the antenna serial number, which removes any ambiguity about the model number or production run.
- **Message Type 1010** supports single-frequency RTK operation and includes an indication of the GLONASS satellite carrier-to-noise (CNR) as measured by the reference station.
- **Message Type 1019** contains GPS satellite ephemeris information. This message could be broadcast in the event that the IODC (Issue of Data, Clock) does not match the IODE (Issue of Data, Ephemeris), which would require the differential reference station to base corrections on the previous good satellite ephemeris. This would allow the user equipment just entering the differential system to utilize the corrections being broadcast for that ephemeris, and would support the use of the satellite for differential navigation despite the fact that the satellite ephemeris was in error. It is anticipated that this message type would be broadcast every 2 minutes or so while this condition persisted.
Another use of the message is to assist user receivers to quickly acquire satellites. For example, if the user receiver has access to a wireless service with this message, rather than waiting until one satellite has been acquired and its almanac data processed, it can utilize the ephemeris information immediately.
- **Message Type 1020** contains GLONASS satellite ephemeris information and has same properties as 1019 message.
- **Messages 1097 (GALILEO), 1107 (SBAS), 1117 (QZSS), 1127 (BeiDou)** are MSM7 (Multiple Signal Messages). MSM7 are high precision messages which means that they contains a complete set of RINEX observations with extended resolution: Full GNSS Pseudoranges, Phase Ranges, Phase Range Rate and CNR (high resolution). Key features of the messages are as follows: Effective identification of satellites and their signals by introducing satellite and signal masks, Effective bit consumption for ‘transition GNSS periods’ by introducing cell masks, Effective decomposition of observables by introducing the rough/fine range concept, Effective scalability of different observables by introducing observation blocks, Expressing complete set of RINEX observations for all bands and all signals in the same units (milliseconds). 

	!!! note
		One of the most important data fields (DF) in MSM messages is the signal mask. It is a bitset indicating which signals from a given GNSS are available from at least one of the multitude of tracked satellites. Each bit in the signal mask is representative of a specific GNSS signal. The definition of the signal mask bits is different for each GNSS, and is provided for each GNSS separately. 

> <cite> Radio Technical Commission for Maritime Services. 2016. RTCM STANDARD 10403.3 DIFFERENTIAL GNSS (GLOBAL NAVIGATION SATELLITE SYSTEMS) SERVICES – VERSION 3. Virginia: Radio Technical Commission for Maritime Services, pp. 108-262</cite>


## Base position

<p style="text-align:center"><img src="../img/reachview/base_mode/position.png" style="width: 800px;"/></p>

There are two main options how to specify base station position. Note that RTK positioning is relative to the base station, so any inaccuracy in it’s position will result in a constant shift of rover coordinates. For many applications it is not critical and averaged single coordinate of the base could be used. If your application requires absolute accuracy for rover position an accurate  base coordinate must be entered.

### Manual
In this mode you supply an a priori known coordinate by locating the unit above surveyed point. Coordinate has to be supplied in ECEF XYZ or in WGS84 Latitude and Longitude and WGS84 ellipsoid height. Antenna height offset is entered at this stage as well, offset is limited to 6.5535 m by the RTCM message.

### Average 
By default Reach will average base position every time it starts. This feature significantly simplifies initial setup in a new location, however it will not provide an accurate absolute coordinate.

ReachView has a unique feature that allows it to determine base station position while working as a rover from another base. This is done by obtaining RTK Fixed solution, averaging it over a period of time and this way obtaining an accurate position for the base. A typical scenario would involve setting up a local base station by determining its coordinate from NTRIP and then broadcasting correction locally, thus reducing the baseline for rovers and improving positioning performance.

If the reference station is too far away it is possible to average float and still improve the accuracy of the position.

In case no correction is available when setting up base or absolute accuracy is not required averaged single coordinates could be used.

**Save averaged position to manual**  
After you have successfully obtained averaged position you might want to save it for future use. Click on the “save coordinates” icon and position will be saved as if it was entered in manual mode. Now every time Reach starts it will broadcast this position in correction messages.

**Repeat averaging**  
If you would like to restart base position averaging process you can click on “repeat averaging” icon.This is especially useful in a situation when you accidentally moved Reach during averaging.


