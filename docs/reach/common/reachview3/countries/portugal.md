# Portugal

## Rover Setup

### Coordinate System

Choose a coordinate system based on `ETRS89` (such as `ETRS89 / Portugal TM06`) or `PTRA08` (such as `PTRA08 / UTM zone 25N`) datums.

### Vertical Datum

Choose the `Portugal GEODPT08 height` vertical datum.

The `GEODPT08` geoid is used to perform the transformation.

## Base Setup

Your base or NTRIP service should be in `ETRS89` or `PTRA08`, depending on which datum is used.

!!! note ""
	The `ETRS89` datum is used on the mainland, and `PTRA08` on the Azores islands.

When setting up a base station on a benchmark, enter `ETRS89` or `PTRA08` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
