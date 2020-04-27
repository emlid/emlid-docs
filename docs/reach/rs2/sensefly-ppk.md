##Overview

In this tutorial, you will find the information on how to perform PPK with senseFly drones and Reach RS2 in eMotion software. 

!!! note ""
    Step-by-step guide can be also found on [senseFly Knowledge Base](https://sensefly.zendesk.com/hc/en-us/articles/360010693419-Emlid-Reach-RS2-PPK-Workflow).  

##Preparing Reach RS2 data 

In this part, we will explain how to place Reach RS2 to record logs for PPK.

###Placing the Reach RS2 receiver

The video below demonstrates how to place the Reach RS2 base over a known point. 

<div style="text-align: center;"><iframe title="Emlid manuals" width="560" height="315" src="https://www.youtube.com/embed/FilRoPVDjCs" allowfullscreen></iframe></div>

To find out other ways of placing the local base station, [consult this guide](../common/tutorials/placing-the-base/).

The general steps for placing the base receiver are described below.

* Make sure you choose an appropriate location to place Reach RS2 base station. Take a look at 2 pictures below. The left picture demonstrates desirable conditions for the base location. The right one is an example of bad surrounding conditions such as the reduced view of the sky, possible obstructions or vegetation nearby

<div style="text-align: center;"><img src="../img/reachrs2/sensefly-ppk/Reach-base-position-correct-wrong.png" style="width: 600px;"></div>

* Make sure your Reach RS2 is placed precisely above the marked point on the tripod and leveled

* If you are setting up base coordinates manually, measure the antenna height offset

!!! note "" 
    Antenna height is measured as the distance between the mark and the antenna reference point (ARP).


For Reach RS2, consider the antenna height as the distance between the mark and the bottom of Reach RS2 (h on the figure below) plus 134 mm.

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/placing-reach.png" style="width: 800px;"/></p>


!!! note ""  
    Precise base coordinates will be needed for post-processing in eMotion. 

###Raw data logging

* Connect to your Reach RS2 using the ReachView App

??? note "Connecting to Reach with iOS/Android device"

    * Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [Apple Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
    
    * Go to Wi-Fi settings on your device
    
    * Connect to Reach hotspot. It appears as **reach:XX:XX**
    
    * Enter password **emlidreach**
    
    * Launch ReachView app
    
    * Choose Reach from the list

??? note "Connecting via a web browser from any device"

	* Go to Wi-Fi settings on your device

	* Connect to Reach hotspot. It appears as **reach:XX:XX**

    * Enter password **emlidreach**

    * Launch a web browser (we recommend using Chrome or Mozilla)

    * Go to 192.168.42.1


* Configure constellation choice in the [RTK Settings tab](../common/reachview/rtk-settings). Our default recommendation is all GNSS enabled at 1 Hz

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/rtk-settings.png" style="width: 600px;"/></p>

* Go to the Logging tab

* Enable the raw data log in UBX format

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/logging-tab.png" style="width: 600px;"/></p>

* Once Reach RS2 base starts data logging, you can fly your eBee in a standalone mode

###Converting raw data log 

* Download [RTKLIB QT apps](https://files.emlid.com/RTKLIB/rtklib-qt-win-b33.zip)

* [Download raw files from Reach to your PC](https://docs.emlid.com/reachrs2/common/quickstart/downloading-files/#logs)

* Start RTKLIB RTKConv 

* Push _Options_ button

* Choose _RINEX Version_ 2.11

* Turn on _Satellites Systems_ you need

* Press _OK_ 

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/rtkconv_options.png" style="width: 400px;"/></p>

* Add your rover raw log in the first field and choose output directory

* Choose format of your log in pop-down menu. Set format to u-blox 

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/rtkconv_first_step.png" style="width: 400px;"/></p>

* Press _Convert_ 

* Now you can proceed to post-processing your logs in eMotion3

##Post-processing with eMotion

* Launch [eMotion3](https://www.sensefly.com/software/emotion/) and select post flight FDM (Flight Device Manager)

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/logs-import.png" style="width: 400px;"/></p>

* Create a project and import the flight logs. Procceed to the RTK/PPK workflow tab

* Set Input file format to RINEX 

* Select newly converted RINEX O, N and G files from the Reach RS2 base

* Set Antenna model to UNKNOWN 

* Fill the base position field with the the known coordinates of the markered ground point (ground marker)

* Set the Height Reference to the Ground marker

* Enter the Antenna height calculated according to explanation in this step for the receiver

* Press Next to calculate solution

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/fdm_process.png" style="width: 400px;"/></p>

* Once Calculated solution is finished, the Geotags are post-processed based on the RINEX file with corrected base position

<p style="text-align:center"><img src="../img/reachrs2/sensefly-ppk/fdm_result.JPG" style="width: 400px;"/></p>

* Proceed to the remaining FDM steps to complete the Postflight process

Now you have successfully post-processed logs from Reach RS2 and eBee drone!