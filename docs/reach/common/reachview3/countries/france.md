# France

## Rover Setup

### Coordinate System

Choose a coordinate system based on the `RGF93` datum (such as `RGF93 / CC42`).

### Vertical Datum

Choose one of the available vertical datums:

* `NGF-IGN69 height`
* `NGF-IGN69(RAF09) height`

The following geoids are used to perform the transformation:

* `RAF09`
* `RAF18`

!!! note ""
	The `NGF-IGN69 height` vertical datum uses the `RAF18` geoid. The `NGF-IGN69(RAF09) height` vertical datum uses the `RAF09` geoid.

## Base Setup

Your base or NTRIP service should be in `RGF93`.

When setting up a base station on a benchmark, enter `RGF93` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
