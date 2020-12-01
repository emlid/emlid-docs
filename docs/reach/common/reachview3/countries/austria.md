# Austria

## Rover Setup

### Coordinate System

Choose a coordinate system based on `MGI (Ferro)` (such as `MGI (Ferro) / Austria East Zone`) or `MGI` (such as `MGI / Austria East`) datums.

### Vertical Datum

Choose one of the available vertical datums:

* `EVRF2000 Austria height`
* `GHA height`

The following geoids are used to perform the transformation:

* `GEOID_GRS80_Oesterreich`
* `GV_Hoehengrid_plus_Geoid_V`

!!! note ""
	The `EVRF2000 Austria height` vertical datum uses the`GEOID_GRS80_Oesterreich` geoid. The `GHA height` vertical datum uses the `GV_Hoehengrid_plus_Geoid_V2` geoid.

## Base Setup

Your base or NTRIP service should be in `ETRS89`. The `AT_GIS_GRID` grid is used to perform the datum conversion.

!!! note ""
	You can't use this datum conversion from `ETRS89` to `MGI` or `MGI (Ferro)` for cadastral purposes. It does not comply with the rules for control network tie-in as per [Paragraph 3 of the Land Survey Regulations (Vermessungsverordnung) 2010](https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20006756&FassungVom=2016-11-30).

When setting up a base station on a benchmark, enter `ETRS89` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
