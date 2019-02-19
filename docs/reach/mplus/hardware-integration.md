
Reach supports various accessories via it's built-in USB OTG port and UART interface on the JST-GH connectors.

### Radio

It is possible to connect radio modules to Reach in order to obtain corrections or send calculated coordinates.

Most radios nowadays use UART or USB as a connection.

#### Connecting UART radio

Logic level on UART in Reach is 3.3V but pins are 5V tolerant, so you can use both 3.3V and 5V logic level radios.

UART radio is accessible on Reach as a serial device with the name **ttyMFD2**.

To connect UART radio to Reach use lower JST-GH port (S1).

| Reach pins | Radio pins |
|:----------:|:----------:|
|     +5V    |     +5V    |
|     TX     |     RX     |
|     RX     |     TX     |
|     GND    |     GND    |

#### 3DR Radio

<div style="text-align: center;"><img src="../img/reachm-plus/hardware-integration/3dr.png" style="width: 700px;"></div><br>


3DR Radio can also be connected over USB.

#### RFD900 Radio

<div style="text-align: center;"><img src="../img/reachm-plus/hardware-integration/rfd.png" style="width: 700px;"></div><br>

!!! attention
    Please mind that RFD can consume up to 800ma in peaks so make sure that your power source can provide enough power for both Reach and RFD900.

<br>
#### Connecting USB radio or LTE modem

<div style="text-align: center;"><img src="../img/reachm-plus/hardware-integration/lte-modem.png" style="width: 700px;"></div><br>

To connect USB radio or LTE-modem to Reach use USB-OTG cable provided with the package.
Plug radio into USB-F port and plug Micro-USB end of the cable in Reach.
**When using USB port in OTG mode Reach has to be [powered](power-supply.md) over one of the JST-GH ports**.

!!! note "Connecting LTE modem"
	Make sure that Reach M+ is in hotspot mode, and an LTE modem is preconfigured to connect to the Internet automatically after powering.
<br>
#### Connecting LoRa radio

<div style="text-align: center;"><img src="../img/reachm-plus/hardware-integration/lora.png" style="width: 700px;"></div><br>

To connect LoRa radio to Reach use upper JST-GH port (S2).