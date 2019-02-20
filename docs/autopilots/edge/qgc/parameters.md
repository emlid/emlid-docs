### Reboot

For rebooting ArduPilot go to the `Vehicle Setups` menu <img src="../../img/qgc/vehicle_setup_menu.png" style="width:30px; vertical-align: middle">  and there choose `Parameters` tab. Further click on `Tools` and `Reboot Vehicle` after.

<div style="text-align: center;"><img src="../../img/qgc/reboot.png"></div><br>


### Telemetry

For UART radio connection use SER2-ADC (ttyAMA0). To change port configuration you can use SERIAL1_ parameters.

Since v1.3 connected USB radio (ttyUSB.Radio) will be recognized. To change port configuration you can use SERIAL2_ parameters.

Both ports have default baud rate 57600.

### GPS and Magnetometer

For external GPS (UART) and Magnetometer (I2C) you can use SER1-I2C (ttyS0) port. To enable GPS in ArduPilot you also need to set GPS2_TYPE parameter to AUTO and reboot.
