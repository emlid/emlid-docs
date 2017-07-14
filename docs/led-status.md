## Reach RS LED indicators

Reach RS has three LEDs, which are used as status indicators for three different parts of the system:

* Power - <font color="orange">orange</font>
* Network - <font color="blue">blue</font>
* Stat - <font color="green">green</font>

### Power LED and power button

* In normal mode, the LED will stay **solid**
* During battery charge, it will add **rare blinks**
* In case of low battery, the LED will **turn off and start rare blinking** to draw user's attention

Power LED will also confirm shutdown(after holding the power button for three seconds) and plugging in a charge cable with **three fast blinks**.

### Network LED

During boot, Reach RS enters a network scan state in which it will try to connect to any known Wi-Fi networks it can find. This might result in connecting to a previously added network or creating its own hotspot.

* Scanning is shown by **fast blinks**
* Client Wi-Fi mode is **slow blinks**
* Hotspot is **solid** LED

The Network LED behavior changes every time you change the Wi-Fi mode via ReachView. It will reflect turning hotspot on, scanning and connecting to existing wireless networks.

### Stat LED

Stat LED is used to display ReachView status. 

* Before app start, Reach RS might need to perform system time sync, which is signified by **fast blinks**
* **Solid light** represents normal operation
* Point collection is indicated by **fast blinks**, which stop when the collections is complete
* If the LED turns **off**, it means the app is having an internal issue

!!! note
    Reach RS requires time syncing only during first time setup. Internet connection, which is required for the first setup anyway, will allow time syncing process to happen automatically.