# Hungary

!!! note "Important"
	Transformations are performed using open source grids from a BME (Budapest Technical University) project. These grids are not official VITEL grids and are not suitable for official land surveying work.

## Rover Setup

### Coordinate System

Choose a coordinate system based on the `HD72` datum (such as `HD72 / EOV`).

### Vertical Datum

Choose the `Hungary EHT2014 height` vertical datum.

The `EHT2014` geoid is used to perform the transformation.

## Base Setup

Your base or NTRIP service should be in `ETRS89`. The `ETRS2EOV` grid is used to perform the datum conversion.

When setting up a base station on a benchmark, enter `ETRS89` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
