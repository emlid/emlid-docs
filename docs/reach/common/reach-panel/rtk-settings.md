# RTK settings

## RTK options


<p style="text-align:center" ><img src="../img/reachview/rtk_settings/rtk-settings-rs-m-plus.png" style="width: 800px;" /></p>


### Positioning mode

+ **Kinematic** - most used positioning mode, assumes that the receiver is moving
+ **Static** - an assumption is made that Reach RS/RS+ is static. Constraining the system helps to resolve ambiguities faster as well as produce measurements with higher precision

 

### GPS AR mode

There are two main strategies for resolving ambiguities:
 
+ **Fix-and-hold**: after first ambiguity fix hold them constrained. Fix is more stable, but in case first initialization was not correct it will take longer to recover and initialize correctly. You can think of it as if Fix had inertia.
+ **Continuous**: ambiguities are resolved epoch by epoch. Less stable, but no risk of holding a false fix.

In real-life conditions on a moving platform, Fix-and-hold provides better overall performance.

### GLONASS AR mode 
Contrary to GPS, all GLONASS satellites transmit on different frequencies, which results in Inter Channel Biases (ICB) that are unique for each receiver model. 

Reach RS/RS+ can correct GLONASS ICBs, allowing for GLONASS AR with non-Reach bases, such as NTRIP casters. The general recommendation is to always have GLONASS AR set to on.



### Elevation mask angle
Satellites lower than set elevation will be excluded from the computation. The default setting is 15 degrees. Usually, satellites with a lower elevation provide too noisy measurements.

### SNR mask
Satellites with low SNR will be excluded from the computation. The default setting is 35.

## GNSS selection



<p style="text-align:center" ><img src="../img/reachview/rtk_settings/gnss-selection-rs-m-plus.png" style="width: 800px;" /></p>

Depending on your location, it might be beneficial to choose certain set of GNSS systems: 

+ GPS + GLONASS + Galileo + SBAS + QZSS at 5 Hz is our default recommendation
+ GPS + BeiDou + Galileo + SBAS + QZSS at 5 Hz recommended for APAC, where QZSS and BeiDou is visible
+ GPS + Galileo + SBAS + QZSS at 14 Hz for most dynamic platforms that require high update rate



