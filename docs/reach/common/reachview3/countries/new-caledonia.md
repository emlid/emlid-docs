# New Caledonia

## Rover Setup

### Coordinate System

Choose a coordinate system based on a datum from the list:

* `IGN53 Mare` datum (such as `IGN53 Mare / UTM zone 58S`)
* `IGN56 Lifou` datum (such as `IGN56 Lifou / UTM zone 58S`)
* `IGN72 Grande Terre` datum (such as `IGN72 Grande Terre / UTM zone 58S`)
* `NEA74 Noumea` datum (such as `NEA74 Noumea / UTM zone 58S`)
* `ST84 Ile des Pins` datum (such as `ST84 Ile des Pins / UTM zone 58S`)
* `ST87 Ouvea` datum (such as `ST87 Ouvea / UTM zone 58S`)

### Vertical Datum

Choose the `NGNC08 height` vertical datum.

The `Ranc08_Circe` geoid is used to perform the transformation.

## Base Setup

Your base or NTRIP service should be in `RGNC91-93`. The following methods are used to perform the datum conversion: `Helmert (7-parameters)`, `RGNC1991_IGN72GrandeTerre` grid, `RGNC1991_NEA74Noumea` grid.

When setting up a base station on a benchmark, enter `RGNC91-93` geographic coordinates (lat/long) and ellipsoidal height in the ReachView 3 *Settings / Base mode*.
