# Switzerland

## Rover Setup

### Coordinate System

Choose a coordinate system based on `CH1903` (such as `CH1903 / LV03`) or `CH1903+` (such as `CH1903+ / LV95`) datums.

### Vertical Datum

Choose one of the available vertical datums:

* `LHN95 height`
* `LN02 height`

The following geoids are used to perform the transformation:

* `CHGEO04_ETRF`
* `CHGEO04_HT_ETRF`

## Base Setup

Your base or NTRIP service should be in `ETRS89`. The following methods are used to perform the datum conversion: `CHENyx06` grid, `Helmert (7-parameters)`.

When setting up a base station on a benchmark, enter `ETRS89` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
