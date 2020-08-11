!!! tip ""
    This is the second part of a guide describing the PPK mapping workflow with Reach. It implies you already have raw logs from both base and rover, set of images, and Ground Control Points. If you don't, [please check the previous part first](geosetter-tutorial.md).

At previous steps, we got centimeter-accurate geotags from Reach and georeferenced a set of images using this data. Now, we'll turn it into a map.

## Creating the map in Pix4Dmapper

Pix4Dmapper is a photogrammetry software for drone mapping by [Pix4D.](https://www.pix4d.com/) It provides tools for creating digital maps and models and taking measurements based on them.

### Creating a new project

To create a new project in Pix4Dmapper:

* Start Pix4Dmapper
* Click *Project* > *New project*... The *New Project* window opens
* In the *New Project* window, enter a name and browse for a directory

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-1.png" style="width: 800px;"></div>

* Click *Next*. The *Select Images* window opens

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-2.png" style="width: 800px;"></div>

* Click *Add images*. Browse to the image folder and select the images. They will display in the window. Click *Next*

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-3.PNG" style="width: 800px;"></div>

* In *Image Geolocation Editor* - *Coordinate System*, click *Edit*… and select *WGS 84* and *Geoid Height Above WGS 84 Ellipsoid [m] = 0* in *Advanced Coordinate Options*
* In *Image Properties Editor* - *Images Table* adjust the *Accuracy Horz* and *Accuracy Vert* values to reflect the estimated accuracy of image geolocation

!!! tip ""
    The Camera Model is usually defined automatically from images’ metadata. However, it can be changed if necessary.

* Select the Output Coordinate System that will be assigned to the generated results, for example, DSM and orthomosaic. If the images are georeferenced, a corresponding UTM zone will be auto-detected by default

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-4.PNG" style="width: 400px;"></div>

* Choose *Processing Options Template*. The template defines parameters for each processing step and generated outputs

The quality of the reconstruction and the processing time depend on the chosen parameters. If the goal is to generate a DSM and an orthomosaic, the 3D Maps template can be selected.

!!! tip ""
    Digital Surface Model (DSM) is a raster data format with an elevation value for each pixel. Orthomosaic is a 2D map generated based on multiple images using orthorectification.  This method removes the perspective distortions from the images using the DSM.


<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-5.PNG" style="width: 800px;"></div>

### Importing GCPs

!!! tip ""
    Ground control points are optional for PPK mapping. If you don’t have them, please, go to the *Processing* section.

For this step, the file with Ground Control Points (GCPs) is needed.

The file must be in either a .csv or .txt file format and contain a point name, latitude and longitude in degrees, and altitude for each point. Use a comma to separate the values:

<div style="text-align: center;">

GCP0,46.23456,6.56114,299.931
<br>
GCP1,46.23234,6.56234,299.823
<br>
...

</div>

!!! tip ""
    Reach supports points export in .csv format only.

To mark the GCPs on images:

* Click *Project* > *GCP/MTP Manager*.... The GCP/MTP Manager window opens
* Click *Import GCPs*. In the *Coordinates Order* drop-down list, choose an appropriate option, browse to the points file, press OK

!!! tip ""
    For Reach, the default order of coordinates is longitude, latitude, altitude.

* In section *GCP/MTP Editor*, click *Basic Editor*

!!! tip ""
    GCPs can also be marked in the *rayCloud* after *Initial Processing* has been completed. Learn more about this method on [Pix4D documentation](https://support.pix4d.com/hc/en-us/articles/202560769-How-to-mark-GCPs-in-the-rayCloud).

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-6.PNG" style="width: 800px;"></div>

* Choose *Sort Images by Distance to GCP* in *Images* section. The images are displayed in order from the closest to the selected GCP to the farthest
* Find and mark every point on 3 images at least. Marking instruments are in the Preview window

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-7.PNG" style="width: 800px;"></div>

* Once all the points are marked, press OK

### Processing

??? note "There are 3 parts of processing:"
    1. *Initial processing.* Keypoints are identified and matched in neighboring images and used for project reconstruction
    2. *Point Cloud and Mesh.* The dense point cloud and 3D triangulated mesh are computed based on the results of the previous step
    3. *DSM, Orthomosaic, and Index.* The DSM and orthomosaic are generated based on the dense point cloud

To start processing the project:

* Click *Processing* in the bottom left corner of the main window
* Select all three processing steps and click *Start*:

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-8.png" style="width: 800px;"></div>

!!! tip ""
    If necessary, processing steps’ parameters can be changed in *Processing Options* menu. For example, the density of point cloud or DSM/orthomosaic resolution. In this guide, we use the standard settings of the 3D Maps template.

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-9.PNG" style="width: 800px;"></div>

At the end of each step, a Quality report is generated and can be used to verify the success of processing

The processing is finished! Now you can export this orthomosaic to any GIS software to create a vector map based on it.

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-10.png" style="width: 800px;"></div>

### Results

Once the project has been processed, it is possible to analyze and display results directly in Pix4Dmapper or import them in third-party software.

To open the folder with ****results, on the Menu bar, click *Process* > *Open Results Folder*...

* The Orthomosaic and DSM are stored in *the /3_dsm_ortho/2_mosaic/* folder

To visualize the orthomosaic or DSM in Pix4Dmapper, click the *Mosaic Editor* tab:

<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-11.PNG" style="width: 800px;"></div>
<div style="text-align: center;"><img src="../img/reach/pix4d-tutorial/pix4d-12.PNG" style="width: 800px;"></div>

The processing is finished! Now you can export this orthomosaic to any GIS software to create a vector map based on it.

<br>

Further reading:

Learn more about processing projects in Pix4Dmapper on [Pix4D documentation.](https://support.pix4d.com/hc/en-us/articles/205319155-Processing-Options-Default-Templates)