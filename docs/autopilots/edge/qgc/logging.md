There are two types of logs that can be used to retrieve data for post-processing or to diagnose problems while running
ArduPilot.


### DataFlash logs

DataFlash logs are saved by the AutoPilot directly to on-board memory. In order to download logs from Edge you need to:

* Click the Analyze  <span style="text-align: center;"> <img src="../../img/qgc/analyze_button.png" style="width: 30px; vertical-align:middle"></span> icon 
at the top of the window.

* Click the 'Refresh' button to view available logs.

* Select the log you would like to download, and click 'Download'.

* Multiple logs can be downloaded by highlighting the desired logs before clicking 'Download'.

* After clicking 'Download' there will appear a new window prompting to choose directory where to save logs.  

<div style="text-align: center;"><img src="../../img/qgc/log-download.png"> </div>
       

### Telemetry logs

Telemetry logs store received MAVLink messages. QGroundControl saves telemetry logs locally in a .tlog file. 

By default, QGroundControl only begins logging after the vehicle has been armed. But it can be configured to
log data while the autopilot is disarmed. To do this click <span style="text-align: center;">
<img src="../../img/quickstart/qgc_settings_button.png" style="width: 30px; vertical-align:middle"></span> icon in the
menu bar, then select the 'General' tab. Select the option to save logs 'even if vehicle was not armed' in order to log 
telemetry while disarmed. In order to save a telemetry log from QGroundControl, you must click save when prompted after
disconnecting from the vehicle, or after quitting the application.

<div style="text-align: center;"><img src="../../img/qgc/logging-when-disarmed.png"> </div>

!!! tip
    QGroundControl allows you to configure a directory to automatically save all telemetry logs.


