## MPU9250 and LSM9DS1

Navio2 contains two 9DOF (degree of freedom) IMU - MPU9250 and LSM9DS1. Each of them combines a gyroscope, an accelerometer and a magnetometer in one device. IMU sensors are not only popular as a part of drone autopilot projects, but are also widely used in devices like cellphones, tablets, etc.

## IMU example

If you haven't already done that, download Navio2 drivers and examples code [here](navio-repository-cloning/).

IMU example for Navio2 runs with one of the on-board sensors at a time. During start-up program you have to specify with which sensor to work.

### C++ 
Move to the folder with the source code, compile and run the example:

```bash
cd C++/Examples/AccelGyroMag
make
./AccelGyroMag -i [sensor name]
```

### Python  
Move to the folder with the source code, compile and run the example:
```bash
cd Python
python AccelGyroMag.py -i [sensor name]
```
Argument [sensor name] allows you to choose inertial measurement unit: mpu is MPU9250, lsm is LSM9DS1.

!!! tip
    LSM9DS1 driver is currently not implemented. Use the C++ counterpart

You should immediately see 9 values, updated in real time. Try to move the device around and see them change. They include Accelerometer, Gyroscope and Magnetometer data, three axis each.  
```bash
Selected: MPU9250
Connection established:  True
Acc:  +0.014  +0.139  +9.974  Gyr:   -0.042   +0.022   +0.011  Mag: -3525.450 +29.584  +0.000
Acc:  -0.010  +0.268 +10.036  Gyr:   -0.042   +0.019   +0.015  Mag: -14.963 +43.390 -50.130
Acc:  -0.010  +0.278  +9.888  Gyr:   -0.043   +0.021   +0.012  Mag: -16.566 +42.852 -50.302
Acc:  +0.010  +0.187 +10.041  Gyr:   -0.039   +0.021   +0.011  Mag: -14.963 +42.314 -50.817
Acc:  -0.062  +0.158  +9.855  Gyr:   -0.039   +0.020   +0.011  Mag: -15.497 +42.493 -49.959
Acc:  -0.067  +0.196 +10.056  Gyr:   -0.044   +0.020   +0.013  Mag: -14.963 +43.748 -50.130
```  

For further information see source code. Function ```create_inertial_sensor()``` creates object of class MPU9250 or LSM9DS1 depending on the argument passed to the program.
The next thing we should pay attention to is the line ```sensor->initialize()```, as it does an important job of setting internal device parameter. Note that this function also sets scales for both Accelerometer and Gyroscope (and for Magnitometer in case of LSM9DS1).  
The main function loop is pretty straightforward: read the data, print the data.

You can find additional information about the chips in [MPU-9250 datasheet](http://store.invensense.com/datasheets/invensense/MPU9250REV1.0.pdf) and [LSM9DS1 datasheet](http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/DM00103319.pdf).
