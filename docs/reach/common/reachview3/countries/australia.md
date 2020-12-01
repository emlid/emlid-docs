# Australia

## Rover Setup

### Coordinate System

Choose a coordinate system based on `GDA2020` (such as `GDA2020 / MGA zone 46`) or `GDA94` (such as `GDA94 / MGA zone 46`) datums.

### Vertical Datum

Choose one of the available vertical datums:

* `AHD (Tasmania) height`
* `AHD height`

The following geoids are used to perform the transformation:

* `AUSGeoid09`
* `AUSGeoid2020`

!!! note ""
	When using  the `AHD height` vertical datum, a correct geoid file will be selected automatically based on the chosen horizontal system:
	
	* Projects based on the `GDA2020` datum use the `AUSGeoid2020` geoid
	* Projects based on the `GDA94` datum use the `AUSGeoid09` geoid
	
	For the `AHD (Tasmania) height` vertical datum only `AUSGeoid09` is available, so use it for projects based on `GDA94` strictly.

## Base Setup

Your base or NTRIP service should be in `GDA2020` or `GDA94`, depending on which datum is used.

!!! note ""
	When working with `Smartnet` or `AusCORS` NTRIP services, make sure to select a correct mount point. Some of them transmit position in `GDA94` while others in `GDA2020`.

When setting up a base station on a benchmark, enter `GDA2020` or `GDA94` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
