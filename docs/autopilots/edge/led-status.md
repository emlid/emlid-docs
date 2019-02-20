## Edge LED indicators

Edge has two LEDs, which are used as status indicators

| System part | Indicator |
|-----------|------|
|<div style="margin-top: 25px">Status</div>|<div><img src="../img/led-status/status_led_green.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Wi-Fi</div>|<div><img src="../img/led-status/wifi_led_blue.png" style="height: 70px;"></div>  |

### Status LED

| LED state | Demo |
|-----------|------|
|<div style="margin-top: 25px">Off</div>|<div><img src="../img/led-status/status_led_inactive.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Waiting for firmware update</div>|<div><img src="../img/led-status/status_led_cyan.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Firmware update mode</div>|<div><img src="../img/led-status/status_led_cyan_breathing.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Booting</div>|<div><img src="../img/led-status/status_led_white_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Bootstrapping</div>|<div><img src="../img/led-status/status_led_white.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Preparation for RCIO update </div>|<div><img src="../img/led-status/status_led_cyan_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Disarmed, no GPS lock</div>|<div><img src="../img/led-status/status_led_blue_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Armed, no GPS lock</div>|<div><img src="../img/led-status/status_led_blue.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Disarmed, GPS lock</div>|<div><img src="../img/led-status/status_led_green_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Armed, GPS lock</div>|<div><img src="../img/led-status/status_led_green.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Pre-arm checks failure</div>|<div><img src="../img/led-status/status_led_yellow_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Error</div>|<div><img src="../img/led-status/status_led_red.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Gyros Initialiazation</div>|<div><img src="../img/led-status/status_led_red_blue_blinking.gif" style="height: 70px;"></div>  |

### Wi-Fi LED

| LED state | Demo |
|-----------|------|
|<div style="margin-top: 25px">Access point mode</div>|<div><img src="../img/led-status/wifi_led_blue.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Activating access point network</div>|<div><img src="../img/led-status/wi-fi_led_blue_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Client mode</div>|<div><img src="../img/led-status/wifi_led_green.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Connecting to client network</div>|<div><img src="../img/led-status/wi-fi_led_green_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Resolving network type</div>|<div><img src="../img/led-status/wi-fi_led_white_blinking.gif" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">No Wi-Fi device</div>|<div><img src="../img/led-status/wifi_led_red.png" style="height: 70px;"></div>  |
|<div style="margin-top: 25px">Connection error</div>|<div><img src="../img/led-status/wi-fi_led_red_blinking.gif" style="height: 70px;"></div>  |

LEDs' colors and sequences depend on the frame you use. So we ask you to refer 
to [ArduPilot’s docs](http://ardupilot.org/copter/docs/common-leds-pixhawk.html) for the exact meaning of each sequence.
