# Slovenia

## Rover Setup

### Coordinate System

Choose a coordinate system based on the `Slovenia 1996` datum (such as `Slovenia 1996 / Slovene National Grid`).

### Vertical Datum

Choose one of the available vertical datums:

* `SVS2000 height`
* `SVS2010 height`

The following geoids are used to perform the transformation:

* `SLOAMG2000`
* `SLOVRP2016`

!!! note ""
	The `SVS2000 height` vertical datum uses the `SLOAMG2000` geoid. The `SVS2010 height` vertical datum uses the `SLOVRP2016` geoid.

## Base Setup

Your base or NTRIP service should be in `Slovenia 1996`.

!!! note ""
	The `Slovenia 1996`  datum is a national realization of `ETRS89`.

When setting up a base station on a benchmark, enter `Slovenia 1996` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
