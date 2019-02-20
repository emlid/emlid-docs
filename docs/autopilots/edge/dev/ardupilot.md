Edge currently uses a custom Emlid's ArduPilot build. The support for Edge in the upstream ArduPilot repository is currently in progress.

## Building

The building process is not that hard and is basically the same as for other ArduPilot-supported boards like [Navio2](https://docs.emlid.com/navio2/common/ardupilot/building-from-sources/).

 We recommend cross-compiling as it is a fast and convenient way to get things done.
 
### Where to get the code

You can find the sources in our [Emlid ArduPilot repository](https://github.com/emlid/ardupilot).

!!!tip
	The support for Edge in [ArduPilot upstream repository](https://github.com/ardupilot/ardupilot) will be added soon.

### How to build

Here we will describe the process of building ArduPilot using cross-compilation on a Linux-based host machine running Ubuntu.

!!!tip
	The additional information about the building process (including how-to for Windows) can be found in [ArduPilot documentation](http://ardupilot.org/dev/docs/building-the-code.html).
	
First, install the required packages:

```
$ sudo apt-get install build-essential git
$ sudo pip install future
```

Now you have to install the appropriate compiler tools.

You can either install a generic Linux ARM compiler with

```
$ sudo apt-get install gcc-arm-linux-gnueabihf
```
or setup the Raspberry Pi's one using the instructions [here](https://docs.emlid.com/navio2/common/ardupilot/building-from-sources/#cross-compiler-setup-on-linux-optional).

Now it's time to download sources:
```
$ git clone https://github.com/emlid/ardupilot.git
$ cd ardupilot
```
Checkout to the particular branch we're using for Edge:
```
$ git checkout Copter-3.5.3-Edge
```
Update all submodules:
```
$ git submodule update --init --recursive
```
Create a convenient alias for ArduPilot's building software called ```waf```:
```
$ alias waf="$PWD/modules/waf/waf-light"
```
Tell the ```waf``` that we are building ArduPilot for Edge:
```
$ waf configure --board edge
```
And, finally, build the whole thing:
```
$ waf copter -j5
```
!!!tip
	The additional information about ```waf``` can be found on [ArduPilot building instructions page on GitHub](https://github.com/ArduPilot/ardupilot/blob/master/BUILD.md).
	
### How to run

Transfer the compiled binary to your Edge (assuming that you and Edge are on the same WiFi network):
```
$ cd ./build/edge/bin
$ rsync -avz arducopter pi@edge.local:~
```

Perform an SSH connection to your edge with
```
$ ssh pi@edge.local
```
!!!tip
	The default ssh login is ```pi```, password is ```raspberry```.
	
And run the freshly-compiled ArduPilot with
```
$ sudo ./arducopter -A udp:your_IP_address:14550
```
!!!tip
	You can find your IP address with the ```ifconfig``` command.
	
Now you should be able to connect your Edge to your QGroundControl and check that everything is fine.
