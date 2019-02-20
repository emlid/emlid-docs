####Mounting Navio on Raspberry Pi

Navio was designed to fit on top of Raspberry Pi Model A and Model B, however it also works with Raspberry Pi Model B+ due to the backward compatibility between them.  Mounting hole is 2.9mm to accommodate M2.5 screw or bolt.

####Powering Navio and Raspberry Pi

***From the single power source over USB***

This method could be used for working with sensor data only. Raspberry Pi powers the Navio board but no voltage on the servo rail is present. 5VRPI pin on header corresponds to Raspberry Pi 5V network and is directly connected to USB source. Never connect two power sources to this network at the same time, it will damage the power supply. If you just want to do PPM decoding or power something over the servo rail you can add a jumper between 5VRPI and BEC. This way the whole servo rail is powered from the Pi, please do not connect servos in this configгration, it will cause voltage spikes and Raspberry Pi will reboot. Use power adapters that can handle at least 1A of current.

***From separate power sources over 5VRPI and BEC power inputs on servo header***

In case you want to control servos, motors or other high power loads it is necessary to use separate power sources for Navio servo rail and Raspberry Pi since the latter is very sensitive to voltage dropouts. Use two BECs or another DC sources that provide 5V and connect them to 5VRPI and BEC inputs on Navio board.
5VRPI input and BEC input should be strictly 4.75-5.25V.

***Voltage levels on ports and headers***

* Servo rail power pins – 5V
* Servo rail PWM pins – 5V
* PPM input pin – 5V
* UART, SPI, I2C port power pins – 5V
* UART, SPI, I2C signal pins – 3.3V (**CAUTION!** connecting 5V logic device to these pins may damage your Raspberry Pi!)
* ADC power pin – 3.3V output
* ADC signal pins – 0V-3.3V input

####Connection map
![map](img/Navio-ConnectionMap.jpg)


Raspberry Pi provides a set of peripheral interfaces which can be used to connect additional hardware. Navio provides access to these interfaces on it's ports. Even though the set of interfaces is limited, it is possible to add more by using USB adapters. This guide demonstrates how different hardware can be connected to Navio and how to properly power it up in a drone.
####Typical hardware setup
![Navio-typical-gear-setup](img/Navio-AntennaRadioBECs.jpg)

####Power
Raspberry Pi is sensitive to voltage drop-outs as they cause it to reboot, to protect it we separated power circuits for Raspberry Pi \ sensors and servo rail \ ports. Power input for Raspberry Pi and sensors is labeled '5VRPI', while power input for servo rail and ports is labeled 'BEC' and both are located on 2.54mm header. That way by using two different power sources you can connect servos, radio modem and other power-hungry loads without disturbing Raspberry Pi.


If you are not connecting any high load you can simply power Raspberry Pi and Navio's sensors using Pi's microUSB socket. Do not connect power to the microUSB socket and '5VRPI' input simultaneously, it will damage the boards.

Acceptable voltage level for Raspberry Pi is 4.75-5.25V, provided current should be at least 1A for Raspberry Pi + Navio.

####PPM Input
RC receiver's PPM output should be connected to 'PPM' pin on 2.54mm header. 'PPM' input accepts signal with 5V level.

####RC outputs
RC outputs on 2.54mm header provide PWM values with 5V voltage level that can be used to control servos or motors. Functions that are designated to RC outputs can be found in APM [plane](http://ardupilot.org/plane/docs/arduplane-setup.html), [copter](http://ardupilot.org/copter/docs/initial-setup.html), [rover](http://ardupilot.org/rover/docs/apmrover-setup.html) setup guides.

####GNSS antenna
GNSS antenna for Navio's onboard GNSS receiver should be connected to the u.fl socket labeled 'ANT'.

####Radio modem
Radio modems that work over UART interface can be connected to the Navio's UART port. Please note that power on UART port is 5V and it is powered by the 'BEC' power input.

####External compass
MPU9250 sensor onboard of Navio contains magnetometer, but optionally it is possible to use external compass. There are a lot of HMC5883L breakout boards, but for such board to be compatible it is required that the board can be powered by 5V.

####External GPS
Optionally it is possible to connect external GPS and compass, but not necessary as Navio already contains an onboard GNSS receiver and compass. As UART and I2C ports on Navio have the same pinouts as on Pixhawk it is possible to connect any Pixhawk-compatible GNSS modules with their provided wires, they usually have an external compass built-in which can be used too by connecting over I2C DF13 wire. Older modules such as ones for APM 2.5 could be used with proper wiring.

####Radio over USB
As Raspberry Pi only has one UART interface in case you would like to use an external GPS there would be no UART ports left for a radio modem. In that case it is possible to add more UART ports by using USB-to-UART adapters that are usually built with Silabs CP210x or FTDI chips such as [this one](https://www.sparkfun.com/products/718).

####Voltage and current sense
![Navio-current-and-voltage-sense](img/Navio-CurrentAndVoltageSense.jpg)

To measure battery's voltage and current use sense boards that provide measurements scaled to 3.3V. Series of AttoPilot voltage and current sense boards rated for different currents can be used for these purposes. Connect A0 and A1 channels of ADC to the voltage and current sense correspondingly.

#### Barometer UV protection

MS5611 barometer (steel cap IC) is sensitive to UV light and might report sudden jumps in altitude under sunlight. It is very important to cover it with a piece of cloth (something like microphone fabric) or put autopilot in a protective case to protect it both from sunlight and airstreams.
