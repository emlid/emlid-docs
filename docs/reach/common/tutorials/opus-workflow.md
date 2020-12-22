# NOAA's Online Positioning User Service (OPUS)

Online Positioning User Service (OPUS) is provided by the National Oceanic and Atmospheric Administration (NOAA). With OPUS you may accurately determine the coordinates of a static point anywhere on the territory of the United States without real-time corrections or base station nearby.

!!! tip "" 
    You can use OPUS with Reach RS2 and Reach M2 only. To process data from Reach RS+, use the NRCAN CSRS-PPP service. [More details are in the PPP guide.](ppp-introduction.md)

In this guide, we will walk you through the following steps:

- Recording RINEX data on Reach
- Exporting raw data from ReachView to your mobile device or PC
- Uploading the collected file to OPUS
- Entering the obtained base coordinates into ReachView

The equipment you need to accomplish the survey:

- Reach receiver
- Tripod

## How OPUS works

A receiver in a standalone positioning mode finds out its position relying on the data obtained from satellites only. Along with raw data, it also gets navigation messages containing such data as satellite clock offset, the ionospheric and tropospheric corrections, etc. When the corrections from the base are received, these offsets are eliminated as both receivers work in the same conditions.

OPUS allows the single receiver to achieve high-level accuracy without the use of corrections from the base station. To calculate the coordinates, OPUS uses corrections from the National Spatial Reference System (NSRS). OPUS works with software that uses data from the NOAA CORS Network for computations. This network of Continuously Operating Reference Stations (CORS) provides Global Navigation Satellite System (GNSS) data consisting of carrier phase and code range measurements in support of three dimensional positioning, meteorology, space weather, and geophysical applications. 

Thereby, the Single receiver might determine its position with a centimeter-level accuracy using only its own raw data and precise ephemerides and clock offsets provided by a NSRS.

The coordinates are the average of three independent, single-baseline solutions, each computed by double-differenced carrier-phase measurements from one of three nearby CORSs.

## NOAA's OPUS service overview

OPUS service uses dual-frequency GPS data for solution computation and supports the Static mode only. The Static data is required to be recorded on the stationary unmoving receiver.

There are 2 ways you can process the data in OPUS:

- Static (for data that are 2 to 48 hours in duration)
- Rapid-Static (for data that are 15 minutes to 2 hours in duration)

The Static and Rapid-Static methods use different processing software and provide pretty similar horizontal accuracy. The Rapid-Static processing has more strict requirements for the data quality in comparison with the Static approach. Moreover, Rapid-Static processing is available only for some regions<sup>[1](#myfootnote1)</sup>.

!!! note ""
    In this guide, we will show you how to process raw data from Reach RS2 using the Static method.

You can learn more about NOAA's OPUS service on their [official site.](https://www.ngs.noaa.gov/OPUS/about.jsp)

## Placing the Reach

Place a Reach device precisely above the marked point on the tripod and level it. [Learn more about placing Reach receiver in this docs entry.](placing-the-base.md)

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/placing-reach-rs2.png" style="width: 600px;"></div>

## Recording RINEX data on Reach

- Go to the *RTK Settings* tab
- Choose **Static** Positioning mode, enable **GPS** only and set up the update rate to **1 Hz**
- Navigate to the *Logging* tab
- Select RINEX 2.XX **Raw data** format
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

[Learn more about downloading files from Reach in this docs entry.](../reachview/logging.md#downloading)

## Converting UBX logs to RINEX

In case you log raw data in UBX format, you can convert them manually in RTKLIB.

- Start **RTKLIB RTKCONV**
- Add your rover raw log in the first field and choose output directory
- Choose format of your log in pop-down menu. Set format to u-blox

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/RTKCONV.png" style="width: 600px;"></div>

- Push the **Options** button
- Choose RINEX Version 2.XX
- Turn on GPS satellite system only
- Enable L1 and L2 frequencies in the Frequencies tab

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/RTKCONV-Options-OPUS.png" style="width: 600px;"></div>

- Click on the **OK** button to save changes
- Push on the **Convert** button to start conversion process

In the result, you will get the *.obs and *.nav files.

## Submitting data to NOAA's OPUS service

- Go to the [NOAA's OPUS site](https://www.ngs.noaa.gov/OPUS/)
- Click on the **Choose file** button and browse for raw*.obs file you would like to process
- If you work with Reach RS2, choose the `EML_REACH_RS2 NONE` in the Antenna field
- Type a pole height in the Antenna Height box
- Enter your email address to get the results
- Click on **Upload to Static** button to submit the data

<div style="text-align: center;"><img src="../img/reach/ppp-introduction/OPUS.png" style="width: 600px;"></div>

OPUS will send the file with the solution to your email address.

## Results assessment

After you get the solution report, it might be useful to check how accurate the results are.

In the solution report, you will get the name of the used reference frame, the XYZ and LLH coordinates of the point and accuracy estimation in meters. Additionally, you can check these fields: OBS USED, FIXED AMB, OVERALL RMS.

The most accurate OPUS solutions have the following characteristics:

- Over 90% of observations are used
- Over 50% of ambiguities are fixed
- Overall RMS is less than 3 cm

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

- [How RTK works](rtk-introduction.md)
- [How PPK works](ppk-introduction.md)
- [GPS Post-processing](gps-post-processing.md)
- [Placing the base](placing-the-base.md)
- [Precise Point Positioning](ppp-introduction.md)

<p style="font-size:70%;"><a name="myfootnote1">1</a>: About OPUS: NOAA’s National Geodatic Survey site. URL: https://www.ngs.noaa.gov/OPUS/about.jsp</p>