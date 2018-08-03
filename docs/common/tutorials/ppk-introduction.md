PPK stands for Post-Processed Kinematic.

### Definitions and differences from RTK

Post-Processed Kinematic (PPK) is an alternative technique to Real-Time Kinematic (RTK). With PPK workflow, accurate positioning doesn't happen in real time, all algorithms are applied afterwards. Both base on the ground and rover (usually on a UAV) record raw GNSS logs, which are then processed to receive an accurate positioning track.

<p style="text-align:center" ><img src="../img/reach/ppk-introduction/PPK.png" style="width: 800px;" /></p>

While PPK is mainly used in UAV mapping, it can also be used as a back up for RTK for any surveying job. PPK offers more flexible workflow, allowing to run the processing multiple times using different settings. It also doesn't require a correction link between base and rover, making equipment setup simpler.

### PPK for UAV Mapping

There are several advantages of using PPK for mapping with a drone. PPK doesn’t require placing Ground Control Points (GCPs), which allows to inspect much wider areas. It is especially useful when you need to map large territories or places with difficult terrain. 

!!! note " "
	For the PPK mapping, it is recommended to have few GCPs on site for data check (checkpoints).

The most critical part of PPK for UAV Mapping is synchronisation of a camera and Reach M+, because:

1. There is always a delay between camera trigger and the actual moment the photo is taken.

2. When a drone flies at high speeds, the autopilot receives position readings only each several meters. The accuracy of, say, 2 meters is not enough for surveying. 

Reach (M+) solves this by connecting to a camera shutter via hot shoe. The time of each photo is logged with a resolution of less than a microsecond. During PPK you receive coordinates of exact moments of each photo taken.

There’s no need in integrating Reach to autopilot for UAV mapping.
 
<p style="text-align:center" ><img src="../img/reach/ppk-introduction/emlid-hotshoe.jpg" style="width: 600px;" /></p>

<p style="text-align:center" > <i>Connecting a camera and Reach M+ with a hot shoe adapter </i></p>

As a result of UAV PPK mapping with Reach, you'll have a set of images and a text file containing a list of accurate coordinates corresponding to each photo. This data is then imported in mapping software such as Agisoft PhotoScan, DroneDeploy, Pix4d, etc.

!!! tip "DJI Drones Workaround"
	You can’t easily integrate Reach M+ with DJI Mavic or Phantom, as their cameras don’t have hot shoe. But you can always stick to working with GCPs, which is simple and efficient for small areas – just like your DJI drone.

Further Reading:

* [Camera control](/common/reachview/camera-control.md)
* [Logging](/common/reachview/logging.md)
* [Post-Processing Guide](gps-post-processing.md)