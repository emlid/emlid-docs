!!! tip ""
    This is the second part of a guide describing the PPK mapping workflow with Reach. It implies you already have raw logs from both base and rover, set of images, and Ground Control Points. If you don't, [please check the previous part first](configuring-reach-for-mapping.md).

In this guide, we are preparing set of images for processing in a photogrammetric software.

## Post-processing

First, we should post-process raw data logs from base and rover in RTKLib. You can use [this guide](gps-post-processing.md) to accomplish it. The result is the *_event.pos file containing the list of accurate positions of each photo.

Convert the \*_event.pos file to \*_event.gpx:

* Open RTKPost and hit on *KML/GPX...* button
* Tap *GPX* option
* In the *Output Altitude* field, choose Ellipsoidal altitude
* In the *Output Time* field, choose UTC or GPST time depending on which is required
* Click on *Input/Output/GE Exe File* and browse for the *_event.pos
* Hit *Convert*

<div style="text-align: center;"><img src="../img/reach/geosetter-tutorial/converting.png" style="width: 400px;"></div>

## Photo geotagging with GeoSetter

Once we have the list of coordinates for each photo, we need to match it with our set of images.

To geotag photos, we use the [GeoSetter](https://www.geosetter.de/en/download-en/). It's a freeware Windows tool allowing to add coordinates to images' metadata.

* Open the *File* menu and choose *Open folder* option to browse for the folder with photos
* Enable the Tracks window by opening the *View* menu and hitting on *Tracks*

<div style="text-align: center;"><img src="../img/reach/geosetter-tutorial/geosetter-1.png" style="width: 800px;"></div>

* In the left top corner of Tracks window, click on the *folder* button and browse for *_events.gpx file that was converted earlier
* In the right top corner of Tracks window, enable the *Show list of track points* button to display the list of all the tracks
* Select the track in the list of coordinates. The track appears as a red marker on the Map

<div style="text-align: center;"><img src="../img/reach/geosetter-tutorial/geosetter-2.png" style="width: 800px;"></div>

* Select all the images. Make sure that in the information bar all images are marked as selected
* Open the *Edit* menu and click on the *Synchronize with GPS Data Files* option. The Synchronize with GPS Data Files window appears
* In the Time Adjustment field, choose *Use Track Point From Map* option and hit on *OK.* The modal window appears

<div style="text-align: center;"><img src="../img/reach/geosetter-tutorial/geosetter-3.png" style="width: 800px;"></div>

* Make sure that the number of images in the modal window is equal to the quantity of all selected images and press *Yes*

<div style="text-align: center;"><img src="../img/reach/geosetter-tutorial/geosetter-4.png" style="width: 300px;"></div>

* Now, time-marks are synchronized with GPS data. As a result, a position marker for each photo is displayed on a map. To save the geolocation into the image EXIF data, open the *Edit* menu and choose *Save changes* option

<div style="text-align: center;"><img src="../img/reach/geosetter-tutorial/geosetter-5.png" style="width: 800px;"></div>

Now you can import this set of images to any mapping software, such as Agisoft Metashape, DroneDeploy, Pix4d, etc. In this guide, we will use the Pix4D software to create a map.

<br>

Further reading:

* [Creating the map in Pix4DMapper](pix4d-tutorial.md) 