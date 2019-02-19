!!! tip ""
	Reach has been replaced with [Reach M+](https://emlid.com/reach). Documentation for Reach M+ can be found [here](https://docs.emlid.com/reachm-plus/).

## Mechanical specs

### Dimensions

Reach RTK module is a tiny device, it is only a few millimeters larger than Intel Edison that it houses.

<div style="text-align: center;"><img src="../img/reach/specs/reach-dimensions.png" style="width: 350px;"></div><br>

### Connectors mating parts

Reach has dual DF13 connectors and comes with all required cables to connect to other devices. In case you would like to make you own cable assembly here are the appropriate connector part numbers:

* On Reach: Hirose DF13-6P-1.25H(50) ([Digikey](http://www.digikey.com/product-detail/en/DF13-6P-1.25H%2850%29/H3354-ND/530653), [Mouser](http://eu.mouser.com/ProductDetail/Hirose-Electric/DF13-6P-125H50/?qs=%2fha2pyFaduilOJdMONLaLBwaFNH0V7VnzXasUV9hMRidfNFMCnSnIA%3d%3d)).

* Receptacle: Hirose DF13-6S-1.25C ([Digikey](http://www.digikey.com/product-search/en?keywords=DF13-6S-1.25C), [Mouser](http://eu.mouser.com/ProductDetail/Hirose-Electric/DF13-6S-125C/?qs=%2fha2pyFaduhJ5h7X7LLPzEL0u%2f%252b1ZTztM8mMa9tEuYmcKFXQSgLZyQ%3d%3d))

Antenna connector is MCX, to connect to SMA or TNC antenna cable you can use one of the numerous adapters. ([cable](http://www.digikey.com/product-detail/en/CAB.0130/931-1102-ND/2332729), [adapter](http://www.digikey.com/product-detail/en/242127/ACX1348-ND/1012025))

<div style="text-align: center;"><img src="../img/reach/specs/sma-mcx-cable.jpg" style="width: 150px;"><img src="../img/reach/specs/sma-mcx-adapter.jpg" style="width: 150px;"></div><br>

### 3D model

This 3D model can be used as a reference for case design. Please note that Reach comes in protective heatshrink that increases its outer dimensions slightly.

<script src="https://embed.github.com/view/3d/emlid/hardware/master/Reach.STL"></script>

During case design keep in mind that you should not place anything close to the Wi-Fi antenna or performance might be degraded. Try to leave at least 5mm of distance to the closest object.

### 3D cases

<div style="text-align: center;"><img src="../img/reach/specs/reach_in_case.jpg" style="width: 550px;"></div><br>


The following printable 3D cases are available for Reach users:

**Reach case model C:**

<script src="https://embed.github.com/view/3d/emlid/hardware/master/Reach_cases/Reach_case_assembly_Rev_C.STL"></script>

Download [top and bottom halves](https://github.com/emlid/hardware/tree/master/Reach_cases/Rev_C_parts) of the case to print it.

**Reach case model D:**

<script src="https://embed.github.com/view/3d/emlid/hardware/master/Reach_cases/Reach_case_assembly_Rev_D.STL"></script>

Download [top and bottom halves](https://github.com/emlid/hardware/tree/master/Reach_cases/Rev_D_parts) of the case to print it.

**Reach case model E:**

<script src="https://embed.github.com/view/3d/emlid/hardware/master/Reach_cases/Reach_case_assembly_Rev_E.STL"></script>

Download [top and bottom halves](https://github.com/emlid/hardware/tree/master/Reach_cases/Rev_E_parts) of the case to print it.

For assebmly cases D and E use DIN-7981 screw (thread size 2.2 mm, length either 6.5 or 9.5 mm). Model C can be assembled using scotch tape.

## Electrical specs

### Maximum ratings

|Name                                       | Value                |
|-------------------------------------------|----------------------|
| Inout voltage on USB and DF13 connectors  | 4.75 - 5.5 V         |
| Logic levels on all pins                  | 3.3 V                |
| Max input voltage on all pins             | 5.5 V                |
| Antenna DC bias                           | 3.3 V                |
| Antenna output current                    | 100 mA               |
| Max current consumption @5V               | 500 mA               |
| Normal current consumption @5V            | 200 mA               |
| Current limit on USB OTG                  | 1000 mA              |
| Temperature range                         | 0 +40 C (-40 +85 C)^ |

Officially Intel Edison is rated 0C to 40C, but Intel also claims they are performing temperature tests with good results, but just are not yet ready to officially rate Edison as extended temperature range device. Users report successful tests down to -40 C.

### Connectors pinout
<div style="text-align: center;"><img src="../img/reach/specs/reach-connectors.png" style="width: 550px;"></div><br>

* GPIO46, GPIO77, PWM, SCL, SDA, TX, RX are connected to Intel Edison via buffers and are 3.3 V logic level, 5 V tolerant.
* TX and RX belong to UART1 on Intel Edison
* SCL and SDA belong to I2C1 on Intel Edison, I2C1 also could be used to communicate with internal magnetometer in MPU9250.
* PWM belongs to PWM3 GPIO183 on Intel Edison
* Time Mark input is connected directly to U-blox chip for low latency, it includes an over-voltage clamp, pull up and current limiting resistor.

### USB OTG

<div style="text-align: center;"><img src="../img/reach/specs/otg-connection.png" style="width: 550px;"></div><br>

Reach can both receive power from USB, acting as a device and source power to the port acting as a host. To use Reach in OTG mode you will need to connect 5V power source to DF13 connector pins (5 V, GND) and use OTG USB cable.
