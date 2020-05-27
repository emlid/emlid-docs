# Precise Point Positioning (PPP)

With the Precise Point Positioning (PPP) technique, you may accurately determine the coordinates of a static point anywhere in the world without real-time corrections or base station nearby.

!!! tip ""

    You can do PPP with both Reach RS2 and Reach RS+ devices. To process data from Reach RS+, use the NRCAN CSRS-PPP service. [More details are below.](#nrcan-csrs-ppp-service)

In this guide, we will walk you through the following steps:

- Recording RINEX data on Reach
- Exporting raw data from ReachView to your mobile device or PC
- Uploading the collected file to PPP service (OPUS or NRCAN)
- Entering the obtained base coordinates into ReachView

The equipment you need to accomplish the survey:

- Reach receiver
- Tripod

## How PPP works

A standalone receiver finds out its position relying on the data obtained from satellites only. Along with raw data, it also gets navigation messages containing such data as satellite clock offset, the ionospheric and tropospheric corrections, etc. Due to information about these offsets, the receiver may calculate its position with a few meters' accuracy. If there was no navigation data, the accuracy would be much worst.

In RTK and PPK, these offsets might be eliminated since both the base and the rover operate in quite similar conditions.

PPP allows the single receiver to achieve high-level accuracy without the use of corrections from the base station. To calculate the coordinates, PPP uses the same data that are provided by the navigation message but much more accurate. Thereby, the Single receiver might determine its position with a centimeter-level accuracy using only its own raw data and precise ephemerides and clock offsets provided by a PPP service.


The PPP technique is commonly used for determining the absolute base position for further RTK/PPK surveys.

### Advantages and disadvantages of using PPP

Post-Processed PPP has both advantages and disadvantages in comparison with [PPK technology:](../../common/tutorials/ppk-introduction.md)

<center>

| Advantages | Disadvantages |
| :----------: | :-------------: |
| Only one receiver is needed| The time required to move from Float to a fixed solution |
| The position can be highly accurate determined at any place on the Earth | Most PPP services only allow using Static processing currently | 
| The position is determined with absolute accuracy | Most PPP services only allow GPS processing currently |
|  | Most PPP services only allow multi-frequency processing |

</center>

## PPP services overview

There are several PPP services available. In this guide, we will take a closer look at the [US NOAA's OPUS PPP service](https://www.ngs.noaa.gov/OPUS/) and the [Canadian NRCAN CSRS-PPP service.](https://webapp.geod.nrcan.gc.ca/geod/tools-outils/ppp.php)

!!! danger ""

    AUSPOS, a PPP service widely used in the Asia-Pacific region, doesn't currently support L2C observations from Reach. The L2C support should be added in the future.

### NOAA's OPUS PPP service

Online Positioning User Service (OPUS) is provided by the National Oceanic and Atmospheric Administration (NOAA).

OPUS PPP service uses dual-frequency GPS data for solution computation and supports the Static mode only. The Static data is required to be recorded on the stationary unmoving receiver.

There are 2 ways you can process the data in OPUS:

- Static (for data that are 2 to 48 hours in duration)
- Rapid-Static (for data that are 15 minutes to 2 hours in duration)

The Static and Rapid-Static methods use different processing software and provide pretty similar horizontal accuracy. The Rapid-Static processing has more strict requirements for the data quality in comparison with the Static approach. Moreover, Rapid-Static processing is available only for some regions. <sup>[1](#myfootnote1)</sup>

!!! note ""

    In this guide, we will show you how to process raw data from Reach RS2 using the Static method.

You can learn more about NOAA's OPUS PPP service on their [official site.](https://www.ngs.noaa.gov/OPUS/about.jsp)

### NRCAN CSRS-PPP service

The Canadian Spatial Reference System (CSRS) PPP service is provided by Natural Resources Canada's Canadian Geodetic Survey.

NRCAN CSRS-PPP service uses single or dual-frequency GPS and GLONASS data for solution computation and supports both Static and Kinematic modes.

- **Static** computation is accomplished with a receiver sitting on one point. In the result of Static mode, you will get the absolutely determined position of this point
- **Kinematic** mode allows surveying with a moving receiver and provides a path as the solution

Depending on the accuracy level and time that is required to get the solution, NRCAN CSRS-PPP service can calculate the data in the following modes <sup>[2](#myfootnote2)</sup>
:

- **FINAL:** the accuracy is about 2 cm (0.8 inches), available 13 -15 days after the end of the week
- **RAPID:** the accuracy is about 5 cm (2 inches), available the next day
- **ULTRA RAPID:** the accuracy is about 15 cm (6 inches), available every 90 minutes

!!! note ""

    In this guide, we will show you how to process raw data from Reach RS2 recorded in the Static mode. However, with the NRCAN CSRS tool, it is also possible to process the data from a single-band Reach RS/RS+ receiver. With Reach RS/RS+, you will get an accuracy of about 30 cm.

You can learn more about NRCAN CSRS-PPP service on their [official site.](https://www.nrcan.gc.ca/maps-tools-publications/tools/geodetic-reference-systems-tools/tools-applications/10925#ppp)

## Placing the Reach

Place a Reach device precisely above the marked point on the tripod and level it. [Learn more about placing Reach receiver in this docs entry.](../../common/tutorials/placing-the-base.md)

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/placing-reach-rs2.png" style="width: 600px;"></div>

## Recording RINEX data on Reach for PPP

- Go to the *RTK Settings* tab
- Choose **Static** Positioning mode, enable **GPS** only and set up the update rate to **1 Hz**

!!! tip ""

    While OPUS handles only GPS data, NRCAN is able to work with both GPS and GLONASS.

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/rtk-settings.png" style="width: 600px;"></div>

- Navigate to the *Logging* tab
- Select RINEX 2.10 **Raw data** format.

!!! tip ""

    OPUS only works with RINEX 2.XX format of raw data recorded on Reach. As for NRCAN, it accepts RINEX 3.XX files as well.

- Enable raw data logging and record the data for 2.5 hours at least

!!! tip ""

    You may log the data from 2 hours to 24 hours depending on the accuracy required.

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/logging.png" style="width: 600px;"></div>


- Once you finish the survey, don't forget to toggle off raw data recording in the *Logging* tab

!!! danger ""

    Do not turn Reach off until the RINEX logs are processed.

## Exporting raw data from ReachView

After you finish raw data logging, you may download RINEX data from Reach to your mobile device or PC.

- In ReachView, go to the *Logging* tab
- Tap on the **Download** button to export the file

[Learn more about downloading files from Reach in this docs entry.](../../common/reachview/logging.md#downloading)

## Converting UBX logs to RINEX

In case you log raw data in UBX format, you can convert them manually in RTKLIB.

- Start **RTKLIB RTKCONV**
- Add your rover raw log in the first field and choose output directory
- Choose format of your log in pop-down menu. Set format to u-blox

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/RTKCONV.png" style="width: 600px;"></div>

- Push the **Options** button
- Choose RINEX Version 2.XX

!!! tip ""

    OPUS only works with RINEX 2.XX format of raw data recorded on Reach. As for NRCAN, it accepts RINEX 3.XX files as well.

- For OPUS, turn on the GPS satellite system only. For NRCAN, you may turn on GPS and GLONASS satellite systems
- Enable L1 and L2 frequencies in the Frequencies tab

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/RTKCONV-Options.png" style="width: 600px;"></div>

- Click on the **OK** button to save changes
- Push on the **Convert** button to start conversion process

In the result, you will get the *.obs and *.nav files. 

## Submitting data to PPP service

### NOAA's OPUS PPP

- Go to the [NOAA's OPUS PPP site](https://www.ngs.noaa.gov/OPUS/)
- Click on the **Choose file** button and browse for raw*.obs file you would like to process
- Choose the NONE option in the Antenna field

!!! note ""

    We are currently in process of getting antenna details for PPP services.

- Type in the Antenna Height value. Consider this value as a pole height plus 134 mm
- Enter your email address to get the results
- Click on **Upload to Static** button to submit the data

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/OPUS.png" style="width: 600px;"></div>

OPUS will send the file with the solution to your email address.

### NRCAN CSRS-PPP

- Click on **Sign in** button and enter your login and password to access [NRCAN CSRS-PPP](https://webapp.geod.nrcan.gc.ca/geod/tools-outils/ppp.php) or create a new account in case you do not have it yet
- In the **Email for results** field, enter your email address to get the results
- In Processing mode, choose Static
- Choose the datum in which you would like to get the position. In this guide, we will work with ITRF option
- In the RINEX observation file field, click on the **Choose file** button and browse for raw*.obs file
- Click on the **Submit to PPP** button to send the file for processing

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/submit-results.png" style="width: 600px;"></div>

NRCAN CSRS-PPP will send the file with solution to your email address.

## Results assessment

After you get the solution report, it might be useful to check how accurate the results are.

### NOAA's OPUS PPP

In the solution report, you will get the name of the used reference frame, the XYZ and LLH coordinates of the point and accuracy estimation in meters. Additionally, you can check these fields: OBS USED, FIXED AMB, OVERALL RMS. 

The most accurate OPUS solutions have the following characteristics:

- Over 90% of observations are used
- Over 50% of ambiguities are fixed
- Overall RMS is less than 3 cm

### NRCAN CSRS-PPP

In the solution report, look for the Estimated Position for raw_*.obs header.

There should be a table with 4 rows:

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/table.png" style="width: 600px;"></div>

- The first row contains calculated LLH coordinates in chosen coordinate system
- The Sigmas row shows an estimated accuracy
- In the A Priori row, there is an averaged in Single mode position taken from the RINEX header
- The Estimated - A Priori row displays the accuracy from this position specified in the RINEX header

## Setting up obtained base coordinates in ReachView

If you need the acquired coordinates to use them as the base position for RTK/PPK, you can now enter the base coordinated into ReachView.

- In ReachView, go to *Base mode* tab
- In the Base coordinates input mode, choose Manual
- Set up the required data format (LLH or XYZ)
- Enter the coordinates and specify the antenna height

!!! note ""

    You may need to convert the solution you get to WGS84.

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/Bluetooth.png" style="width: 600px;"></div>

If you experience any difficulties during the processing or want to discuss the workflow, start a thread at the [Emlid community forum.](https://community.emlid.com/)

Further reading:

- [How RTK works](../../common/tutorials/rtk-introduction.md)
- [How PPK works](../../common/tutorials/ppk-introduction.md)
- [GPS Post-processing](../../common/tutorials/gps-post-processing.md)
- [Placing the base](../../common/tutorials/placing-the-base.md)

<p style="font-size:70%;"><a name="myfootnote1">1</a>: About OPUS: NOAA’s National Geodatic Survey site. URL:  https://www.ngs.noaa.gov/OPUS/about.jsp</p>

<p style="font-size:70%;"><a name="myfootnote2">2</a>: Tools and Applications: Natural Resources Canada site. URL: https://www.nrcan.gc.ca/maps-tools-publications/tools/geodetic-reference-systems-tools/tools-applications/10925#ppp</p>

