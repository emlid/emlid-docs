## Required data

This tutorial requires:

* Raw logs from the rover
* Raw logs from the base
* (Optional) For absolute positioning: RINEX observations log from a reference station in range of 100 km
* (Optional) For processing improvement: precise ephemeris and clock files from the IGS
* Emlid version of RTKLIB

Download the latest version of Emlid RTKLIB for your system: 

| Win 64-bit | Linux 64-bit |
|------------|--------------|
| [Download](https://files.emlid.com/RTKLIB/RTKLIB-Win-x64.zip)   | [Download](https://files.emlid.com/RTKLIB/RTKLIB-qt-Linux-x64.zip)     |
| [md5](https://files.emlid.com/RTKLIB/RTKLIB-MD5SUMS)        | [md5](https://files.emlid.com/RTKLIB/RTKLIB-MD5SUMS)          |

Rover track is calculated relatively to the base station so in order to get rover track with correct absolute coordinates the exact position of the base station should be known. You either need to place base station on a point with known coordinate or determine it by post-processing base against a reference station in static mode. It is better if the station is within 100 km range, but longer range might work as well.


## Converting raw logs to RINEX (if needed)

!!! note
    If your raw logs from base and rover are saved in .ubx format you should convert them to RINEX. If you already have RINEX logs from the receivers you can skip this step.

Start **RTKLIB RTKCONV** after downloading raw files from Reach to your PC.

* Add your rover raw log in the first field and choose output directory.
* Choose format of your log in pop-down menu. Set format to u-blox if logs downloaded from each device. Otherwise, choose RTCM3 if base and rover logs were received from rover.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkconv_format.png" style="width: 600px;"></div>

* Push "Options" button.
* Choose "RINEX Version" 3.03.
* Turn on "Satellites Systems" you need.
* Press "OK" and "Convert" after.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkconv_options.png" style="width: 600px;"></div>

Now you should repeat the same with base log. Don't forget to change format.
After that you'll see something similar in your output folder.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkconv_output_folder.png" style="width: 600px;"></div>


### Calculating base position

Start **RTKLIB RTKPOST** software and enter the fields as shown here. If running for the first time you will need to set mode to Kinematic or Static in the options to unlock the fields for base station data. You can skip the start time, it is not compulsory.

* Choose rover .obs file for the Rover field (RINEX file from your rover).
* Select base station .obs file for the Base Station field (RINEX file from your base).
* Put base or rover .nav file in the third field.
* (Optional) You can as well add precise ephemeris and clocks at this stage. They are required for long baselines.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_adding_files.png" style="width: 600px;"></div>


Now proceed to the options by pushing "Options" button.

* Set positioning mode you need. Usually it's "Kinematic" or "Static".

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_setting1_mode.png" style="width: 600px;"></div>


* Choose "Elevation Mask" value. Usually it's 15-20.
* Push "SNR Mask" button and set the value you need. This will help you to avoid satellites with low signal strength.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_setting1_mask.png" style="width: 600px;"></div>


* Turn on "Rec Dynamics" to estimate receiver velocity and acceleration. Use it for DGPS/DGNSS or Kinematic modes.
* Select used navigation systems.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_setting1_dynamics.png" style="width: 600px;"></div>


* Go to the "Setting2" tab.
* Set "Integer Ambiguity Res" to Fix and Hold. In this mode continuously static integer ambiguities are estimated and resolved. If the validation OK, the ambiguities are tightly constrained to the resolved values.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_setting2_ambiguity.png" style="width: 600px;"></div>


* Set "Max Pos Var for AR" and turn on "AR Filter" on the right.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_setting2_ar.png" style="width: 600px;"></div>


* Switch to "Positions" tab.
* Select "Base Station". Choose "Average of Single Position" for any log to average single point solution or "RINEX Header Position" to use approximate position in RINEX .obs header.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_positions_base.png" style="width: 600px;"></div>


* Press "OK" button and "Execute" in the main window.
* You'll see green process bar. Wait until "done" label. It could take quite a lot of time if your logs are big. In that case window could not answer. Just chill and relax.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_execute.png" style="width: 600px;"></div>


After that you'll see something similar in your output folder. The .pos file with "__event" will contain timestamps if you had them during your job.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkpost_output_folder.png" style="width: 600px;"></div>

## Result visualization and analysis

Open **RTKLIB RTKPLOT** and drag and drop your .pos file.
If you see green points that mean that they're fix (Q=1), orange mean float (Q=2), red - single (Q=5).

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkplot_pos.png" style="width: 600px;"></div>


After that you could add .obs file to see more analyzing tools in pop-down menu.
For example, first image shows "Satellite Visibility" and second one "Position" in 3 directions.

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkplot_satvis.png" style="width: 600px;"></div>

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkplot_position.png" style="width: 600px;"></div>

If you've got time marks add them as a Solution-2 (File -> Open Solution2).

<div style="text-align: center;"><img src="../img/reach/post-processing/rtkplot_timemarks.png" style="width: 600px;"></div>


Looks really good, isn't it?

All log rights belong to our good friend and great surveyor Luke Wijnberg.

For more information about options read [RTKLIB manual](http://www.rtklib.com/prog/manual_2.4.2.pdf).

<!-- 


Now switch tab and set GPS AR to Fix-and-hold and Glonass to OFF. Glonass integer ambiguity resolution can be enabled if both base and rover are Reach.

![image](img/post-processing/Post3.PNG)

The observations RINEX from the reference station includes exact position in the header file, so we will choose it for the base position. This is very important because it is reference coordinate in the whole post-processing workflow. You need to have one known point to start from.

![image](img/post-processing/Post4.PNG)

Now you can hit execute and monitor solution quality, Q=1 means FIX.

![image](img/post-processing/Post5.PNG)

After computation is over press Plot to see the track. We got the base coordinate, write it down we are going to use it in the next step.

![image](img/post-processing/POst6.PNG)

### Calculating rover track

Browse to the rover obs (Rinex from your rover Reach), to the base station obs (Rinex from the base Reach) and to the nav (Rinex from your base Reach).

![image](img/post-processing/Post7.PNG)

Now proceed to the options and set positioning mode to Kinematic, that will tell RTKLIB that the receiver was moving. Select used navigation systems and set filter to combined. Enable dynamic filter as well.

![image](img/post-processing/Post8.PNG)

In this case Glonass ambiguity resolution can be set to ON, as both receivers are identical.

![image](img/post-processing/Post9.PNG)

Now we are at the point where we need to enter the coordinates of the base that we have calculated in the previous step.

![image](img/post-processing/Post10.PNG)

Hit execute and plot the resulting solution. Looks good, but some regions are yellow which indicates float solution. We can look at the observations to try to find the source of the issue.

![image](img/post-processing/Post11.PNG)

In RTKPLOT go to file-> open observations and select observations from the moving rover. Switch view to satellite visibility. You might need to go to the view options and select all satellite systems and set "cycle slip" to LLI flag to see data like this. We can notice that reception is worse in the beginning, so we can try to crop it to avoid feeding bad data in the filters.

![image](img/post-processing/Post12.PNG)

By switching view to Position it is evident that take off is around 14:05 and after this moment signal reception is much better.

![image](img/post-processing/Post13.PNG)

Let's try to process again, but crop data at 14:03.

![image](img/post-processing/Post14.PNG)

Looks really good now!

![image](img/post-processing/Post15.PNG)

What could have happened if we did not use the exact position of the base, but just averaged single position? The picture depict a close up of three turns, where green track has been processed with exact base station position specified and blue track has been processed without it. Both tracks are precise, but blue track has a shift of several meters.

![image](img/post-processing/Post16.PNG) -->


