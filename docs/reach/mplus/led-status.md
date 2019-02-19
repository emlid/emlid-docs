!!! success " "
    LED functionality is available with ReachView version 2.7.0 and newer 

## Reach M+ LED indicators

Reach M+ has three LEDs, which are used as status indicators for three different parts of the system:

| System part | Indicator |
|-----------|------|
|Power|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/orange.png" style="width: 30px;"></div>  |
|Network|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/blue.png" style="width: 30px;"></div>  |
|Stat|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/green.png" style="width: 30px;"></div>  |



### Power LED 

| LED state | Demo |
|-----------|------|
|Reach M+ is OFF |<div style="text-align: center;"><img src="../img/reachm-plus/led-status/grey.png" style="width: 30px;"></div>  |
|Normal operation|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/orange.png" style="width: 30px;"></div>  |


### Network LED

During boot, Reach M+ enters a network scan state in which it will try to connect to any known Wi-Fi networks it can find. This might result in connecting to a previously added network or creating its own hotspot.

| LED state | Demo |
|-----------|------|
|Scanning|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/network-scanning-led.gif" style="width: 30px;"></div>  |
|Client Wi-fi mode|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/client-led.gif" style="width: 30px;"></div>  |
|Hotspot mode|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/blue.png" style="width: 30px;"></div>  |

The Network LED behavior changes every time you change the Wi-Fi mode via ReachView. It will reflect turning hotspot on, scanning and connecting to existing wireless networks.

### Stat LED

Stat LED is used to display ReachView status. 

| LED state | Demo |
|-----------|------|
|Time sync|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/time-sync-led.gif" style="width: 30px;"></div>  |
|Normal operation|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/green.png" style="width: 30px;"></div>  |
|Point collection|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/point-collection-led.gif" style="width: 30px;"></div>  |
|Internal error|<div style="text-align: center;"><img src="../img/reachm-plus/led-status/grey.png" style="width: 30px;"></div>  |


### Time sync
After network configuration is done, green LED will start blinking. It is shown during time sync.

!!! Attention
    The app will not launch until the time sync is complete. Internet connection allows this to happen automatically, but in hotspot mode Reach requires a connected antenna with some satellite visibility.



### LED Behavior

The table below demonstrates possible flash patterns describing various states of the receiver.  


| Reach State  |  Demo |
|--------------|-------|
|<br><br><br><br> <div style="text-align: center;">    OFF   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/off.png" style="height: 150px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Loading   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/loading.gif" style="height: 150px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Time sync   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/time-sync.gif" style="height: 150px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Network scan   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/network-scan.gif" style="height: 150px;"></div> |
|<br><br><br><br> <div style="text-align: center;">     App running, client Wi-Fi mode   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/running-client.gif" style="height: 150px;"></div>
|<br><br><br><br> <div style="text-align: center;">    App running, hotspot mode   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/running-hotspot.gif" style="height: 150px;"></div> |
|<br><br><br><br> <div style="text-align: center;">    Point collection <br> _assuming the device is in hotspot mode_   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/point-collection.gif" style="height: 150px;"></div>
|<br><br><br><br> <div style="text-align: center;">    Internal error <br> _assuming the device is in hotspot mode_   </div>   | <br>  <div style="text-align: center;"><img src="../img/reachm-plus/led-status/error.png" style="height: 150px;"></div>
