# Slovakia

## Rover Setup

### Coordinate System

Choose a coordinate system based on `S-JTSK` (such as `S-JTSK / Krovak`) or `S-JTSK [JTSK03]` (such as `S-JTSK [JTSK03] / Krovak`) datums.

### Vertical Datum

Choose one of the available vertical datums:

* `Baltic 1957 depth`
* `Baltic 1957 height`
* `EVRF2007 height`

The following geoids are used to perform the transformation:

* `Slovakia_ETRS89h_to_Baltic1957`
* `Slovakia_ETRS89h_to_EVRF2007`

## Base Setup

Your base or NTRIP service should be in `ETRS89`. The following methods are used to perform the datum conversion: `Helmert (7-parameters)`, `Slovakia_JTSK03_to_JTSK` grid.

!!! note ""
	The datum conversion from `ETRS89` to `S-JTSK` uses `Helmert (7-parameters)` transformation method and the datum conversion from `ETRS89` to `S-JTSK [JTSK03]` uses both `Helmert (7-parameters)` and `Slovakia_JTSK03_to_JTSK` grid.

When setting up a base station on a benchmark, enter `ETRS89` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
