# Placing GCPs in RTK mode

To place GCPs with Reach RS/RS+ follow the steps from this guide.

### Configure RTK

* If you have 2 Reach RS/RS+, set RTK settings by [following "Base and rover setup" video guide](https://youtu.be/4GfUDoDwEAE)
* If you have just one Reach RS/RS+, you need to connect it to NTRIP first. [Check this guide for more details](/common/tutorials/ntrip-workflow/)


### Create a project

Create a project in ReachView Survey tool by [following "Creating New Project" guide.](/common/reachview/survey/#creating-new-project)

### Fix target

Put your pole in the center of the target.

<div style="text-align: center;"><img src="../img/reach/placing-gcps/placing-gcp.jpg" style="width: 800px;"></div>

!!! tip ""
	Level your pole using a bubble level.


### Collect point

In ReachView Survey tool press the **Collect** button and save your GCP. Repeat the procedure for as many GCPs as you need.

!!! tip ""
	[More info about Survey tool functionality you can find here](/common/reachview/survey/)

### Export

* Specify the GCPs data format which your GIS or photogrammetry software can handle 
* [Export your project file in one of the suitable formats](/common/reachview/survey/#exporting-data)
