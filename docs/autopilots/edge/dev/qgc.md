# QGroundControl

## Building

### Source code
You can get the source code of QGroundControl by typing these commands
```
$ git clone https://github.com/emlid/qgroundcontrol
$ cd qgroundcontrol
$ git submodule update --init --recursive
```

### Supported builds
Currently, ```QGroundControl for Edge``` supports builds for ```Windows``` and ```Linux```. 

### Requirements
#### Compiler
- ```Windows``` - [Visual Studio 2015 compiler](http://www.visualstudio.com/downloads/download-visual-studio-vs#d-express-windows-desktop)
- ```Linux(Ubuntu)``` - g++ 64 bit: 
```$ sudo apt-get install build-essential```

#### Qt
You need to install Qt as described below instead of using pre-built 
packages from say, a Linux distribution, because QGroundControl needs access to private Qt headers.

- Download the [Qt installer](http://www.qt.io/download-open-source).
  - Make sure to install **Qt** version **5.9.1 ONLY with QtRemoteObjects framework**.
  - **Ubuntu**: Set the downloaded file to executable using: ```$ chmod +x```. 
  Install to default location for use with ```./qgroundcontrol-start.sh```
  - If you install Qt to a non-default location you will need to modify qgroundcontrol-start.sh 
in order to run downloaded builds.

!!! danger "Attention"
	Windows: Make sure to install VS 2015 32 bit package.

#### Additional packages
- **Linux(Ubuntu)**: ```$ sudo apt-get install espeak libespeak-dev libudev-dev libsdl2-dev libblkid-dev```

#### Video streaming
- **Linux(Ubuntu)**: ```$ sudo apt-get install gstreamer1.0*```
- **Windows**: 
  You need two packages:
  - [gstreamer-1.0-devel-x86-1.5.2.msi](https://gstreamer.freedesktop.org/data/pkg/windows/1.5.2/gstreamer-1.0-devel-x86-1.5.2.msi)
  - [gstreamer-1.0-x86-1.5.2.msi](https://gstreamer.freedesktop.org/data/pkg/windows/1.5.2/gstreamer-1.0-x86-1.5.2.msi)
  
!!! danger "Attention"
	Make sure you select "Complete" installation instead of "Typical" installation during the install process. The installer places them under c:\gstreamer, which is where the QGC build system will look for it.

### Building using Qt Creator (Windows and Linux)

- Launch Qt Creator and open the `qgroundcontrol.pro` project.
- Select the appropriate kit for your needs:
  - **Linux(Ubuntu)**: Desktop Qt 5.9.1 GCC bit
  - **Windows**: Desktop Qt 5.9.1 MSVC2015 32bit
  
### Shadow build from command line
From ```QGroundControl``` directory

```
$ cd ..
$ mkdir qgrondcontrol_build
$ cd qgroundcontrol_build
$ qmake ../qgroundcontrol/qgroundcontrol.pro CONFIG+=release # or debug
$ make
```
