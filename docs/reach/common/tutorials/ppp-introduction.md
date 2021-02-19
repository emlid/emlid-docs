With the Precise Point Positioning (PPP) technique, you may accurately determine the coordinates of a static point anywhere in the world without real-time corrections or base station nearby.

!!! tip "" 
    You can do PPP with both Reach RS2 and Reach RS+ devices. To process data from Reach RS+, you can use the [NRCAN CSRS-PPP service](#nrcan-csrs-ppp-service-overview).

In this guide, we will walk you through the following steps:

- Recording RINEX data on Reach
- Exporting raw data from the ReachView 3 app to your mobile device or PC
- Uploading the collected file to PPP service
- Entering the obtained base coordinates into the ReachView 3 app

The equipment you need to accomplish the survey:

- Reach receiver
- Tripod

## How PPP works

A standalone receiver finds out its position relying on the data obtained from satellites only. Along with raw data, it also gets navigation messages containing such data as satellite clock offset, the ionospheric and tropospheric corrections, etc. Due to information about these offsets, the receiver may calculate its position with a few meters' accuracy. If there was no navigation data, the accuracy would be much worse.

In RTK and PPK, these offsets might be eliminated since both the base and the rover operate in quite similar conditions.

PPP allows the single receiver to achieve high-level accuracy without the use of corrections from the base station. To calculate the coordinates, PPP uses the same data that is provided by the navigation message but much more accurate. Thereby, the Single receiver might determine its position with a centimeter-level accuracy using only its own raw data and precise ephemerides and clock offsets provided by a PPP service.

The PPP technique is commonly used for determining the absolute base position for further RTK/PPK surveys.

### Advantages and disadvantages of using PPP

Post-Processed PPP has both advantages and disadvantages in comparison with [PPK technology](ppk-introduction.md):
<center>

| Advantages | Disadvantages |
| :----------: | :-------------: |
| Only one receiver is needed| The time required to move from Float to a fixed solution |
| The position can be highly accurate determined at any place on the Earth | Most PPP services only allow using Static processing currently | 
| The position is determined with absolute accuracy | Most PPP services only allow GPS processing currently |
|  | Most PPP services only allow multi-frequency processing |

</center>

## PPP services overview

There are several PPP services available:

* **[Brazilian IBGE-PPP service](https://www.ibge.gov.br/en/geosciences/geodetic-positioning/services-for-geodetic-positioning/20104-online-service-for-post-processing-gnss-data.html?=&t=processar-os-dados)**, mainly used in South America region, is capable of working with  both single-band and multi-band Reach receivers
    
* **[AUSPOS 3.0](https://gnss.ga.gov.au/auspos)**, a PPP service widely used in the Asia-Pacific region, can now process data from Reach RS2 receiver

* **[Canadian NRCAN CSRS-PPP service](https://webapp.geod.nrcan.gc.ca/geod/tools-outils/ppp.php)** can process both single-frequency and multi-frequency logs

In this guide, we will take a closer look at the [Canadian NRCAN CSRS-PPP service](https://webapp.geod.nrcan.gc.ca/geod/tools-outils/ppp.php). However, you can work with other services, if more applicable to you.

### NRCAN CSRS-PPP service overview

The Canadian Spatial Reference System (CSRS) PPP service is provided by Natural Resources Canada's Canadian Geodetic Survey.

NRCAN CSRS-PPP service uses single or dual-frequency GPS and GLONASS data for solution computation and supports both Static and Kinematic modes.

- **Static** computation is accomplished with a receiver sitting on one point. In the result of Static mode, you will get the absolutely determined position of this point
- **Kinematic** mode allows surveying with a moving receiver and provides a path as the solution

Depending on the accuracy level and time that is required to get the solution, NRCAN CSRS-PPP service can calculate the data in the following modes<sup>[1](#myfootnote1)</sup>:

- **FINAL:**  the accuracy is about 2 cm (0.8 inches), available 13 -15 days after the end of the week
- **RAPID:** the accuracy is about 5 cm (2 inches), available the next day
- **ULTRA RAPID:** the accuracy is about 15 cm (6 inches), available every 90 minutes  

!!! note ""
    In this guide, we will show you how to process raw data from Reach RS2 recorded in the Static mode. However, with the NRCAN CSRS tool, it is also possible to process the data from a single-band Reach RS/RS+ receiver. With Reach RS/RS+, you will get an accuracy of about 30 cm.

You can learn more about NRCAN CSRS-PPP service on their [official site](https://www.nrcan.gc.ca/maps-tools-publications/tools/geodetic-reference-systems-tools/tools-applications/10925#ppp).

## Placing the Reach

Place a Reach device precisely above the marked point on the tripod and level it. You can learn more about placing Reach receiver in this [tutorial](placing-the-base.md).

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/placing-reach-rs2.png" style="width: 600px;"></div>

## Recording RINEX data on Reach

- Go to the *GNSS settings* tab
- Enable **GPS** and **GLONASS** and set up the update rate to **1 Hz**

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/rtk-settings.png" style="height: 550px;"></div>

- Navigate to the *Logging* tab
- Select RINEX 2.XX or 3.XX **Raw data** format.
- Enable raw data logging and record the data for 2.5 hours at least

!!! tip ""
    You may log the data from 2 hours to 24 hours depending on the accuracy required.

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/logging.png" style="height: 550px;"></div>

- Once you finish the survey, don't forget to toggle off raw data recording in the *Logging* tab

!!! danger ""
    Do not turn Reach off until the RINEX logs are processed.

## Exporting raw data from ReachView 3

After you finish raw data logging, you may download RINEX data from Reach to your mobile device or PC.

- In ReachView 3, go to the *Logging* tab
- Tap on the *Download* button to export the file

## Converting UBX logs to RINEX

In case you log raw data in UBX format, you can convert them manually in RTKLIB.

- Start *RTKLIB RTKCONV*
- Add your rover raw log in the first field and choose output directory
- Choose format of your log in pop-down menu. Set format to u-blox

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/RTKCONV.png" style="width: 600px;"></div>

- Push the *Options* button
- Choose RINEX Version 2.XX or 3.XX
- Turn on GPS and GLONASS satellite systems
- Enable L1 and L2 frequencies in the *Frequencies* tab

!!! note ""
    If you work with Reach RS2, you can also specify the receiver and antenna name before conversion:
    
    * the receiver name is `EMLID REACH RS2`
    * the antenna name is `EML_REACH_RS2`
    
    <div style="text-align: center;"><img src="../img/reach/ppp-introduction/RTKCONV-Options-NRCAN.png" style="width: 600px;"></div>

- Click on the *OK* button to save changes
- Push on the *Convert* button to start conversion process

As the result, you will get the *.obs and *.nav files.

## Submitting data to NRCAN CSRS-PPP service

- Click on *Sign in* button and enter your login and password to access [NRCAN CSRS-PPP](https://webapp.geod.nrcan.gc.ca/geod/tools-outils/ppp.php) or create a new account in case you do not have it yet
- In the *Email for results* field, enter your email address to get the results
- In *Processing mode*, choose Static
- Choose the datum in which you would like to get the position. In this guide, we will work with ITRF option
- In the RINEX observation file field, click on the *Choose file* button and browse for raw*.obs file
- Click on the *Submit to PPP* button to send the file for processing

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/submit-results.png" style="width: 600px;"></div>

NRCAN CSRS-PPP will send the file with solution to your email address.

## NRCAN CSRS-PPP results assessment

After you get the solution report, it might be useful to check how accurate the results are.

In the solution report, look for the Estimated Position for raw_*.obs header.
There should be a table with 4 rows:
<div style="text-align: center;"><img src="../img/reach/ppp-introduction/table.png" style="width: 600px;"></div>

- The first row contains calculated LLH coordinates in chosen coordinate system
- The Sigmas row shows an estimated accuracy
- In the A Priori row, there is an averaged in Single mode position taken from the RINEX header
- The Estimated - A Priori row displays the accuracy from this position specified in the RINEX header

## Setting up obtained base coordinates in ReachView 3

If you need the acquired coordinates to use them as the base position for RTK/PPK, you can now enter the base coordinated into the ReachView 3 app.

- In ReachView 3, go to the *Base mode* tab
- In the *Base coordinates input* mode, choose Manual
- Set up the required data format (LLH or XYZ)
- Enter the coordinates and specify the antenna height

!!! note ""
    You may need to convert the solution you get to WGS84.

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/Bluetooth.png" style="height: 550px;"></div>

If you experience any difficulties during the processing or want to discuss the workflow, start a thread at the [Emlid community forum](https://community.emlid.com/).

Further reading:

- [How RTK works](rtk-introduction.md)
- [How PPK works](ppk-introduction.md)
- [GPS Post-processing](gps-post-processing.md)
- [Placing the base](placing-the-base.md)
- [OPUS Workflow](opus-workflow.md)

<p style="font-size:70%;"><a name="myfootnote1">1</a>: Tools and Applications: Natural Resources Canada site. URL: https://www.nrcan.gc.ca/maps-tools-publications/tools/geodetic-reference-systems-tools/tools-applications/10925#ppp</p>
