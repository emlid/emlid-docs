You can collect points with the Reach Panel app using Point Collection tool. The feature allows to make project-based point collection with auto-save rules or manually and then export the data into different formats. 

!!! tip ""
    The tool is perfect for surveying and ground control points collection. 

###Creating New Project

* Go to Reach rover with a browser or Reach Panel mobile app
* Choose the Survey tab in the menu
* To create a new project press *New project* or click on the project name to open it

<p style="text-align:center" ><img src="../img/reachview/survey/create-new-project.gif" style="width: 800px;" /></p>


###Project settings 

####Basic information

On the first step, you can fill in Project name, Author and add Comment if you want. However, you can use default settings and press *Next* button.

<p style="text-align:center" ><img src="../img/reachview/survey/step1-fill-in.gif" style="width: 800px;" /></p>

####Auto-save rules

Auto-save rules are set for Single, Float or Fix statuses and allow to automate point collection process. 

To configure auto-save rules:

* Select the solution status at which the device will save points automatically by clicking on the checkbox
	
	The menu with settings will open. You can use recommended default values for the required observation time, precision and DOP or set yours.

	#####Default observation time
	| Solution status  | Time |
	| :-------------: | :-------------: |
	| Fix  | 40 sec  |
	| Float  | 5 min  |
	| Single  | 10 min  |

	#####Precision
	This parameter indicates the highest possible RMS error within the measurement. The deviation for the single solution is usually several meters, with the float solution you may expect sub-meter precision, with the fix status you can get centimeter-level precision.

	#####DOP
	DOP stands for “the dilution of precision” and specifies the effect of satellite geometry on measurement precision. The better the geometry - the lower the DOP value. For auto-save rules default value is 2, when DOP is higher it is not recommended to collect points as bad satellite geometry might affect accuracy.

* If you don’t need auto-saving, you can click *Done* to go further. In that case, you will need to start and stop point collection manually

<p style="text-align:center" ><img src="../img/reachview/survey/step2-auto-save-rules.gif" style="width: 800px;" /></p>


####Survey tool interface

Survey tool interface shows the map with base and rover on it. 

* **B** stands for the base station
* **R** stands for the rover

<p style="text-align:center" ><img src="../img/reachview/survey/map-rover-icon.gif" style="width: 800px;" /></p>

####Antenna height setup

* Press <img src="../img/reachview/survey/antenna-height-icon.svg" align="center" /> to open the Pole height menu
* If you use thread adapter, check the box

!!! note ""
	Reach RS2 has an industry-standard 5/8" mount and doesn't require a thread adapter

* Change pole height in the next form if it differs from the standard 2m value
* Press the *Save* button

<p style="text-align:center" ><img src="../img/reachview/survey/antenna-height.gif" style="width: 800px;" /></p>

####Collecting the point

* Press <img src="../img/reachview/survey/new-point-icon.svg" align="center" /> to go to the next window
	
	You can set the point’s name or use the default value. If you leave the name field blank the default point name will be “Point 1”, “Point 2”, etc.

	!!! note ""
    	You can also set the new Pole height value if it changed.

* Press *Collect* to start point collecting process

<p style="text-align:center" ><img src="../img/reachview/survey/start-point-collecting.gif" style="width: 800px;" /></p>

If you set Auto-save rules, you will see the status bar indicating the time until the end of point collection. Otherwise, you need to stop collecting point by pressing the *Accept* button.

!!! danger ""
    If the *Collect* button is unavailable and you see the message “Waiting for solution status”, you won’t be able to start point collection. Check the solution status.

You can stop the process by pressing the *Cancel* button. In that case, the point will not be saved.

* If you want to end surveying or look at the result, press the *Back* button.
You will see the map with all the points you have collected

<p style="text-align:center" ><img src="../img/reachview/survey/back-button.gif" style="width: 800px;" /></p>

####Point options

