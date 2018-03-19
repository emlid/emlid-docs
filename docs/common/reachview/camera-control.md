Reach is able to trigger cameras as well as register events. Event mark feature is a must for aerial mapping as it allows to register precise time when shutter was activated.

<p style="text-align:center" ><img src="../img/reachview/camera_control/camera.png" style="width: 800px;" /></p>

### Camera trigger
Camera trigger is only available on Reach module and not available on Reach RS. By altering the duty cycle and period parameters you can match settings required for triggering your camera module. Real-time signal graph is shown on the same page. Note, that this feature does not have to be used if your autopilot is able to trigger the camera, as it has more information about the flight plan and can make more informed decisions on when to fire the camera. 

### Camera events
You see the time of the last event for real-time debugging. Only works with GNSS satellites in view for time synchronization. Event is triggered by driving time mark pin down, usually by a camera hot shoe. All event marks are stored in the raw data log. Time mark pin is designed to be directly connected to a hotshoe cable without any additional electronic parts such as resistors or capacitors. 

Check the [RTK Settings](/common/reachview/rtk-settings/#gnss-selection-for-time-marks-logging) section of ReachView docs for the recommended GNSS selection when recording time marks with Reach.

