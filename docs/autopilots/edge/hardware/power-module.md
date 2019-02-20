## Edge power module

### Specifications

| | |
|:-|:-|
|Working voltage|2-12S|
|Maximum load| 60A (200A[*](power-module/#modifications-for-high-current-setups))|


### Connection

Use a JST-GH-6P to JST-GH-6P cable to connect your Edge power module.

<div style="text-align: center;"><img src="../../img/hardware/edge_power_module.png" style="width: 500px;"></div><br>

* Plug one end of the cable in either PWR1 or PWM2 port on the Edge drone controller
* Plug another end of the very same cable in the port of the Edge power module

### Modifications for high current setups

By default the maximum current that can be drawn is 60A. But the module sensor itself allows to measure and draw current up to 200A.

!!! tip " "
    In order to achieve this, you need to replace the wires and the connectors that can endure continuous load of 200A
