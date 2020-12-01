# Latvia

## Rover Setup

### Coordinate System

Choose a coordinate system based on the `LKS92` datum (such as `LKS92 / Latvia TM`).

### Vertical Datum

Choose the `Latvia 2000 height` vertical datum.

The `LV_14` geoid is used to perform the transformation.

!!! note ""
	Consider the `Latvia 2000 height` vertical datum as `LAS-2000,5 height` in this case.

## Base Setup

Your base or NTRIP service should be in `LKS92`.

!!! note ""
	The `LKS92` datum is a national realization of `ETRS89`.

When setting up a base station on a benchmark, enter `LKS92` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
