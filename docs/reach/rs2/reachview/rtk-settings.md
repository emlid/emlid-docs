# RTK settings

## RTK options

<p style="text-align:center" ><img src="../img/reachview/rtk-settings/rtk-settings-rs2.png" style="width: 800px;" /></p>

### Positioning mode

+ **Kinematic** - most used positioning mode, assumes that the receiver is moving
+ **Static** - an assumption is made that Reach is static. Constraining the system helps to resolve ambiguities faster as well as produce measurements with higher precision

### Elevation mask angle
Satellites lower than set elevation will be excluded from the computation. The default setting is 15 degrees. Usually, satellites with a lower elevation provide too noisy measurements.

### SNR mask
Satellites with low SNR will be excluded from the computation. The default setting is 35.

## GNSS selection

Reach RS2 tracks GPS, GLONASS, GALILEO, QZSS, and BEIDOU satellite systems. The data can be logged with 1 Hz, 5 Hz or 10 Hz update rate.

All GNSS enabled at 5 Hz is our default recommendation.
