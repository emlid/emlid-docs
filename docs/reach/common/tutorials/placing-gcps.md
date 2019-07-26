# Placing GCPs in RTK mode

To place GCPs with Reach units follow the steps from this guide.

### Configure RTK

* If you have 2 Reach RS2, [this video will guide you on how to set them up in RTK](https://youtu.be/-K32ayVmH6U)
* If you have 2 Reach RS/RS+, set RTK settings by [following "Base and rover setup" video guide](https://youtu.be/4GfUDoDwEAE)
* If you have just one Reach receiver, you need to connect it to NTRIP first. [Check this guide for more details](../../tutorials/ntrip-workflow/)

### Create a project

Create a project in ReachView Survey tool by [following "Creating New Project" guide.](../../reachview/survey/#creating-new-project)

### Fix target

Put your pole in the center of the target.

<div style="text-align: center;"><img src="../img/reach/placing-gcps/placing-gcp.jpg" style="width: 800px;"></div>

!!! tip ""
	Level your pole using a bubble level.


### Collect point

In ReachView Survey tool press the *Collect* button and save your GCP. Repeat the procedure for as many GCPs as you need.

!!! tip ""
	[More info about Survey tool functionality you can find here](../../reachview/survey/)

### Export

* Specify the GCPs data format which your GIS or photogrammetry software can handle 
* [Export your project file in one of the suitable formats](../../reachview/survey/#exporting-data)
