## Overview

From the [RTK basics](/common/tutorials/rtk-introduction) follows that RTK technique requires 2 receivers: one acting as the base and one as the rover. Sometimes CORS and NTRIP networks take the place of traditional base stations. They provide accurate absolute position and send corrections over the Internet. Typically the distance between the reference station and local rover shouldn't exceed 10-15 km due to the ionospheric effect. So if the reference station is located too far or simply is absent in the area you will need a local base station. Another advantages of your own base are independence from the Internet connection and lack of NTRIP subscription fees.

If you are setting up your own base it is necessary to pay attention to this article. A good understanding of different ways to set up the base will help you to reach desired accuracy for your application.


## Absolute and relative position
ReachView has several way to determine or set the base station position providing different accuracy. Let's take a look at the illustration below (figure 1). RTK algorithm precisely calculates the distance between base and rover, this distance is called Baseline. The Rover position is  precisely determined relatively to the Base position. In the same time the rover coordinates offset from the real location depends on the position accuracy of the base. If the position that has been set in the base station is different from the actual True position  on earth the offset equal to this difference will be in the rover position as well.  

<p style="text-align:center"><img src="../img/reach/placing-the-base/position.png" style="width: 800px;"/></p> 
_Figure 1_  
<br>
It is often enough to know precise position of an object relatively to base station but for some applications like survey and mapping it is fundamental to get accurate absolute position. In this case the offset ΔX, ΔY, ΔZ between actual True position and the Base station position  should be avoided or reduced.
<br>

!!! attention
    Absolute position of rover is accurate only to the same accuracy as the position of the base station.

Proper positioning of the base station is a key to successful data collection. The shift of base coordinates will keep the collected data precise but will make it inaccurate (which is absolutely fine for volumetric measurements but unacceptable if you have to tie collected data to the global coordinates). For example if you are processing the map using data collected by RTK-equipped drone using corrections from the shifted base your map will be later geo-referenced with the same offset (figure 2).

<p style="text-align:center"><img src="../img/reach/placing-the-base/absolute-shift.png" style="width: 800px;"/></p> 
_Figure 2_  
<br>
The same shift producing effect may be noticed if the base is placed inaccurately over a known point or just moved from it's determined position without relevant amendments.

!!! success "Useful note"
    If the accurate absolute position of the base has been determined only after the job has been done, the offset of the map can be determined and corrected. 


## Ways to set the base

As already mentioned Reach and Reach RS used as a base may be positioned using different ways. You can manually enter the base coordinates, use averaging feature or use PPP and PPK techniques to determine the coordinates.

| Base setup method         | Accuracy        | Requirement                   | Observation time | Processing time                                                              | Cost                                |
|---------------------------|-----------------|-------------------------------|------------------|------------------------------------------------------------------------------|-------------------------------------|
| Manual, on a known point  | as of the point | Known point                   | 0 min            | Immediate, no processing required                                            | Free                                |
| Average single position   | ~2.5 m           |                               | &lt;5 min            | Immediate, processing on Reach                                               | Free                                |
| RTK FIX position          | 7mm+1mm/km      | NTRIP stream from base &lt;15km  | &lt;5 min            | Immediate, processing on Reach                                               | Free/$$ depending on local provider |
| RTK Float position        | 1.0m            | NTRIP stream from base &lt;100km | &lt;15 min           | Immediate, processing on Reach                                               | Free/$$ depending on local provider |
| Post-Processed Kinematic  | 7mm+1mm/km      | RINEX logs from base &lt;100km   | ~1 h              | 15min on PC after log from reference station available, usually posted hourly | Free/$ depending on local provider  |
| Precise Point Positioning | ~30cm           |                               | ~4 h              | In ~24h after submitting logs to NRCan online service                        | Free                                |

_Numbers in the table are approximate and only for reference purposes. Your experience may vary in different conditions, always follow appropriate survey practices!_ 

<br>

No matter which method you use relative position of the rover will always be cm-precise, the actual accuracy will be set by the accuracy of the base position.

