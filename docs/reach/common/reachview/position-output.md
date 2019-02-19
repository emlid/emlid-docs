
### Formats

<p style="text-align:center" ><img src="../img/reachview/position_output/format.png" style="width: 800px;" /></p>

Reach supports following position output formats: 

#### LLH
Simple text protocol for Latitude Longitude and Height as well as solution status. Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

#### XYZ
Simple text protocol for X, Y, Z ECEF coordinates as well as solution status. Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

#### ENU
Simple text protocol for East, North and UP components of the baseline as well as solution status. Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

#### NMEA 0183
The most popular standard in the industry. Supported messages: GNRMC, GNGGA, GPGSA, GLGSA, GAGSA, GPGSV, GLGSV, GAGSV, GNGST, GNVTG.

Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

#### ERB
Used for communication to Ardupilot, protocol description can be found [here](https://files.emlid.com/ERB.pdf).


**Data in any of these formats can be sent via Serial, TCP or Bluetooth.**

### Serial
Serial port connection is available through several hardware connection options. All of them support the following baud rates: 4800, 9600, 14400, 19200, 28800, 38400, 56000, 57600, 115200, 128000, 153600, 230400, 256000, 460800.

#### UART
Corresponds to TTL UART on Reach module or to RS232 port on Reach RS/RS+ extension connector. Common way to connect to autopilot or another consumer of position data.

#### USB-to-PC
When connected over USB to a PC Reach will show up as several devices, one of them will be a serial port. You can use this serial port to send position data to the PC.

#### USB OTG
Use a micro-USB OTG cable to connect USB accessories. In this mode only USB devices that emulate a serial port could be used. Example of popular chips that are supported: FT232, CP2102. There are numerous devices built on these chips that will provide you a TTL UART or RS232 port. 

### TCP
Typical scenario for using TCP is sending position data to an application on the same network or to a server with public IP. 

TCP supports two roles:

#### Server
You need to specify port and after that clients will be able to connect to this device on its IP address. Many clients can be connected to the same server.

#### Client
You need to specify IP address of the server and port number.

If ReachView does not allow to set a certain port number it means that it is reserved for internal use.

### Bluetooth
Bluetooth output is used to stream position data to smartphones, tablets or data collectors. Please make sure to pair your device in Bluetooth settings.

!!! note ""
	iOS devices don't support getting a location over Bluetooth from third-party hardware.

