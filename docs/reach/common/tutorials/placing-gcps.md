# Placing GCPs in RTK mode

To place GCPs with Reach units follow the steps from this guide.

### Configure RTK

??? note "Setting RTK on Reach RS2 base and rover over LoRa radio"

	If you have 2 Reach RS2, this video will guide you on how to set them up in RTK:

    <center>

	<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/-K32ayVmH6U" allowfullscreen></iframe></div>

	</center>

??? note "Setting RTK on Reach RS+ base and rover over LoRa radio"

	If you have 2 Reach RS/RS+, configure RTK by following "Base and rover setup" video guide:
        
	<center>

	<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/4GfUDoDwEAE" allowfullscreen></iframe></div>

	</center>

??? note "Setting RTK on Reach rover over NTRIP"
	If you have just one Reach receiver, you need to connect it to NTRIP first. [Check this guide for more details](../../quickstart/ntrip-workflow/)

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
