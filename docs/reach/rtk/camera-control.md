Reach is able to trigger cameras as well as register events. Event mark feature is a must for aerial mapping as it allows to register precise time when shutter was activated.

<p style="text-align:center" ><img src="../img/reach/camera-control/camera-control-settings.png" style="width: 800px;" /></p>

### Camera trigger
By altering the duty cycle and period parameters you can match settings required for triggering your camera module. Real-time signal graph is shown on the same page. Note, that this feature does not have to be used if your autopilot is able to trigger the camera, as it has more information about the flight plan and can make more informed decisions on when to fire the camera. 

### Camera events
You see the time of the last event for real-time debugging. Only works with GNSS satellites in view for time synchronization. An event is triggered by driving time mark pin down, usually by a camera hot shoe. It is possible to connect Reach Module with an adapter to any camera with hot shoe (e.g. Sony, Canon, Nikon). All event marks are stored in the raw data log. Time mark pin is designed to be directly connected to a hot shoe cable without any additional electronic parts such as resistors or capacitors.

#### Connecting Reach Module to a camera using HSA

To connect Reach Module to a camera with hot shoe adapter (HSA) use 5-pin JST-GH cable. Attach JST-GH connector to the port with the Time Mark pin. Make sure you connect the adapter to a hot shoe of a camera correctly:

<p style="text-align:center" ><img src="../img/reach/camera-control/emlid-hotshoe.jpg" style="width: 500px;" /></p>

!!! danger "Attention"
    Check the [RTK Settings](../../reachview/rtk-settings/#gnss-selection-for-time-marks-logging) section of Reach Panel docs for the recommended GNSS selection when recording time marks with Reach.