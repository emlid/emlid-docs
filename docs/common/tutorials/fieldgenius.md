
In this tutorial you'll find the information on how to setup data collector running FieldGenius with Reach RS/RS+ via Bluetooth. Step-by-step guide can be also found on [MicroSurvey knowledgebase](http://helpdesk.microsurvey.com/index.php?/Knowledgebase/Article/View/1436).


## Configuring Bluetooth connection

* In the ReachView app go to Wi-Fi/Bluetooth tab. Turn on Bluetooth and make Reach RS always discoverable.
<p style="text-align:center"><img src="../img/reach/fieldgenius/bt-on.png" style="width: 800px;"/></p> 
<br>
* In Windows go to Bluetooth settings and select "Add a Bluetooth Device". Select Reach from the list of discovered devices and confirm the connection.
<p style="text-align:center"><img src="../img/reach/fieldgenius/windows-pairing.png" style="width: 800px;"/></p> 
<br>
* When pairing is completed you will see Windows device is listed in ReachView. Reach device will be listed as device in Windows.
<p style="text-align:center"><img src="../img/reach/fieldgenius/reachview-paired.png" style="width: 800px;"/></p> 
<br>
<p style="text-align:center"><img src="../img/reach/fieldgenius/windows-connected.png" style="width: 800px;"/></p> 

## Configuring ReachView

After successful Bluetooth pairing you should configure BT position output and correction input if needed.

### Position output

* Go to Position output in ReachView and select BT tab. Select NMEA format and click Apply
<p style="text-align:center"><img src="../img/reach/fieldgenius/position-output.png" style="width: 800px;"/></p> 


### Correction input

* If you want to send the corrections from your controller via Bluetooth go to Correction input and select BT tab. Set RTCM3 format and Apply settings.
<p style="text-align:center"><img src="../img/reach/fieldgenius/correction-input.png" style="width: 800px;"/></p> 

## Configuring FieldGenius

### Creating a new project and instrument profile

* Launch FieldGenius. It will ask to create a new project. On this step you can go to Project Settings to configure units and coordinate system. Click OK to proceed.
<p style="text-align:center"><img src="../img/reach/fieldgenius/fieldgenius-project.png" style="width: 500px;"/></p> 
<br>
* You'll see FieldGenius interface. Choose "Select Instrument".
<p style="text-align:center"><img src="../img/reach/fieldgenius/select-instrument.png" style="width: 500px;"/></p> 
<br>
* Choose GNSS Rover instrument type and add new instrument profile.
<p style="text-align:center"><img src="../img/reach/fieldgenius/add-rover.png" style="width: 500px;"/></p> 
<br>
* Set Reach RS profile name and click Save.
<p style="text-align:center"><img src="../img/reach/fieldgenius/ReachRS-profile.png" style="width: 500px;"/></p> 

### Configuring the communication between FieldGenius and Reach RS

* Pick the Edit option to configure the receiver parameters.
<p style="text-align:center"><img src="../img/reach/fieldgenius/ReachRS-edit.png" style="width: 500px;"/></p>
<br>
* Select "Model and Communication"
<p style="text-align:center"><img src="../img/reach/fieldgenius/model-and-communication.png" style="width: 500px;"/></p> 
<br>
* Select NMEA from the Make list and Basic Model. Click on "Bluetooth Device List".
<p style="text-align:center"><img src="../img/reach/fieldgenius/bluetooth-list.png" style="width: 500px;"/></p> 
<br>
* Click "Search" in Bluetooth Device List.
<p style="text-align:center"><img src="../img/reach/fieldgenius/search-bt.png" style="width: 500px;"/></p> 
<br>
* Select Reach device. 
<p style="text-align:center"><img src="../img/reach/fieldgenius/reach-bt-appear.png" style="width: 500px;"/></p> 
<br>
* Enter the default PIN Code, for Reach RS it is "123456" and press "OK".
<p style="text-align:center"><img src="../img/reach/fieldgenius/Pin-code.png" style="width: 500px;"/></p> 
<br>
* After adding Reach device in Bluetooth Device List return to Model and Communication settings and click "Connect".
<p style="text-align:center"><img src="../img/reach/fieldgenius/connect-to-fieldgenius-reach.png" style="width: 500px;"/></p> 
<br>
* You will see progress dialog.
<p style="text-align:center"><img src="../img/reach/fieldgenius/process-bar.png" style="width: 500px;"/></p> 
<br>
* If the connection is successful the position will be displayed with a number of satellites and PDOP.
<p style="text-align:center"><img src="../img/reach/fieldgenius/successful-connection.png" style="width: 500px;"/></p> 

### Configure FieldGenius to receive RTK corrections from a NTRIP caster

* Go to Instrument Settings.
<p style="text-align:center"><img src="../img/reach/fieldgenius/correction-input-settings.png" style="width: 500px;"/></p> 
<br>
* Choose "Link Configure".
<p style="text-align:center"><img src="../img/reach/fieldgenius/link-configure.png" style="width: 500px;"/></p> 
* Pick Data Collector Internet in Link Device and click "Setup".
<p style="text-align:center"><img src="../img/reach/fieldgenius/ntrip-setup.png" style="width: 500px;"/></p> 
<br>
* In the dialog window click "Press to Modify".
<p style="text-align:center"><img src="../img/reach/fieldgenius/ntrip-modify.png" style="width: 500px;"/></p> 
<br>
* Click "Add" in NTRIP Casters dialog and enter NTRIP caster details. Press "OK".
<p style="text-align:center"><img src="../img/reach/fieldgenius/ntrip-account-add.png" style="width: 500px;"/></p> 
<br>
*  Select the created caster. 
<p style="text-align:center"><img src="../img/reach/fieldgenius/select-caster.png" style="width: 500px;"/></p> 
<br>
* Pick "OK" to finish the setup.
<p style="text-align:center"><img src="../img/reach/fieldgenius/save-ntrip-account.png" style="width: 500px;"/></p> 
<br>
* In Link Configure dialog pick "Connect". 
<p style="text-align:center"><img src="../img/reach/fieldgenius/connect-to-caster.png" style="width: 500px;"/></p> 
<br>
* Once connected to the Internet, request the sourcetable and choose a mountpoint.
<p style="text-align:center"><img src="../img/reach/fieldgenius/request-sourcetable.png" style="width: 500px;"/></p> 
<br>
<p style="text-align:center"><img src="../img/reach/fieldgenius/select-mountpoint.png" style="width: 500px;"/></p> 
<br>
* In a moment you will see the solution status in FieldGenius interface. 
<p style="text-align:center"><img src="../img/reach/fieldgenius/fix-fieldgenius.png" style="width: 500px;"/></p> 
<br>
* You can also go to ReachView to check satellites and solution status.
<p style="text-align:center"><img src="../img/reach/fieldgenius/fix-reachview.png" style="width: 800px;"/></p> 





