## Reach RS LED indicators

Reach RS has three LEDs, which are used as status indicators for three different parts of the system:

* Power - <font color="red">red</font>
* Network - <font color="blue">blue</font>
* Stat - <font color="green">green</font>

### Reach RS boot LED sequence

During boot Reach RS will go through 3 steps:

* Network scan
* Time sync
* ReachView launch

### Power and power button

Power led is on to show Reach RS is turned on. If you hold down the power button to turn Reach RS off, the led will confirm system shutdown by three fast blinks.

### Network state

Reach RS will indicate a network scan with very fast <font color="blue">blue</font> blinks. If a known Wi-Fi network is detected, Reach RS will connect to it and set the Network LED to do short blinks. If the scan found no familiar networks, a hotspot is started and the LED will start breathing slowly.

### Time sync

Time sync is indicated by fast <font color="green">green</font> blinks on the Stat LED.

### ReachView launch

!!! note
    The app will not launch until the time sync is complete. Internet connection allows this to happen automatically, but in hotspot mode Reach RS requires some satellite visibility.

After the time sync is done the Stat LED blinks stop and ReachView will be launched. Successful launch will be signified with a solid <font color="green">green</font> light on the Stat indicator, fail will make the Stat LED turn off.


**More interactive and informative LED statuses will be introduced in one of the future updates.**