To open the list of all points, press <img src="../img/reachview/survey/points-list-icon.svg" align="center" />. You can open point details, edit the point info, find it on the map or stake out the point.
[Read more about Stake out function in our guide](#point-stakeout).

<p style="text-align:center" ><img src="../img/reachview/survey/list-all-points.gif" style="width: 800px;" /></p>

Also, you can work with each point separately by choosing it on the map. 

<p style="text-align:center" ><img src="../img/reachview/survey/point-options.gif" style="width: 800px;" /></p>

When the surveying is done, press <img src="../img/reachview/survey/back-button-icon.svg" align="center" /> to close and save the project. It will be available in Survey tab menu.

<p style="text-align:center" ><img src="../img/reachview/survey/close-project.gif" style="width: 800px;" /></p>

####Exporting Data

When you finish collecting points, you can export your project in CSV, DXF, GeoJSON, DroneDeploy CSV or ESRI Shapefiles format.

To do it, press •••, click *Export* and choose the right format. The downloading will start automatically. Large projects might take some time to process. After that, you can find your archive in the default Downloads folder.

!!! note ""
	If you use Reach Panel app on Android, exporting will be made in a Downloads folder. As for iOS, you will need to choose the way you want to save your project.

<p style="text-align:center" ><img src="../img/reachview/survey/export-button.gif" style="width: 800px;" /></p>

It is also possible to export your project in Survey tab without opening it. Click the *Export* button in the project window and choose the format as in a previous way.

## Point stakeout

Point stakeout is a feature that allows finding points with known coordinates.

### Preparing data

Open the Survey tab in Reach Panel.

<p style="text-align:center" ><img src="../img/reachview/survey/survey.png" style="width: 800px;" /></p>

* If there is a ready project, click to the project name to open it

* If you don’t have any projects or want to create a new one, [check Creating New Project part of this article](#creating-new-project)

You can use coordinates collected earlier or just upload a list with required points.

#### Points import

Hit ••• button on the right side of the project name and choose *Import* in the drop-down list.

<p style="text-align:center" ><img src="../img/reachview/survey/import-points-1.gif" style="width: 800px;" /></p>

You can upload files in CSV, GeoJSON or DXF formats or just enter coordinates manually. 

!!! note ""
	Check the templates to find out what exactly your data should look like.

	??? note "CSV template"
		    name,longitude,latitude,elevation
		    Point 1,30.339,59.958,53.618
		    Point 2,30.334,59.960,58.944

	??? note "GeoJSON template"
		    {
		      "type": "FeatureCollection",
		      "crs": {
		        "type": "name",
		          "properties": {
		            "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
		          }
		       },
		      "features": [
		        {
		          "type": "Feature",
		          "properties": {
		            "name": "Point 1"
		          },
		          "geometry": {
		            "type": "Point",
		            "coordinates": [ 30.339, 59.958, 53.618 ]
		          }
		        },
		        {
		          "type": "Feature",
		          "properties": {
		            "name": "Point 2"
		          },
		          "geometry": {
		            "type": "Point",
		            "coordinates": [ 30.334, 59.960, 58.944 ]
		          }
		        }
		      ]
		    }

After you finish adding coordinates, hit the *Import* button.

<p style="text-align:center" ><img src="../img/reachview/survey/import-points-2.gif" style="width: 800px;" /></p>

### Interface

Tap the point you want to stake out. It will be highlighted in blue. At the bottom of the screen, you will see point description that includes the name of the point, point collection UTC date and time and solution status.

Hit the *Stake out* button to start.

<p style="text-align:center" ><img src="../img/reachview/survey/start-stakeout.gif" style="width: 800px;" /></p>

Let’s get in touch with the stake out interface before proceeding.

<p style="text-align:center" ><img src="../img/reachview/survey/stakeout-interface.PNG" style="width: 800px;" /></p>

* You can see [solution status](../../reachview/status/#solution-status), [AR ratio](../../reachview/status/#ar-validation-ratio), [age of differential](../../reachview/status/#age-of-differential), satellite number and [Reach name](../../reachview/settings/#change-reach-name) in the status bar placed in the top of the page. Make sure you have Fix
* The antenna height value can be found under the status bar
* In this mode, the map is always North-oriented
* There’s a dark-gray field at the bottom of the window. The left value is the horizontal distance to the point, the right value is vertical
* *Done* button finishes the stakeout
* There are other points you can switch under the distance values

### Staking out points

Try to move in the direction to the point. The map zooms in automatically. 

!!! tip "How to understand in which direction the point is?"
	Once start walking, you will see Rover symbol changes to the arrow.

When the distance to the point is less than 50 centimeters (1.64 feet), stakeout changes the mode.

You need to put a blue rover circle into the white ring by moving the pole. Ensure the pole isn’t tilted. Does rover circle become green? Good job! We have almost finished.

<p style="text-align:center" ><img src="../img/reachview/survey/stakeout-process.gif" style="width: 800px;" /></p>

Here you also can choose the **2D** or **3D** option. **2D** stands for latitude and longitude coordinates only. With **3D** you can also find the height of the point.

<p style="text-align:center" ><img src="../img/reachview/survey/2D-3D.gif" style="width: 800px;" /></p>

Congratulations! You’ve just staked out your first point! Now you can switch to another point to continue or hit *Done* button to finish.

## To-Dos

Survey Tool is constantly improving. Many features including new export formats, new project settings are coming soon. The discussion, including questions and feature request, is available on [the community forum](https://community.emlid.com).




