## Overview

QGIS (previously known as Quantum GIS) is the cross-platform free and open-source desktop geographic information system (GIS) app that provides data viewing, editing and analysis. It can be used for almost any GIS application. 

<div style="text-align: center;"><img src="../img/reach/qgis-survey/reachrs-qgis.jpg" style="width: 350px;"></div><br>

## Connecting QGIS to Reach

First of all, we need to connect survey equipment to QGIS. There are two simple ways. One, over local network, or second by USB. 

!!! tip ""
    To configure the connection in QGIS, you might need to enable the *GPS Information* panel first. Go to the *View* list in the Menu bar and tick this option in the *Panels* field to accomplish this.

### TCP

In order to connect over local network, the computer running QGIS needs to be on the same network as the rover. This can be via the rover's hotspot. This screenshot shows the rover configuration and QGIS configuration. The port number is the same as we will enter in QGIS to find the position string.


<div style="text-align: center;"><img src="../img/reach/qgis-survey/reach-rs-tcp-set.png" style="height: 550px;"></div><br>


In QGIS, the color panel turns green to indicate connection when we enter in the IP address of the rover and the port number.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/qgis-tcp-set.png" style="width: 350px;"></div><br>


### USB

The second way to connect is via "serial device", actually USB. First plug the micro USB into the opening on the rover.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/reachrs-usb.jpg" style="width: 550px;"></div><br>

Then, plug the other end into the computer usb port.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/reachrs-usb-tablet.jpg" style="width: 350px;"></div><br>

For this, the settings on your rover should be as on the screenshot below.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/reachview-qgis-usb.png" style="height: 550px;"></div><br>

In QGIS, choose to connect by serial device and use the same COM port as is shown in connected devices.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/qgis-usb.png" style="width: 350px;"></div><br>

Now that we are connected, we should see Reach position in QGIS.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/reachview-qgis-connected.png" style="width: 850px;"></div><br>

## QGIS basics

In QGIS, we can choose from a wide range of the background maps, including your own drone imagery.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/qgis-view.png" style="width: 550px;"></div><br>

The *GPS* panel shows status, but if you want to check for the solution status, it is better to keep an eye on the Reachview 3 app for that. Once we are connected and have our layers and snapping settings ready, we can add points, lines, and polygons, based on our location.


<div style="text-align: center;"><img src="../img/reach/qgis-survey/qgis-emlid2.png" style="width: 350px;"></div><br>

### QGIS CAD tools

Let's see at the feature of manually entering lines. Often we need to enter a line and then enter distances and directions based on that line, e.g., 30 m at 90 degrees relative to a given line. QGIS has a feature called CAD tools that should work for this. First, enter the line (for example, property line). Then, draw parallel or perpendicular lines from that one. This is found in the advanced digitizing panel. Here you can select start point by vertex and then begin drawing from that point at a direction relative to a selected line.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/qgis-cad.png" style="width: 350px;"></div><br>

Distances and angles can be preset.
Back in the office after the survey, there are options to trim, extend, fillet linework, convert points to arcs, etc. These features could be used while surveying as well. Check out the plug-in QAD.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/qgis-qad-tools.png" style="width: 650px;"></div><br>

Also check out plug-in CadTools.

<div style="text-align: center;"><img src="../img/reach/qgis-survey/qgis-cad-tools.png" style="width: 650px;"></div><br>

!!! tip ""
    Check out the [tutorial](https://www.youtube.com/watch?v=QsjmLa16obs1) for QGIS CAD tool by Klas Karlsson.


## Credits

We want to thank [Brent Wiebe](https://community.emlid.com/users/brent_w/activity) for sharing his experience of using QGIS as survey tool with Reach. 


