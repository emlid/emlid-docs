!!! tip ""
	Reach has been replaced with [Reach M+](https://emlid.com/reach). Documentation for Reach M+ can be found [here](https://docs.emlid.com/reachm-plus/).


!!! success " "
    LED functionality is available with ReachView version 2.7.0 and newer 


## Reach boot LED sequence

Reach LED is an RGB LED that cycles through a simple pattern:

Network state -> App state

During boot Reach will go through 3 steps:

* Network scan
* Time sync
* ReachView launch

### Network scan

During boot, Reach enters a network scan state in which it will try to connect to any known Wi-Fi networks it can find. This might result in connecting to a previously added network or creating its own hotspot.

| Network state | Demo |
|-----------|------|
|Scanning|<div style="text-align: center;"><img src="../img/reach/led-status/network-scanning-led.gif" style="width: 30px;"></div>  |
|Client Wi-Fi mode|<div style="text-align: center;"><img src="../img/reach/led-status/blue.png" style="width: 30px;"></div>  |
|Hotspot Wi-Fi mode|<div style="text-align: center;"><img src="../img/reach/led-status/white.png" style="width: 30px;"></div>  |


### Time sync

After network configuration is done, **<font color="magenta">magenta</font> blinks** will be added to the LED. They are shown during time sync.

!!! attention
    The app will not launch until the time sync is complete. Internet connection allows this to happen automatically, but in hotspot mode Reach requires a connected antenna with some satellite visibility.

### ReachView launch and operation

After the time sync is done, the **magenta blinks** stop and ReachView is launched. **<font color="green">Green</font> solid** light will take its place, showing app start. You can see several additional states:

| App state | Demo |
|-----------|------|
|Normal app operation|<div style="text-align: center;"><img src="../img/reach/led-status/green.png" style="width: 30px;"></div>  |
|Point collection|<div style="text-align: center;"><img src="../img/reach/led-status/point-collection-led.gif" style="width: 30px;"></div>  |
|App internal error|<div style="text-align: center;"><img src="../img/reach/led-status/red.png" style="width: 30px;"></div>  |


### LED Behavior

The table below demonstrates possible flash patterns describing various states of the receiver.  


| Reach State | Time Sync   -> | Network   -> | App Status | Sequence Demo |
|--------------|-----------|---------------------|---------|-----------|
|<br> <div style="text-align: center;">    OFF   </div>                   | <br>  </div>    |  <br> </div> | <br> </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/off.png" style="width: 150px;"></div>   |
|<br> <div style="text-align: center;">    Lack of power   </div>                   | <br>  <div style="text-align: center;"><img src="../img/reach/led-status/magenta.png" style="height: 30px;"><br>Blinks each 10-15 sec</div>    |  <br> </div> | <br> </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/low-power.gif" style="width: 150px;"></div>   |
|<br> <div style="text-align: center;">    Network scan   </div>                   | <br>  </div>    |  <br> <div style="text-align: center;"><img src="../img/reach/led-status/blue.png" style="height: 30px;"><br>Fast blinks</div> | <br> </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/network-scan.gif" style="width: 150px;"></div>   |
|<br> <div style="text-align: center;">    Time sync in client Wi-Fi mode   </div>                   | <br>  <div style="text-align: center;"><img src="../img/reach/led-status/magenta.png" style="height: 30px;"><br>Solid</div>    |  <br> <div style="text-align: center;"><img src="../img/reach/led-status/blue.png" style="width: 30px;"><br>Solid</div> | <br> </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/time-sync-client.gif" style="width: 150px;"></div>   |
|<br> <div style="text-align: center;">    Time sync in Hotspot mode, <br> _sattelite visibility is required_   </div>                   | <br>  <div style="text-align: center;"><img src="../img/reach/led-status/magenta.png" style="height: 30px;"><br>Solid</div>    |  <br> <div style="text-align: center;"><img src="../img/reach/led-status/white.png" style="width: 30px;"><br>Solid</div> | <br> </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/time-sync-hotspot.gif" style="width: 150px;"></div>   |
|<br> <div style="text-align: center;">    App running,<br> Wi-Fi client mode   </div>                   | <br>  </div>    |  <br> <div style="text-align: center;"><img src="../img/reach/led-status/blue.png" style="height: 30px;"><br>Solid</div> | <br><div style="text-align: center;"><img src="../img/reach/led-status/green.png" style="height: 30px;"><br>Solid </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/running-client.gif" style="width: 150px;"></div>   |
|<br> <div style="text-align: center;">    App running, <br>hotspot mode    </div>                   | <br>  </div>    |  <br> <div style="text-align: center;"><img src="../img/reach/led-status/white.png" style="height: 30px;"><br>Solid</div> | <br><div style="text-align: center;"><img src="../img/reach/led-status/green.png" style="height: 30px;"><br>Solid </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/running-hotspot.gif" style="width: 150px;"></div>   | 
|<br> <div style="text-align: center;"> Point collection, <br> _assuming Reach is_ <br> _in Hotspot mode_     </div>                   | <br>  </div>    |  <br> <div style="text-align: center;"><img src="../img/reach/led-status/white.png" style="height: 30px;"><br>Solid <br> </div> | <br><div style="text-align: center;"><img src="../img/reach/led-status/green.png" style="height: 30px;"><br>Fast blinks </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/point-collection.gif" style="width: 150px;"></div>   |
|<br> <div style="text-align: center;">    Internal error, <br>_assuming Reach is_ <br> _in Hotspot mode_   </div>                   | <br>  </div>    |  <br> <div style="text-align: center;"><img src="../img/reach/led-status/white.png" style="height: 30px;"><br>Solid <br> </div> | <br><div style="text-align: center;"><img src="../img/reach/led-status/red.png" style="height: 30px;"><br>Solid </div>|<br>  <div style="text-align: center;"><img src="../img/reach/led-status/error.gif" style="width: 150px;"></div>   |
