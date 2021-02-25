# Hungary

## Rover Setup

### Coordinate System

Choose a coordinate system based on the `HD72` datum (such as `HD72 / EOV`).

### Vertical Datum

Choose one of the available vertical datums:

* `Hungary EHT2014 height`
* `Hungary VITEL2014 height`

The following geoids are used to perform the transformation:

* `EHT2014`
* `VITEL2014`

## Base Setup

Your base or NTRIP service should be in `ETRS89`. The `ETRS2EOV` grid is used to perform the datum conversion.

When setting up a base station on a benchmark, enter `ETRS89` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
