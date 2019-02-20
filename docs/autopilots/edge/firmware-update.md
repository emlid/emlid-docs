

## Connect Edge to a computer

!!! notice 
	Power off Edge before connecting it to the computer
	
To connect Edge to your computer use a Micro-USB to USB-A cable from the kit.

* Plug Micro-USB connector into the PC port on Edge
* Plug another end of the cable into a USB port on your computer

<div style="text-align: center;"><img src="../img/firmware-update/pc_to_edge.png" style="width: 550px;"></div><br>

## Flash your Edge

### QGroundControl (Windows/Linux/OSX)

!!! tip
	Graphical user interface depends on your system. Main steps are equivalent for all supported operating systems.

Open QGroundControl, choose `Setup` <img src="../img/firmware-update/qgc/qground_setup_ico.png" style="width:30px; vertical-align: middle"> menu and go to `Firmware` tab

<div style="text-align: center;"><img src="../img/firmware-update/qgc/start.png" style="width: 800px;"></div><br>

Plug in your device (If you did not do it before) and wait until QGroundControl automatically detects it.

<div style="text-align: center;"><img src="../img/firmware-update/qgc/edge_available.png" style="width: 800px;"></div><br>

Next, click on the `Connect` button to start initialization your device.

!!! tip 
	On Linux QGroundControl will ask you for administrative privileges.

<div style="text-align: center;"><img src="../img/firmware-update/qgc/edge_connected.png" style="width: 800px;"></div><br>

Wait several seconds while QGrounControl initializes your device.

<div style="text-align: center;"><img src="../img/firmware-update/qgc/init_start.png" style="width: 800px;"></div><br>

After initialization completes, you'll see this dialog with:

* Needed disk space for download and exatract firmware image
* Release date of new firmware
* Available version of firmware for Edge
* Current version of plugged Edge 

<div style="text-align: center;"><img src="../img/firmware-update/qgc/prefs_menu.png" style="width: 800px;"></div><br>

Next, you should click `Ok` and firmware update will start. 
You can cancel the update process by pressing `Cancel` button.

<div style="text-align: center;"><img src="../img/firmware-update/qgc/flasher_running.png" style="width: 800px;"></div><br>

When firmware update complete, you can unplug your device.