!!! tip
    Refer to [Base mode tab of ReachView tutorial](/common/reachview/base-mode/#base-position) to learn how to configure different ways of setting up the base with ReachView.
 
#####Manual
Manual input of the position is rather straightforward and is used when you have access to a known point. The most popular scenarios include finding a trig point or hiring a surveyor who will set the benchmark point. In this case absolute accuracy depends on how accurately the point's coordinates were determined.
<p style="text-align:center"><img src="../img/reach/placing-the-base/trig.jpg" style="width: 800px;"/></p> 
_Triangulation station also known as trig point or trig beacon with Reach RS on top (photo by Luke Wijnberg)_
<br>

Pay attention and carefully place the base over a known point and measure the height of the antenna from the mark. It will help to avoid shifts from the absolute position and keep measurements accurate. Refer to [Placing Reach and Reach RS in the field](#placing-the-base-station-in-the-field) for detailed instructions.
 
#####Average
Let’s take a closer look at setting up the base using the position averaging with single, float and fix solutions. All these ways provide different levels of base coordinates accuracy and are suitable for different applications.
 
####Averaged single 
This approach is used when you don't require absolute accuracy. The averaging happens in stand-alone GPS mode without using any corrections and this provides you with a several meters absolute accuracy.
 
The left illustration below (see figure 3) shows rover passes the same path few times and receives the corrections from the base configured using averaged single solution. While the position for each individual pass lies within the receiver precision limits, the absolute position may differ by up to few meters. We can see this if we repeat averaging of static base station several times and build the same path after each reaveraging, take a look on the right of figure 3.  

<p style="text-align:center"><img src="../img/reach/placing-the-base/averaged-single.png" style="width: 800px;"/></p> 
_Figure 3_  
<br>

!!! success "Perfect for repeatable precise relative positioning (GPS tractor guidance, autonomous flights and landing)"
    If you need accurate relative only positioning the easiest way is to average the position using single solution. Just physically mark point on the ground and save coordinates to manual in ReachView. Day-to-day result would have looked almost identical to those of the obtained using NTRIP corrections.
 
#### Averaged float and fix

Averaging RTK fix solution is way more accurate than single averaging and becomes possible when the receiver used as the base is configured to obtain NTRIP corrections over the Internet. This might be useful if the reference station is located too far and reducing baseline by installing the local base improves positioning performance of rover.  

<p style="text-align:center"><img src="../img/reach/placing-the-base/averaged-float.gif" style="width: 600px;"/></p>
 
On the left of the next illustration (see figure 4) the rover passes the same path and receives the corrections from the base configured using averaged fix position.  
When the base is set up using averaged fix solution, the coordinates are determined with a centimeter accuracy (if obtaning survey-grade NTRIP corrections). In this case the deviations of the each path built immediately after reaveraging several times will be within few centimeters, take a look at figure 5. 

<p style="text-align:center"><img src="../img/reach/placing-the-base/averaged-fix.png" style="width: 800px;"/></p> 
_Figure 4_  
<br>

If the baseline is too long to obtain fix, averaging float solution will still improve the position to ~1m level. 

!!! success "Perfect for data collection and surveying, placing GCPs and drone mapping"
    The base position averaged using fix solution provides several centimeters accuracy and works great when you need accurate absolute position!
 
 
#### Post-Processed Kinematics
With post processed kinematics technique you may determine base coordinates without real-time corrections with centimeter accuracy. You will need RINEX logs from the reference station in the area of 100km. The process will take you about 15 minutes to calculate the position of your base station using PPK tutorial from the docs.

General steps: 

* Enable [logging of raw data](/common/reachview/logging/) and record log for a about an hour
* Exort log with the collected data from ReachView to your PC
* Refer to [PPK tutorial](/common/tutorials/gps-post-processing)
* After you get the coordinates you may enter them manually in Base coordinates section. **Comparing PPK position to the averaged position and applying corrections to the collected data is the way to compensate the shift shown in the example on figure 2**.


#### Precise Point Positioning

With precise point positioning technique you may accurately determine base coordinates anywhere in the world without real-time correction or base station nearby however it may take a considerable time to get coordinates.

General steps:

* Enable [logging of raw data](/common/reachview/logging/) and record log for a few hours 
* Export log with the collected data from ReachView to your mobile device or PC
* Upload the collected file to PPP service (for example [NRCAN](https://webapp.geod.nrcan.gc.ca/geod/tools-outils/ppp.php))
* After you get the coordinates you may enter them manually in Base coordinates section.

 
### Placing the base station in the field 

!!! Danger "Pay Attention!"
    The mismeasured height of the antenna above the mark is probably the most pervasive and frequent blunder in GPS control surveying.

#### Placing Reach RS (Figure 4)

* Make sure your Reach device is placed precisely above the marked point on the tripod and leveled
* If you are setting up base coordinates manually measure the antenna height offset

!!! note " " 
    Antenna height is measured as the distance between the mark and the antenna reference point (ARP). 

 For Reach RS consider the antenna height as the distance between mark and the bottom of Reach RS (h on figure 4) plus 65 mm.

<p style="text-align:center"><img src="../img/reach/placing-the-base/placing-reach-rs.png" style="width: 800px;"/></p>  
_Figure 4_
 <br>

* When you securely placed Reach RS over the mark, you are ready to set or determine its position.

#### Placing Reach (Figure 5)

* Place Tallysman antenna on the ground plane as described in [Reach Antenna placement section](https://docs.emlid.com/reach/antenna-placement/#ground-plane).
* Make sure Reach antenna is placed precisely above the marked point on the tripod and leveled
* If you are setting up base coordinates manually measure the antenna height offset. For Tallysman antenna going with Reach, ARP is the bottom surface. 

<p style="text-align:center"><img src="../img/reach/placing-the-base/placing-reach.png" style="width: 800px;"/></p>  
_Figure 5_
 <br>

* When you securely placed Reach antenna over the mark, you are ready to set or determine its position.

 
### Storing the base position
 
If you want to reuse the determined base location:

* Carefully mark physical position on the ground
* Save coordinates to manual using the button in Base Coordinates section of Base mode tab
* When using this position next time, accurately place the base station over the mark
* Enter the recorded coordinates manually in ReachView
 

