## Mechanical specs

| File name | Download link |
|-----------|---------------|
| Reach M2 3D model in STEP format | [reachm2 [STEP, 2.1 MB]](https://github.com/emlid/hardware/blob/master/reach-mplus.step)|
| Reach M2 3D model in IGES format | [reachm2 [IGES, 3.6 MB]](https://github.com/emlid/hardware/blob/master/reach-mplus.iges)|
| Reach M2 LoRa radio 3D model in STEP format | [LoRa-radio [STEP, 344 KB]](https://github.com/emlid/hardware/blob/master/LoRa-radio.step) |
| Reach M2 LoRa radio 3D model in IGES format | [LoRa-radio [IGES, 661 KB]](https://github.com/emlid/hardware/blob/master/LoRa-radio.iges) |
| Reach M2 GNSS antenna 3D model in STEP format | [GNSS antenna [STEP, 2.8 MB]](https://github.com/emlid/hardware/blob/master/reachm2-gnss-antenna.STEP) |

### Dimensions

<div style="text-align: center;"><img src="../img/reachm2/specs/dimensions.png" style="width: 650px;"></div><br>
<div style="text-align: center;"><img src="../img/reachm2/specs/height.png" style="width: 650px;"></div><br>

Reach M2 module weights 30g.

### Connectors mating parts

Reach has 4 JST-GH connectors and comes with all required cables to connect to other devices.

Antenna connector is MCX, to connect to SMA or TNC antenna cable you can use one of the numerous adapters. ([cable](http://www.digikey.com/product-detail/en/CAB.0130/931-1102-ND/2332729), [adapter](http://www.digikey.com/product-detail/en/242127/ACX1348-ND/1012025))

<div style="text-align: center;"><img src="../img/reachm2/specs/sma-mcx-cable.jpg" style="width: 150px;"><img src="../img/reachm2/specs/sma-mcx-adapter.jpg" style="width: 150px;"></div><br>


## Electrical specs

### Maximum ratings

|Name                                       | Value                |
|-------------------------------------------|----------------------|
| Input voltage on USB and JST-GH connectors  | 5 - 5.5 V         |
| Logic levels on all pins                  | 3.3 V                |
| Max input voltage on all pins             | 3.3 V                |
| Antenna DC bias                           | 3.3 V                |
| Antenna output current                    | 100 mA               |
| Max current consumption @5V               | 3 A               |
| Normal current consumption @5V            | 600 mA               |
| Current limit on USB OTG                  | 1000 mA              |
| Temperature range                         | -20…+65ºC	(-5…+150ºF)|

### Antenna Phase Centers

[Reach M2 GNSS antenna](https://store.emlid.com/product/multi-band-gnss-antenna/ "Emlid Store | Multi-band GNSS antenna") phase centers' offsets for L1 and L2 are 0.035 m and 0.037 m respectively.


### Connectors pinout
<div style="text-align: center;"><img src="../img/reachm2/specs/reachm2-connectors.png" style="width: 700px;"></div><br>


### USB OTG

Reach can both receive power from USB, acting as a device and source power to the port acting as a host. To use Reach in OTG mode you will need to connect 5V power source to JST-GH connector pins (5 V, GND) and use OTG USB cable.

## Compliance

CE Compliance documents can be found here:

[Reach M2 CE Declaration of conformity](http://files.emlid.com/compliance/CE-Declaration-of-Conformity-Reach-M2.pdf)
