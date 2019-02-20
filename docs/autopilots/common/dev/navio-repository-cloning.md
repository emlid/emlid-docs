## Downloading drivers and examples

Clone our repository to get access to examples:
```bash
git clone https://github.com/emlid/Navio2.git
cd Navio2
```  

For Navio+ this is essentially the same: 

```bash
git clone https://github.com/emlid/Navio.git
cd Navio
```  

## Repository structure

### C++

*- Examples*

Basic examples showing how to work with Navio's onboard devices using C++.

* AccelGyroMag
* ADC
* AHRS
* Barometer
* GPS
* LED 2
* RCInput
* Servo

*- Navio*

C++ drivers for Navio's onboard devices and peripheral interfaces.

* MPU9250 SPI
* LSM9DS1 SPI
* U-blox SPI
* MS5611 I2C
* I2C driver
* SPI driver

### Python

Basic examples showing how to work with Navio's onboard devices using Python.

* AccelGyroMag
* ADC
* Barometer
* GPS
* LED
* RCInput
* Servo

### Utilities

Applications and utilities for Navio2.

* 3D IMU visualizer
* U-blox SPI to PTY bridge utility
* U-blox SPI to TCP bridge utility
