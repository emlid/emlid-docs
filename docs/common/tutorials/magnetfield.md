In this tutorial you'll find the information on how to setup data collector running Topcon MAGNET Field Layout with Reach RS/RS+ via Bluetooth. When working with MAGNET Field Layout it is possible to use Reach RS in conjunction with Topcon Total Stations like LN-100.
<p style="text-align:center"><img src="../img/reach/magnetfield/topcontotalstation-reachrs.jpg" style="width: 600px;"/></p> 
<p style="text-align:center" >Topcon LN-100 and 2 Reach RS for site layout (photo courtesy of Brent Wiebe).</p>



## Configuring Bluetooth connection

!!! note
    In this tutorial the Bluetooth connection with Windows device is shown. Exact steps of pairing the devices may vary on different platforms.

* In the ReachView app go to Wi-Fi/Bluetooth tab. Turn on Bluetooth and make Reach RS always discoverable.
<p style="text-align:center"><img src="../img/reach/magnetfield/bt-on.png" style="width: 800px;"/></p> 
<br>
* On data collector go to Bluetooth settings and select "Add a Bluetooth Device". Select Reach from the list of discovered devices and confirm the connection.
<p style="text-align:center"><img src="../img/reach/magnetfield/windows-pairing.png" style="width: 800px;"/></p> 
<br>
* When pairing is completed you will see the data collector is listed in ReachView. 
<p style="text-align:center"><img src="../img/reach/magnetfield/reachview-paired.png" style="width: 800px;"/></p> 


## Configuring ReachView

After successful Bluetooth pairing you should configure BT position output and correction input if needed.

### Position output

* Go to Position output in ReachView and select BT tab. Select NMEA format and click Apply.
<p style="text-align:center"><img src="../img/reach/magnetfield/position-output.png" style="width: 800px;"/></p> 


### Correction input

* If you want to send the corrections from your controller via Bluetooth go to Correction input and select BT tab. Set RTCM3 format and Apply settings.
<p style="text-align:center"><img src="../img/reach/magnetfield/correction-input.png" style="width: 800px;"/></p> 

## Configuring MAGNET Field

### Configuring the communication between SurvCE and Reach RS

* Launch MAGNET Field and go to Configure menu.
<p style="text-align:center"><img src="../img/reach/magnetfield/configure.png" style="width: 600px;"/></p> 
<br>
* Choose "Survey" 
<p style="text-align:center"><img src="../img/reach/magnetfield/survey.png" style="width: 600px;"/></p> 
<br>
* Click on "Select from Library" in GPS+ Configuration.
<p style="text-align:center"><img src="../img/reach/magnetfield/library-select.png" style="width: 600px;"/></p> 
<br>
* Add new configuration.
<p style="text-align:center"><img src="../img/reach/magnetfield/add-new.png" style="width: 600px;"/></p> 
<br>
* Type in the name for the configuration and choose Real Time DGPS/NMEA as Type with SBAS/Autonomous Corrections. Click "Next".
<p style="text-align:center"><img src="../img/reach/magnetfield/reachrs-profile.png" style="width: 600px;"/></p> 
<br>
* Pick "Generic NMEA" from the manufacturers list. Proceed to the next step.
<p style="text-align:center"><img src="../img/reach/magnetfield/generic-nmea.png" style="width: 600px;"/></p> 
<br>
* Tick "External Receiver" and select Bluetooth connection type.
<p style="text-align:center"><img src="../img/reach/magnetfield/external-receiver-checkbox.png" style="width: 600px;"/></p> 
<br>
* Click "Next" to configure survey parameters or click on the green tick to finish the setup. 
<p style="text-align:center"><img src="../img/reach/magnetfield/complete-the-setup.png" style="width: 600px;"/></p> 
<br>
* Pick the created configuration and click on the green tick to exit Configuration Library.
<p style="text-align:center"><img src="../img/reach/magnetfield/library-exit.png" style="width: 600px;"/></p> 
<br>
* Return to the main menu and select "Connect".
<p style="text-align:center"><img src="../img/reach/magnetfield/connect.png" style="width: 600px;"/></p> 
<br>
* In connections select GPS device type and make sure Reach RS is chosen. Click "Connect".
<p style="text-align:center"><img src="../img/reach/magnetfield/connect-reach-rs.png" style="width: 600px;"/></p> 
<br>
* Make a search for Bluetooth devices and choose Reach from the list. Click "Select".
<p style="text-align:center"><img src="../img/reach/magnetfield/select-reach.png" style="width: 600px;"/></p> 
<br>
* In Bluetooth PIN settings tick "Require PIN" and enter the default PIN-code for Reach RS "123456".
<p style="text-align:center"><img src="../img/reach/magnetfield/pin-code.png" style="width: 600px;"/></p> 
<br>
* Now go to Setup and check the Status. If the connection is successful the position will be displayed with a number of satellites and PDOP.
<p style="text-align:center"><img src="../img/reach/magnetfield/integration-done.png" style="width: 600px;"/></p> 
<br>
* In case of successful connection you'll also see the receiver icon in the corner of MAGNET Field interface.
<p style="text-align:center"><img src="../img/reach/magnetfield/successful-connection.png" style="width: 600px;"/></p> 
<br>


