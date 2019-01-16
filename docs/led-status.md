!!! success " "
    LED functionality is available with ReachView version 2.7.0 and newer 

## Reach RS/RS+ LED indicators

Reach RS/RS+ has three LEDs, which are used as status indicators for three different parts of the system:

| System part | Indicator |
|-----------|------|
|Power|<div style="text-align: center;"><img src="../img/reachrs/led-status/orange.png" style="width: 30px;"></div>  |
|Network|<div style="text-align: center;"><img src="../img/reachrs/led-status/blue.png" style="width: 30px;"></div>  |
|Stat|<div style="text-align: center;"><img src="../img/reachrs/led-status/green.png" style="width: 30px;"></div>  |



### Power LED and power button

| LED state | Demo |
|-----------|------|
|Normal operation|<div style="text-align: center;"><img src="../img/reachrs/led-status/orange.png" style="width: 30px;"></div>  |
|Battery charge|<div style="text-align: center;"><img src="../img/reachrs/led-status/charge.gif" style="width: 30px;"></div>  |
|Low battery|<div style="text-align: center;"><img src="../img/reachrs/led-status/low-battery.gif" style="width: 30px;"></div>  |

Power LED will also confirm shutdown(after holding the power button for three seconds) with **three fast blinks**.

### Network LED

During boot, Reach RS/RS+ enters a network scan state in which it will try to connect to any known Wi-Fi networks it can find. This might result in connecting to a previously added network or creating its own hotspot.

| LED state | Demo |
|-----------|------|
|Scanning|<div style="text-align: center;"><img src="../img/reachrs/led-status/network-scanning-led.gif" style="width: 30px;"></div>  |
|Client Wi-fi mode|<div style="text-align: center;"><img src="../img/reachrs/led-status/client-led.gif" style="width: 30px;"></div>  |
|Hotspot mode|<div style="text-align: center;"><img src="../img/reachrs/led-status/blue.png" style="width: 30px;"></div>  |

The Network LED behavior changes every time you change the Wi-Fi mode via ReachView. It will reflect turning hotspot on, scanning and connecting to existing wireless networks.

### Stat LED

Stat LED is used to display ReachView status. 

| LED state | Demo |
|-----------|------|
|Time sync|<div style="text-align: center;"><img src="../img/reachrs/led-status/time-sync-led.gif" style="width: 30px;"></div>  |
|Normal operation|<div style="text-align: center;"><img src="../img/reachrs/led-status/green.png" style="width: 30px;"></div>  |
|Point collection|<div style="text-align: center;"><img src="../img/reachrs/led-status/point-collection-led.gif" style="width: 30px;"></div>  |
|Internal error|<div style="text-align: center;"><img src="../img/reachrs/led-status/grey.png" style="width: 30px;"></div>  |

!!! attention
    Reach RS/RS+ requires time syncing only during first time setup. Internet connection, which is required for the first setup anyway, will allow time syncing process to happen automatically.

### LED Behavior

The table below demonstrates possible flash patterns describing various states of the receiver.  


| Reach State  |  Demo |
|--------------|-------|
|<br><br><br><br> <div style="text-align: center;">    OFF   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/off.png" style="height: 250px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Reach RS+ charging   </div>   | <br> <div style="text-align: center;"><img src="../img/reachrs/led-status/RS-plus-charging.gif" style="height: 250px;"></div> |
|<br><br><br><br> <div style="text-align: center;">   Reach RS charging     </div>   | <br> <div style="text-align: center;"><img src="../img/reachrs/led-status/off.png" style="height: 265px;"></div>  |
|<br><br><br><br> <div style="text-align: center;">    Reach RS+ charging after connecting the cable   </div>|<br> <div style="text-align: center;"><img src="../img/reachrs/led-status/RS-plus-charging-after-connecting-the-cable.gif" style="height: 250px;"></div>|
|<br><br><br><br> <div style="text-align: center;">    Reach RS behavior after connecting the cable   </div>|<br> <div style="text-align: center;"><img src="../img/reachrs/led-status/RS-no-reaction.gif" style="height: 250px;"></div>|
|<br><br><br><br> <div style="text-align: center;">    Loading   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/loading.gif" style="height: 265px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Reach RS+ loading after connecting the cable   </div>|<br> <div style="text-align: center;"><img src="../img/reachrs/led-status/RS-plus-loading-after-connecting-the-cable.gif" style="height: 250px;"></div>|
|<br><br><br><br> <div style="text-align: center;">    Time sync   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/time-sync.gif" style="height: 250px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Low battery   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/lack-of-power.gif" style="height: 250px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Network scan   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/network-scan.gif" style="height: 250px;"></div> |
|<br><br><br><br> <div style="text-align: center;">     App running, client Wi-Fi mode   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/running-client.gif" style="height: 250px;"></div>
|<br><br><br><br> <div style="text-align: center;">    App running, hotspot mode   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/running-hotspot.png" style="height: 250px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Point collection <br> _assuming the device is in hotspot mode_   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/point-collection.gif" style="height: 250px;"></div>
|<br><br><br><br> <div style="text-align: center;">    Internal error <br> _assuming the device is in hotspot mode_   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachrs/led-status/error.png" style="height: 250px;"></div>
