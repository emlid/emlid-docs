Copter includes a suite of Pre-arm Safety Checks which will prevent the vehicle from arming if any issues are discovered
before take-off. These checks help to prevent crashes and fly-aways and can also be enabled and disabled individually.
Arming checks are performed each time there is an attempt to arm the vehicle.

You will notice a pre-arm check failure because the LED will be flashing yellow.
To determine exactly which check has failed:

1. Connect your Edge to the ground station.
2. Ensure the GCS is connected to the vehicle.
3. Turn on your radio transmitter and attempt to arm the vehicle (regular procedure using throttle down, yaw right)
4. The first cause of the Pre-Arm Check failure will be displayed in red on the HUD window


### This is a list of arming checks that may be enabled.


### All

All of the arming checks are performed.


### Barometer

Fails if any of the Barometers detected at boot are unhealthy which is normally a sign of a hardware failure.


### Compass

Fails if the on board compass is enabled and any of the following are true:

* The compass is unhealthy
* The compass offsets have not been set and learning offsets is disabled
* The compass is currently calibrating
* The compass calibration requires a reboot
* The compass offsets are too large
* The current magnetic field vector length is too large
* Individual compasses have inconsistent measurements


### GPS lock

Fails if the home position is unset and the GPS is not reporting a 3D fix.


### INS (i.e. Acclerometer and Gyro checks)

Fails if

* Any of the gyros are unhealthy
* Any of the gyros have a poor calibration
* Any of the accelerometers are unhealthy
* Any of the accelerometers have a poor calibration
* The accelerometer calibration requires a reboot
* Individual accelerometers have inconsistent measurements
* Individual gyros have inconsistent measurements
* The AHRS is unhealthy

### RC

Fails if the configured RC input ranges are invalid.


### Board voltage

Fails if the board voltage is below 4.3V or above 5.8V. This is a serious problem and the power system 
(i.e. Power Module, battery, etc) should be carefully checked before flying.

### Battery Level

Fails if the battery failsafe is active, of if a battery voltage is below the threshold configured by the
ARMING_MIN_VOLT or ARMING_MIN_VOLT2 parameters.


### Logging Available

Fails if there is no sd card inserted or if writing a log failed.


### Hardware safety switch

Fails if the hardware safety switch is enabled and the hardware safety switch is not in the armed state. The hardware
switch is optional, it can be cumbersome to access the electronics in order to arm the autopilot at the hardware level.


### GPS Configuration

Fails if any of the following is true:

* Any gps requires further configuration.
* Individual gps inputs are giving inconsistent readings.
* Blending of multiple gps inputs is unhealthy.
