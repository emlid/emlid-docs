ReachView supports four simultaneous logs streams. Full memory behaviour and log split period could be specified in the [settings](settings/). Every log stream has enable/disable logic, once enabled logs will be written even if you restart the device. After restart new log file will be automatically created.

### Raw data

<p style="text-align:center" ><img src="../img/reachview/logging/raw.png" style="width: 800px;" /></p>

Raw data is logged directly into RINEX and UBX format. UBX could be converted to Rinex after download using RTKCONV utility. Event marks are stored in this file as well.

### Position

<p style="text-align:center" ><img src="../img/reachview/logging/position.png" style="width: 800px;" /></p>

Position could be logged in different formats. 

**LLH**  
Simple text protocol for Latitude Longitude and Height as well as solution status. Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

**XYZ**  
Simple text protocol for X, Y, Z ECEF coordinates as well as solution status. Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

**ENU**  
Simple text protocol for East, North and UP components of the baseline as well as solution status. Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

**NMEA 0183**  
The most popular standard in the industry. Supported messages: GPRMC, GPGGA, GPGSA, GLGSA, GAGSA,  GPGSV, GLGSV and GAGSV. Protocol definition can be found in [RTKLIB ver. 2.4.2 Manual](http://www.rtklib.com/prog/manual_2.4.2.pdf) on page 102.

**ERB**  
Used for communication to Ardupilot, protocol description can be found [here](https://files.emlid.com/ERB.pdf).

### Base correction

<p style="text-align:center" ><img src="../img/reachview/logging/base_correction.png" style="width: 800px;" /></p>

Logs incoming correction from the base. Format is defined by correction input.