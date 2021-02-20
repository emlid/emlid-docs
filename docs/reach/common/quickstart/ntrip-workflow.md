#Working with NTRIP service

##Overview

This guide explains how to configure Reach to get correction messages from NTRIP service.

!!! tip ""
	NTRIP correction input setup can be done at home before the survey. In that case, you just need to connect Reach to the Internet in the field.

##Update Reach

If you just received your Reach, you need to update it to make sure you have all the latest features. The instruction is in a carry case Reach comes with. 

You can also follow the video guide:

<center>

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/fIY__hNjcNI" allowfullscreen></iframe></div>

</center>

##Connect Reach to the Internet

Reach requires the Internet connection to work with NTRIP. You don’t need any special devices or software for that, only a smartphone with a hotspot feature.

Turn on mobile data on your smartphone and share it over Wi-Fi hotspot. Reach will connect to your network and get access to the Internet.

Check the [tutorial](../../quickstart/connecting-to-the-internet/) for more information about how to connect Reach to other networks.

##Configure Reach for RTK mode with NTRIP

Open the ReachView 3 app and go to the *GNSS settings* tab. Set everything to the same options as on the screenshot below.

!!! note ""
	In the *GNSS select* section pick either Galileo or Beidou depending on your location. While Glonass covers most of the world, Beidou might be more efficient in the Asia-Pacific region. In this example we use Glonass.

Apply changes.

<div style="text-align: center;"><img src="../img/quickstart/ntrip-workflow/rtk-settings.png" style="height: 550px;"></div>

Now go to the *Correction input* tab, select *NTRIP* and fill in the information from your provider. Choose the nearest reference station to receive the corrections from.

!!! tip ""
	Check the website of your NTRIP provider to find out which mount point suits you better. 

<div style="text-align: center;"><img src="../img/quickstart/ntrip-workflow/ntrip-correction-input.png" style="height: 550px;"></div>

!!! note ""
	If you are using VRS service, you need to enable *Send receiver's position to the provider*. 

Press *Apply*.

##Provide Reach with a clear sky view

Reach RS needs to have a clear view of the sky approximately 30 degrees above the horizon. There should be no obstacles that could block the view like buildings, trees, cars, humans, laptops etc.

<div style="text-align: center;"><img src="../img/quickstart/ntrip-workflow/skyview-obstacles.png" style="width: 800px;"></div>

Learn more about Reach setup in the [Placement](https://docs.emlid.com/reachrs/placement/) section of Reach RS+ docs

##Collect and export data

Check tutorials on how to create new projects, collect points, and export projects:

* [New project](https://www.youtube.com/watch?v=tfSb_1yrYgY&t=6s)
* [Point collection](https://www.youtube.com/watch?v=4tm3bJcf_wk&list=UULPIvk_Oj2Cs0m_APA4FUyQ&index=5)
* [Project export](https://www.youtube.com/watch?v=-X31SxMTd-o&list=UULPIvk_Oj2Cs0m_APA4FUyQ&index=1)

