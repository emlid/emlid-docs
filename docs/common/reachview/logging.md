#Record and download logs

This tutorial shows how to record logs for Data Analysis and Post-Processing Kinematic (PPK) and how to download them from Reach to your computer.

!!! tip ""
	To learn more about PPK check [this article](/common/tutorials/ppk-introduction).

##Log split period

Before starting log recording, you can specify the log split period in ReachView [settings](settings/). For instance, if we set to save the log every 4 hours, the new log file will be created every 4 hours, while preserving the previous log as well. This setting allows you to control the size of the files that you work with.

##Logging

To enable logs recording, go to "Logging" tab in ReachView. Here you can see several logging options. Reach can record raw data, position log, and base corrections.

<p style="text-align:center" ><img src="../img/reachview/logging/enable-logging.png" style="width: 800px;" /></p>

<p style="text-align:center" ><img src="../img/reachview/logging/enable-logging.gif" style="width: 800px;" /></p>

###Raw data

A raw data log contains GNSS observations from the receiver without calculation of accurate coordinates. It can be recorded in UBX or directly into industry standard RINEX format. UBX can be converted to RINEX with RTKCONV utility after downloading to your PC. If you don’t know which one you need, we recommend using RINEX 3.03.

Time marks for UAV mapping are stored in this file as well.

###Position

Position can be logged in different formats. Open a dropdown list to choose the format for position coordinates.

!!! note ""
	Here's a short formats overview. More detailed descriptions of formats may be found in Position output section of the [docs](position-output/#formats).

* **LLH**

LLH is a simple text protocol for Latitude, Longitude, and Height in WGS84. It also contains information about RTK solution status.

* **XYZ**

XYZ is a simple text protocol for X, Y, Z ECEF coordinates as well as solution status. 

* **ENU**

ENU is also a simple text protocol for East, North and UP components of the baseline as well as solution status.

* **NMEA**

NMEA 0183 is the most popular standard in the industry. It is usually supported by most software and hardware. NMEA messages supported: GPRMC, GPGGA, GPGSA, GLGSA, GAGSA, GPGSV, GLGSV, GAGSV. 

* **ERB**

ERB format is used for communication with Ardupilot.

###Base corrections

The last logging option is base corrections. This log format is defined by corrections Reach accept from the base. If you use Reach base, this log will be recorded in RTCM3.

##Downloading

After completing the survey, you can save logs to your Mac, Windows, Linux or mobile device. You can do it in the same "Logging" tab in ReachView.

Turn off toggles <img src="../img/reachview/logging/toggle.png" align="middle" /> to stop record the logs. Find your logs below in the "Logging" tab in ReachView.

<p style="text-align:center" ><img src="../img/reachview/logging/download-logs.gif" style="width: 800px;" /></p>

You can see the recording date and time. 

There are two buttons on the right side of each log: <img src="../img/reachview/logging/blue-arrow.png" align="middle" alt="blue arrow" />  button allows to save it, and <img src="../img/reachview/logging/garbage-can.png" align="middle" alt="red garbage can" /> button deletes it.

Now when the logs are downloaded, you can use [RTKLIB software](/common/tutorials/gps-post-processing) from Emlid docs to start working with your data.

Check [PPK guide](/common/tutorials/gps-post-processing) in Emlid docs to learn more about PPK. 



