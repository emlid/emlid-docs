## Overview

QGIS (previously known as Quantum GIS) is the cross-platform free and open-source desktop geographic information system (GIS) app that provides data viewing, editing and analysis. It can be used for almost any GIS application. 

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/reachrs-qgis.jpg" style="width: 350px;"></div><br>

## Connecting QGIS to Reach RS

First of all, we need to connect survey equipment to QGIS. There are two simple ways. One, over local network, or second by USB. 

### TCP

In order to connect over local network, the computer running QGIS needs to be on the same network as the rover. This can be via the rover's hotspot. This screenshot shows the reach Rover config and the QGIS config. The port number is the same as we'll enter in QGIS to find position string.


<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/reach-rs-tcp-set.png" style="width: 550px;"></div><br>


In QGIS, the color panel turns green to indicate connection when we enter in the IP address of the rover and the port number.


<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/qgis-tcp-set.png" style="width: 350px;"></div><br>


### USB

The second way to connect is via "serial device", actually USB. First plug the micro USB into the opening on Rover.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/reachrs-usb.jpg" style="width: 550px;"></div><br>

Then, plug the other end into the computer usb port.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/reachrs-usb-tablet.jpg" style="width: 350px;"></div><br>

For this, the settings on your rover should be as on the screenshot below.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/reachview-qgis-usb.jpg" style="width: 350px;"></div><br>

In QGIS, choose to connect by serial device and use the same COM port as is shown in connected devices.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/qgis-usb.png" style="width: 350px;"></div><br>

Now that we're connected we should see our position in QGIS similar to on our Reachview app.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/reachview-qgis-connected.png" style="width: 750px;"></div><br>
<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/reachview-qgis-connected1.png" style="width: 750px;"></div><br>

## QGIS basics

In QGIS, we can choose from a wide range of background maps, including your own drone imagery.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/qgis-view.png" style="width: 550px;"></div><br>

The GPS panel shows status but if you want to check for the solution status it is better to keep an eye on Reachview app for that. Once we're connected and have our layers and snapping settings ready we can go to work! Adding points, lines, and polygons, based on our location.


<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/qgis-emlid2.png" style="width: 350px;"></div><br>

### QGIS CAD tools

Let's see at the feature of manually entering lines. Often we need to enter a line and then enter distances and directions based on that line, e.g. 30 m at 90 degrees relative to a given line. QGIS has a feature called CAD tools that should work for this. First, enter the line (for example, property line). Then, draw parallel or perpendicular lines from that one. This is found in the advanced digitizing panel. Here you can select start point by vertex and then begin drawing from that point at a direction relative to a selected line.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/qgis-cad.png" style="width: 350px;"></div><br>

Distances and angles can be preset.
Back in the office after the survey, there are options to trim, extend, fillet linework, convert points to arcs, etc. These features could be used while surveying as well. Check out the plug-in QAD.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/qgis-qad-tools.png" style="width: 650px;"></div><br>

Also check out plugin CadTools.

<div style="text-align: center;"><img src="../img/reachrs/qgis-survey/qgis-cad-tools.png" style="width: 650px;"></div><br>

!!! tip
    [Check out](https://www.youtube.com/watch?v=QsjmLa16obs1) the tutorial for QGIS CAD tool by Klas Karlsson.


## Credits

We want to thank [Brent Wiebe](https://community.emlid.com/users/brent_w/activity) for sharing his experience of using QGIS as survey tool with Reach RS. 


