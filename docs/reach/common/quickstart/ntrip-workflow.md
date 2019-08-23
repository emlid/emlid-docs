#Working with NTRIP service

##Overview

This guide explains how to configure Reach to get correction messages from NTRIP service.

!!! tip ""
	NTRIP correction input setup can be done at home before the survey. In that case, you just need to connect Reach to the Internet in a field.

##Update Reach

If you just received your Reach, you need to update it to make sure you have all the latest features. The instruction is in a carry case Reach comes with. 

You can also find the tutorial in [documentation](../../../quickstart/first-setup/) or follow the video guide:

<center>

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/fIY__hNjcNI" allowfullscreen></iframe></div>

</center>

##Connect Reach to the Internet

Reach requires the Internet connection to work with NTRIP. You don’t need any special devices or software for that, only a smartphone with a hotspot feature.

Turn on mobile data on your smartphone and share it over Wi-Fi hotspot. Reach will connect to your network and get access to the Internet.

[Check the tutorial for more information about how to connect Reach to other networks.](../connecting-to-the-internet/)

##Configure Reach for RTK mode with NTRIP

Open ReachView and go to **RTK settings**. Set everything to the same options as on the screenshot below.

!!! note ""
	In the **GNSS select** section pick either Galileo or Beidou depending on your location. While Glonass covers most of the world, Beidou might be more efficient in the Asia-Pacific region. In this example we use Glonass.

Apply changes.

<div style="text-align: center;"><img src="../img/quickstart/ntrip-workflow/rtk-settings.png" style="width: 800px;"></div>

Now go to **Correction input** tab, select **NTRIP** and fill in the information from your provider. Choose the nearest reference station to receive the corrections from.

!!! tip ""
	Check the website of your NTRIP provider to find out which mount point suits you better. 

<div style="text-align: center;"><img src="../img/quickstart/ntrip-workflow/ntrip-correction-input.png" style="width: 600px;"></div>

!!! note ""
	If you are using VRS service, you might need to enable GGA messages. 

Press **Apply**.

##Provide Reach with a clear sky view

Reach RS needs to have a clear view of the sky approximately 30 degrees above the horizon. There should be no obstacles that could block the view like buildings, trees, cars, humans, laptops etc.

<div style="text-align: center;"><img src="../img/quickstart/ntrip-workflow/skyview-obstacles.png" style="width: 800px;"></div>

[Learn more about Reach setup in the Placement section of Reach RS+ docs](https://docs.emlid.com/reachrs/placement/)

##Collect and export data

Check tutorials on how to create new projects, collect and stake out points, import and export projects:

* [New project](../../reachview/survey/#creating-new-project)
* [Survey tool overview](../../reachview/survey/#survey-tool-interface)
* [Point collection](../../reachview/survey/#collecting-the-point)
* [Stakeout](../../reachview/survey/#point-stakeout)
* [Project import](../../reachview/survey/#points-import) and [export](../../reachview/survey/#exporting-data)

