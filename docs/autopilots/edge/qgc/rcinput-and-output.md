## RC Input

RC Input is a key part of any autopilot that gives the pilot control of the airframe allows them to change modes and also gives them control of auxiliary equipment.

Edge supports both S.Bus and PPM input, which combines information about all PWM channels from the receiver in one sequence, which could be transferred over single wire. Channel values sent by remote controller will be decoded and then used for servo control.

You need to calibrate [radio](../qgc/calibration/#radio-calibration) before using it.

By default the RC input channels are:

- Channel 1: Roll input
- Channel 2: Pitch input
- Channel 3: Throttle input
- Channel 4: Yaw input
- Channel 5: Flight mode
- Channel 6: (Optional) Tuning

These can be changed by setting the RCMAP_ROLL, RCMAP_PITCH, RCMAP_THROTTLE and RCMAP_YAW parameters. After changing any of these parameters the flight controller should be rebooted.

To set modes of channels 7..12 select `Vehicle Setup` and then `Flight Modes` tab.

<div style="text-align: center;"><img src="../../img/qgc/channel_options.png"></div><br>

## RC Output

RC Output is how ArduPilot controls servos and motors.

Edge has 12 available output channels.

To change channel configuration you can use SERVOx_ parameters. The “x” in this case is the channel number.

!!! danger " "
    We do ask to NOT SET AUXILIARY FUNCTION SWITCHES TO RC7,8 USING HEX FRAME!

You can use `Motors Test` to check motor connection. In `Vehicle Setup` menu choose `Motors`.

<div style="text-align: center;"><img src="../../img/qgc/motors_test.png"></div><br>

!!! danger "Attention"
    Make sure the propellers are removed before using this. It can be dangerous.

## Relay Switch

A “Relay” is a digital output pin that can be either 0V or 3.3V. Similar to a servo it allows the flight controller to invoke some action from another device on the vehicle. You can use it to control things like camera shutter, bottle drop etc.

!!! note
    This feature available only on ArduCopter.

First you need to specify RELAY_PIN parameter in QGC `Parameters`:

<div style="text-align: center;"><img src="../../img/qgc/relay_pin.png"></div><br>

!!! danger "Attention"
    Don't set digital pin to PWM channel used for control servos!

Next, configure pilot control of the relay. Choose previously selected Relay for one of the free channels in `Flight Modes`:

<div style="text-align: center;"><img src="../../img/qgc/rc_relay_control.png"></div><br>

After that you can switch state of Relay Pin using your RC transmitter.
