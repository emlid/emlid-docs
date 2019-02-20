![3DIMU](http://www.emlid.com/wp-content/uploads/2014/10/3DIMU.png)

One of examples for Navio demonstrates the work of Mahony AHRS with the data from an onboard MPU9250 or LSM9DS1 sensor. We’ve also made a simple but cool visualizer for it that you can run on your PC\Mac. Here’s the instruction how to run AHRS and visualizer:

### Preparing your Mac

Install [pip](https://pip.pypa.io/en/latest/installing.html) and use it to get required packages:

```bash
sudo pip install PyOpenGL PyOpenGL_accelerate
sudo pip install pyserial
```

You might be asked to install command line developer tools along the way.

### Preparing your PC

* Install [Python](https://www.python.org/downloads/release/python-2712/)
* Install [OpenGL](https://pypi.python.org/pypi/PyOpenGL/3.0.2)
* Install [Pyserial](https://pypi.python.org/pypi/pyserial/2.7)
* Download [Freeglut binaries](http://files.transmissionzero.co.uk/software/development/GLUT/freeglut-MinGW.zip) and place 32-bit and 64-bit DLLs to Windows 32-bit (C:\Windows\SysWOW64) and 64-bit (C:\Windows\System32) folders

### On Mac
Download [the archive with Navio utilities](https://github.com/emlid/Navio2/archive/master.zip).
Extract the archive, enter the directory with 3DIMU utility and run it:

```bash
cd Navio2/Utilities/3DIMU
python 3Dimu.py
```

### On PC
Download [the archive with Navio utilities](https://github.com/emlid/Navio2/archive/master.zip).
Extract the archive, enter the directory with 3DIMU utility, open .py file with Python. Make sure Windows Firewall is off.

### On Raspberry Pi

Clone Navio repository using the following [instructions](navio-repository-cloning/).
Navigate to the folder with AHRS example, compile and run it:

```bash
cd C++/Examples/AHRS
make
./AHRS -i [sensor name] X.X.X.X 7000
```

Where X.X.X.X is an ip address of your PC. 7000 is the port number used in 3DIMU. Argument [sensor name] allows you to choose inertial measurement unit: mpu is MPU9250, lsm is LSM9DS1.

Now try to move your Navio and check how the “brick” on the screen moves along with it.
