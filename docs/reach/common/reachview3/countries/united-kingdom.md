# United Kingdom

## Rover Setup

### Coordinate System

Choose a coordinate system based on the `OSGB 1936` datum (such as `OSGB 1936 / British National Grid`).

### Vertical Datum

Choose one of the available vertical datums:

* `Belfast height`
* `Douglas height`
* `ODN (Offshore) height`
* `ODN Orkney height`
* `ODN height`
* `St. Marys height`
* `Stornoway height`

The following geoids are used to perform the transformation:

* `OSGM15_Belfast`
* `OSGM15_GB`

!!! note ""
	The `Belfast height` vertical datum uses the `OSGM15_Belfast` geoid. All the other vertical datums use the `OSGM15_GB` geoid.

## Base Setup

Your base or NTRIP service should be in `ETRS89`. The `OSTN15` grid is used to perform the datum conversion.

When setting up a base station on a benchmark, enter `ETRS89` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
