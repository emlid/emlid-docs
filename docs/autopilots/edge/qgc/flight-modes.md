This article provides an overview of the available flight modes.

### Recommended Flight Modes 

* Stabilize
* Alt Hold
* Loiter
* RTL (Return-to-Launch)
* Auto

### Stabilize

In this mode your inputs are directly passed to the motors with stabilization.
You're controlling your vehicle manually except the self-leveling the roll and pitch axis.

!!! tip
    Try Alt Hold or Loiter mode instead of Stabilize and you'll be concentrated on less
    controls at once. This will be a good starting point if you're learning to fly.


### Alt hold

When altitude mode is activated, Copter keeps consistent altitude allowing you
to handle roll, pitch, and yaw. The throttle is automatically controlled to
maintain the current altitude.

### Loiter

Loiter Mode maintains the current location, heading and altitude automatically.
The difference between this and manual mode is that when pilot releases the sticks,
the vehicle returns to a stop and hold position.

### RTL (Return-to-Launch)

RTL mode navigates Copter from its current position to hover above the home position.
The copter will first take the minimum relative altitude (RTL_ALT) before returning
home. To learn more about RTL Mode behaviour and its parameters please navigate to
[this page](http://ardupilot.org/copter/docs/rtl-mode.html).

### Auto

In Auto mode the copter will accomplish a mission script which combines the "Navigation"
commands and “Do” commands. "Navigation" commands affect vehicle's location and "Do"
commands tackle auxiliary functions.

<hr>

!!! tip
    If you want to learn more about the available flight modes, please, refer to the ArduPilot docs available [here](http://ardupilot.org/copter/docs/flight-modes.html).

