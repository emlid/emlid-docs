## Emlidtool

### What is Emlidtool?

Emlidtool is pre-installed utility that makes your experience with autopilot easier.
![emlidtool](/img/emlidtool/emlidtool.png)

### Overview

Generally emlidtool has five available options: info, test, ardupilot, rcio, status.

### Info 

Show information about the system.

Usage:

```
emlidtool info
```

This will produse an output like this:
```
emlidtool version: 1.0.3
Vendor: Emlid Limited
Product: Edge
Issue: Emlid 2017-12-30 v1.3
Kernel: 4.9.45-3db5e7e-emlid-v7+
```

### Test 

Run simple tests on the device. 

Usage:

```
emlidtool tests [sensors]
```

You can specify which sensors you want to test.

Running tests without arguments has the same effect as specifying 'all'. 

### Ardupilot 

Helps you to configure and enable ArduPilot on boot.

Usage:

```
emlidtool ardupilot {configure, help}
```

You can choose either 'configure' or 'help'.


'configure' helps you to choose an appropriate software for your device:
```
emlidtool ardupilot configure
```

By default it opens graphical user interface, but if you prefer old-school interface, type:
```
emlidtool ardupilot configure --no-tui
```


You will be supposed to choose your vehicle and frame corresponding to the available list.

Let's say that we have copter. Then we need to enter '1'.

```
1) copter
2) plane
3) rover
4) sub
Type selection number for your vehicle: 1
```

Running ardupilot without arguments or with 'help' shows you a guide explainig how to enable ArduPilot on boot.

### RCIO 

Tool to configure RCIO.  

Usage:

```
emlidtool rcio {check, update}
```

'check' - determine whether you need to update firmware or not.

'update' - update firmware.

Usage:
```
emlidtool rcio update [-p 'path'][-q][-y]
```
where:

-p 'path' - specify firmware path

-q - quiet update (no stdout)

-y - answer 'yes' on all questions

### STATUS

Show status of services on your Edge board.

Usage:
```
emlidtool status
```

You will see following output:

```
module name : (current state), (enable/disable on boot);
```

Example output of this tool look like this:
![status](/img/emlidtool/status_window.png)
