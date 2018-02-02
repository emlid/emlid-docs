You can collect points with the ReachView app using Point Collection tool. The feature allows to make project-based point collection with auto-save rules or manually and then export the data into different formats. 

!!! success " "
    The tool is perfect for surveying and ground control points collection. 

###Creating New Project

####Basic information

To start a new project select Survey tab in ReachView and click on the "New Project" button. Name your project and assign an author, you can specify the additional details in comment section. Submit basic information by clicking "Next" button.

<p style="text-align:center" ><img src="../img/reachview/survey/new-project.gif" style="width: 800px;" /></p>


####Project settings 

On this step choose the projection. Currently you can use EPSG:4326 (WGS84 Latitude, Longitude and Height) projection.

!!! attention
    The projection cannot be changed after project creation is done.

In this section you can also specify the default height of antenna, which is actually the distance between the antenna and the point being measured (h on the scheme below).

<p style="text-align:center" ><img src="../img/reachview/survey/height.png" style="width: 500px;" /></p>

This parameter can be manually changed for each point before its collection. 

<p style="text-align:center" ><img src="../img/reachview/survey/project-settings.gif" style="width: 800px;" /></p>


####Auto-save rules

With the point collection tool you may get points manually or use auto-save rules. If you want to collect manually- you can skip this step.  
The rules are individual for SINGLE, FLOAT and FIX statuses and may apply to the specific solution.

The rule settings include three parameters:

* Required observation time  

* Precision  
This parameter indicates the highest possible RMS error within the measurement. The deviation for single solution is usually several meters, with the float solution you may expect sub-meter precision,  with the fix status you can get centimeter level precision.

* DOP  
DOP stands for “the dilution of precision” and specifies the effect of satellite geometry on measurement precision. The better the geometry - the lower the DOP value. For auto-save rules default value is 2, when DOP is higher it is not recommended to collect points as bad satellite geometry might affect accuracy.

#####Example settings for auto-save rules

Let’s create auto-save rules for FLOAT and FIX statuses.  
Observation time for float solution is 2 minutes and 20 seconds, the precision is 0.5 meters and DOP is equal 2.  
For the fixed solution we set the time value of 20 seconds, the precision is 0.005 meters and DOP is 2.

<p style="text-align:center" ><img src="../img/reachview/survey/auto-save.gif" style="width: 800px;" /></p>


!!! note
    Auto-save rules configuration in this example is shown for demonstration purposes.


The point will be collected automatically after 20 seconds of observation if the DOP doesn’t exceed 2 and the RMS deviation is less than  0.005 meters. In case the solution is floating, the observation time will be 2:20 with the same conditions.

After auto-save rules configured, we can click "Done" button and move to project view and survey tool interface. 

###Survey tool interface
Point collection tool interface shows the project settings, auto-save rules and the list of points collected. The map below will show collected points. 
In the right upper  corner of the screen you’ll find project export icon.

!!! attention
    In the current version you can’t edit project parameters you’ve initially specified, this opportunity will be added in the next release.


###Collecting the point
* To collect a new point use the green button in the right bottom of the screen. 
* In a new window you’ll see the status section with real-time RTK and averaging statuses.
* In the Point settings tab specify name (if you leave it blank the default point name will be “Point 1”, “Point 2”, etc).
* Set antenna height if you didn’t do it in projects settings or if the height changed. 
* When everything is ready check the status bar along with the green "Collect" button in the bottom of the screen.

<p style="text-align:center" ><img src="../img/reachview/survey/project.gif" style="width: 800px;" /></p>


If the status bar is red and you see the message “Waiting for status” , you won’t be able to start point collection. The tool needs satellites visibility, at least single status is needed.
If the status bar is green, click "Collect" to start point collection.  
If you start point collection and the auto-rule for current status is enabled, status bar in the bottom will show countdown of required observation time. As the time passes, the point will be automatically captured. **Don’t forget to click "Save&Go" to save the point!**  
If you want to collect point manually just press "Accept" button during the collection. Your point will be stored and you can move to the next one.

<p style="text-align:center" ><img src="../img/reachview/survey/manual-collect.gif" style="width: 800px;" /></p>


###Exporting Data

Before export you can delete useless points from the list in the project interface. By clicking on each point you can see its description and coordinates.  
When you’re done with point collection you may export points from the project to CSV, DXF, GeoJSON, ESRI shapefiles. Large projects might take some time to process.

<p style="text-align:center" ><img src="../img/reachview/survey/export.gif" style="width: 800px;" /></p>


## To-Dos

Survey Tool is constantly improving. Many features including new export formats, new project settings are coming soon. The discussion, including questions and feature request, is available on [community forum](https://community.emlid.com).




