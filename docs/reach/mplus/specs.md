## Mechanical specs

### Dimensions



<div style="text-align: center;"><img src="../img/reachm-plus/specs/dimensions.png" style="width: 650px;"></div><br>
<div style="text-align: center;"><img src="../img/reachm-plus/specs/height.png" style="width: 650px;"></div><br>

Reach M+ module weights 20g.

### Connectors mating parts

Reach has 4 JST-GH connectors and comes with all required cables to connect to other devices.

Antenna connector is MCX, to connect to SMA or TNC antenna cable you can use one of the numerous adapters. ([cable](http://www.digikey.com/product-detail/en/CAB.0130/931-1102-ND/2332729), [adapter](http://www.digikey.com/product-detail/en/242127/ACX1348-ND/1012025))

<div style="text-align: center;"><img src="../img/reachm-plus/specs/sma-mcx-cable.jpg" style="width: 150px;"><img src="../img/reachm-plus/specs/sma-mcx-adapter.jpg" style="width: 150px;"></div><br>

### 3D model

Reach M+ 3D model can be downloaded here:

* [Reach M+ Step file](https://github.com/emlid/hardware/blob/master/ReachM%2B.step)


## Electrical specs

### Maximum ratings

|Name                                       | Value                |
|-------------------------------------------|----------------------|
| Input voltage on USB and JST-GH connectors  | 4.75 - 5.5 V         |
| Logic levels on all pins                  | 3.3 V                |
| Max input voltage on all pins             | 3.3 V                |
| Antenna DC bias                           | 3.3 V                |
| Antenna output current                    | 100 mA               |
| Max current consumption @5V               | 500 mA               |
| Normal current consumption @5V            | 200 mA               |
| Current limit on USB OTG                  | 1000 mA              |
| Temperature range                         | -20…+70ºC		   |


### Connectors pinout
<div style="text-align: center;"><img src="../img/reachm-plus/specs/reachm-connectors.png" style="width: 700px;"></div><br>


### USB OTG

Reach can both receive power from USB, acting as a device and source power to the port acting as a host. To use Reach in OTG mode you will need to connect 5V power source to JST-GH connector pins (5 V, GND) and use OTG USB cable.

## Compliance

CE Compliance documents can be found here:

* [Reach M+ CE Declaration of conformity](https://files.emlid.com/compliance/RM_CE_declaration.pdf)
