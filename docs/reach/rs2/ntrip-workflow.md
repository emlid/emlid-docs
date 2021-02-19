#Working with NTRIP service

##Overview

This guide explains how to configure Reach to get correction messages from NTRIP service.

!!! tip ""
	NTRIP correction input setup can be done at home before the survey. In that case, you just need to provide Reach with the Internet in the field.

## Update Reach

If you just received your Reach, you need to update it to make sure you have all the latest features. The instruction is in a carry case Reach comes with. 

You can also find the tutorial in [documentation](../../../quickstart/first-setup/) or follow the video guide:

<center>

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/Miy8L_1AgCQ" allowfullscreen></iframe></div>

</center>

## Video Guide

The video below covers the process of setting up Reach RS2 to receive RTK corrections over the Internet.

<center>

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/YWz0mhOwFAg" allowfullscreen></iframe></div>

</center>

## Text Guide

### Connect Reach to the Internet

Reach requires the Internet connection to work with NTRIP. 
	
There are 2 ways on how you can connect Reach RS2 to the Internet:

1. Insert a SIM card and enable Mobile data on Reach
2. Turn on mobile data on your smartphone and share it over Wi-Fi hotspot. Reach will connect to your network and get access to the Internet

Check the [tutorial](connecting-to-the-internet.md) for more information about how to provide Reach RS2 with Internet access.

### Configure Reach for RTK mode with NTRIP

Open ReachView 3 and go to *GNSS settings*. Set everything to the same options as on the screenshot below and apply changes.

<div style="text-align: center;"><img src="../img/reachrs2/ntrip-workflow/rtk-settings.png" style="height: 550px;"></div>

Now go to the *Correction input* tab, select *NTRIP* and fill in the information from your provider. Choose the nearest reference station to receive the corrections from.

!!! tip ""
	Check the website of your NTRIP provider to find out which mount point suits you better. 

<div style="text-align: center;"><img src="../img/reachrs2/ntrip-workflow/ntrip-correction-input.png" style="height: 550px;"></div>

!!! note ""
	If you are using VRS service, you need to enable *Send receiver's position to the provider*. 

Press *Apply*.

### Provide Reach with a clear sky view

Reach RS2 needs to have a clear view of the sky approximately 30 degrees above the horizon. There should be no obstacles that could block the view like buildings, trees, cars, humans, laptops etc.

<div style="text-align: center;"><img src="../img/reachrs2/ntrip-workflow/Reach-placement-correct-wrong.png" style="width: 800px;"></div>

Learn more about Reach setup in the [Placement](placement.md) section of Reach RS2 docs

### Collect and export data

Check tutorials on how to create new projects, collect and stake out points, import and export projects:

* [New project](../common/reachview/survey/#creating-new-project)
* [Survey tool overview](../common/reachview/survey/#survey-tool-interface)
* [Point collection](../common/reachview/survey/#collecting-the-point)
* [Stakeout](../common/reachview/survey/#point-stakeout)
* [Project import](../common/reachview/survey/#points-import) and [export](../common/reachview/survey/#exporting-data)

