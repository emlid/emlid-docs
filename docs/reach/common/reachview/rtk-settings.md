## RTK options

<p style="text-align:center" ><img src="../img/reachview/rtk_settings/rtk_set.png" style="width: 800px;" /></p>

### Positioning mode

+ **Single** - standalone positioning mode, does not provide improved precision
+ **Kinematic** - most used positioning mode, assumes that the receiver is moving
+ **Static** - an assumption is made that Reach is static. Constraining the system helps to resolve ambiguities faster as well as produce measurements with higher precision

### GPS AR mode

There are two main strategies for resolving ambiguities:
 
+ **Fix-and-hold**: after first ambiguity fix hold them constrained. Fix is more stable, but in case first initialization was not correct it will take longer to recover and initialize correctly. You can think of it as if Fix had inertia.
+ **Continuous**: ambiguities are resolved epoch by epoch. Less stable, but no risk of holding a false fix.

In real-life conditions on a moving platform, Fix-and-hold provides better overall performance.

### GLONASS AR mode 
Contrary to GPS, all GLONASS satellites transmit on different frequencies, which results in Inter Channel Biases (ICB) that are unique for each receiver model. 

Reach can correct GLONASS ICBs, allowing for GLONASS AR with non-Reach bases, such as NTRIP casters. The general recommendation is to always have GLONASS AR set to on.

### Elevation mask angle
Satellites lower than set elevation will be excluded from the computation. The default setting is 15 degrees. Usually, satellites with a lower elevation provide too noisy measurements.

### SNR mask
Satellites with low SNR will be excluded from the computation. The default setting is 35.

### Max acceleration
Set it according to what acceleration antenna experiences on your platform. If you are not sure about the correct value collect a dataset and use RTKPLOT to see what kind of accelerations are present in your application. Default value is 1 m/s^2.

## GNSS selection

<p style="text-align:center" ><img src="../img/reachview/rtk_settings/gnss_sel.png" style="width: 800px;" /></p>

Depending on your location it might be beneficial to choose certain set of GNSS systems: 

+ GPS + GLONASS + SBAS + QZSS at 5 Hz is our default recommendation
+ GPS + BEIDOU + SBAS + QZSS at 5 Hz recommended for APAC, where QZSS and BEIDOU is visible
+ GPS + SBAS + QZSS at 14 Hz for most dynamic platforms that require high update rate

### GNSS selection for time marks logging 
We recommend using the following configurations for PPK flights: 

| System                                | Frequency |
|---------------------------------------|-----------|
| GPS + GLONASS + GALILEO + SBAS + QZSS | 1 Hz      |
| GPS + GLONASS + QZSS                  | 5 Hz      |
| GPS + GALILEO                         | 5 Hz      |
| GPS                                   | 10 Hz     |


!!! danger "Attention"
    Use one of the stable configurations above to avoid missing events in log files.


