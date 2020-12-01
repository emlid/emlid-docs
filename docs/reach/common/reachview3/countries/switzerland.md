# Switzerland

## Rover Setup

### Coordinate System

Choose a coordinate system based on `CH1903` (such as `CH1903 / LV03`) or `CH1903+` (such as `CH1903+ / LV95`) datums.

### Vertical Datum

!!! note ""
	At the moment, ReachView 3 doesn't support vertical datums for this country.

## Base Setup

Your base or NTRIP service should be in `ETRS89`. The following methods are used to perform the datum conversion: `CHENyx06` grid, `Helmert (7-parameters)`.

When setting up a base station on a benchmark, enter `ETRS89` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
