!!! tip ""
	Reach has been replaced with [Reach M+](https://emlid.com/reach). Documentation for Reach M+ can be found [here](https://docs.emlid.com/reachm-plus/).

Reach supports various accessories via it's built-in USB OTG port and UART interface on the DF13 connector

### Radio

It is possible to connect radio modules to Reach in order to obtain corrections or send calculated coordinates.

Most radios nowadays use UART or USB as a connection.

#### Connecting UART radio

Logic level on UART in Reach is 3.3V but pins are 5V tolerant, so you can use both 3.3V and 5V logic level radios.

UART radio is accessible on Reach as a serial device with the name **ttyMFD2**.

To connect UART radio to Reach use upper DF13 port (the one near the USB).

| Reach pins | Radio pins |
|:----------:|:----------:|
|     +5V    |     +5V    |
|     TX     |     RX     |
|     RX     |     TX     |
|     GND    |     GND    |

#### 3DR Radio

<div style="text-align: center;"><img src="../img/reach/hardware-integration/reach-3dr-radio.png" style="width: 550px;"></div><br>

Connection diagram for 3DR Radio v2:

<div style="text-align: center;"><img src="../img/reach/hardware-integration/reach-3dr-radio-connection-map.png" style="width: 550px;"></div><br>

3DR Radio can also be connected over USB.

Please note that a bug in the **Reach image before v1.2** prevents the Rover module from booting while it`s receiving UART correction signals from the base module. Current fix is powering up base module after the rover module has booted (LED are blinking red/blue/white).

#### RFD900 Radio

<div style="text-align: center;"><img src="../img/reach/hardware-integration/reach-rfd900-radio.png" style="width: 550px;"></div><br>

Connection diagram for RFD900 radio:

<div style="text-align: center;"><img src="../img/reach/hardware-integration/reach-rfd900-radio-connection-map.png" style="width: 550px;"></div><br>

!!! attention
    Please mind that RFD can consume up to 800ma in peaks so make sure that your power source can provide enough power for both Reach and RFD900.

#### Connecting USB radio

<div style="text-align: center;"><img src="../img/reach/hardware-integration/reach-usb-radio.png" style="width: 550px;"></div><br>

To connect USB radio to Reach use USB-OTG cable provided with the package.
Plug radio into USB-F port and plug Micro-USB end of the cable in Reach.
**When using USB port in OTG mode Reach has to be [powered](power-supply.md) over one of the DF13 ports**.
