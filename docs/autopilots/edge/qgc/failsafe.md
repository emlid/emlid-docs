## Wi-Fi RSSI failsafe

Edge supports Return-To-Launch in cases where RSSI (received signal strength indicator) between the pilot’s WiFi module and the flight controller’s AP
falls below certain value.

You can set it in `Safety` tab in `Vehicle Setup` menu:

<div style="text-align: center;"><img src="../../img/qgc/wifi_rssi_failsafe.png"></div><br>

!!! note
    Every Vehicle type has its own `Safety` tab

By default this failsafe is disabled. You can choose `Low` or `Medium` value according to required signal level.
