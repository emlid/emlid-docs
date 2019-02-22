SurvCE starting from version 5.06 supports Emlid Reach RS/RS+. In this tutorial you'll find the information on how to setup data collector running SurvCE/SurvPC with Reach RS/RS+ via Bluetooth.

## Configuring Bluetooth connection

!!! note ""
    In this tutorial the Bluetooth connection with Windows device is shown. Exact steps of pairing the devices may vary on different platforms.

* In the ReachView app go to Wi-Fi/Bluetooth tab. Turn on Bluetooth and make Reach RS/RS+ always discoverable.
<p style="text-align:center"><img src="../img/reach/survce/bt-on.png" style="width: 800px;"/></p> 
<br>
* On data collector go to Bluetooth settings and select "Add a Bluetooth Device". Select Reach from the list of discovered devices and confirm the connection.
<p style="text-align:center"><img src="../img/reach/survce/windows-pairing.png" style="width: 800px;"/></p> 
<br>
* When pairing is completed you will see the data collector is listed in ReachView. 
<p style="text-align:center"><img src="../img/reach/survce/reachview-paired.png" style="width: 800px;"/></p> 


!!! note "Windows OS workaround for SurvPC"
    If you are using SurvPC on Windows system with built-in Bluetooth adapter, you also need to check the COM port assigned to the BT device: <br> 1. Go to Control Panel and choose Devices and Printers<p style="text-align:center"><img src="../img/reach/survce/control-panel.png" style="width: 600px;"/></p> <br> 2. Right click on Reach device and select Properties <p style="text-align:center"><img src="../img/reach/survce/properties.png" style="width: 600px;"/></p> <br> 3. Go to Hardware tab and check Standard Serial over Bluetooth Link. In this example it's COM8. <p style="text-align:center"><img src="../img/reach/survce/bt-com-port.png" style="width: 400px;"/></p>



## Configuring ReachView

After successful Bluetooth pairing you should configure BT position output and correction input if needed.

### Position output

* Go to Position output in ReachView and select BT tab. Select NMEA format and click Apply.
<p style="text-align:center"><img src="../img/reach/survce/position-output.png" style="width: 800px;"/></p> 


### Correction input

* If you want to send the corrections from your controller via Bluetooth go to Correction input and select BT tab. Set RTCM3 format and Apply settings.
<p style="text-align:center"><img src="../img/reach/survce/correction-input.png" style="width: 800px;"/></p> 

## Configuring SurvCE

### Configuring the communication between SurvCE and Reach RS/RS+
* After launching SurvCE and creating a new project go to the Equip tab and select GPS Rover.
<p style="text-align:center"><img src="../img/reach/survce/GPS-rover.png" style="width: 600px;"/></p> 
<br>
* Select EMLID as Manufacturer. 
<p style="text-align:center"><img src="../img/reach/survce/emlid-reachrs.png" style="width: 600px;"/></p> 
<br>
* Then go to Comms tab and pick Bluetooth settings.

<p style="text-align:center"><img src="../img/reach/survce/bt-configure.png" style="width: 600px;"/></p> 

!!! note "Windows OS workaround for SurvPC"
    If you are using SurvPC on Windows system with built-in Bluetooth adapter, you just need to choose Generic BT Type and select COM port assigned to the BT device: <p style="text-align:center"><img src="../img/reach/survce/surv-pc-com-port.png" style="width: 600px;"/></p> 


* In a dialog window click "Find Device".
<p style="text-align:center"><img src="../img/reach/survce/find-the-device.png" style="width: 600px;"/></p> 
<br>
* Once Reach RS/RS+ is detected select it.
<p style="text-align:center"><img src="../img/reach/survce/choose-reach.png" style="width: 600px;"/></p> 
<br>
* Connect Reach RS/RS+ and SurvCE.
<p style="text-align:center"><img src="../img/reach/survce/connect-bt.png" style="width: 600px;"/></p> 
<br>
* You will see the confirmation of connection. 
<p style="text-align:center"><img src="../img/reach/survce/success.png" style="width: 600px;"/></p> 

### Configure SurvCE to receive RTK corrections from NTRIP caster

* In GPS Rover dialog select RTK tab. Select Data Collector Internet as Device and NTRIP as Network.
<p style="text-align:center"><img src="../img/reach/survce/NTRIP-configure.png" style="width: 600px;"/></p> 
<br>
* Go to Network settings and fill in NTRIP caster details. 
<p style="text-align:center"><img src="../img/reach/survce/ntrip-account.png" style="width: 600px;"/></p> 
<br>
* After this select the mountpoint and click on the green tick. 
<p style="text-align:center"><img src="../img/reach/survce/mountpoints.png" style="width: 600px;"/></p> 
<br>
* The setup finished. You are ready to collect the data with Reach RS/RS+ and SurvCE!
