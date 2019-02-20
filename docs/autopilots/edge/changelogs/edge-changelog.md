## Edge firmware changelog

### v1.5 (2018-07-04)

System:

* kernel updated to v4.14.34

Modules:

* emlidtool v1.0.7:
    * Edge support:
        * Board information
        * Selftests
        * Status of modules
        * Ardupilot setup
* rcio-firmware v1.3:
    * GPIO support
    * Indication during flashing
* rcio-dkms v1.0.0:
    * Virtual GPIO support
    * Support for kernels >= 4.10
* 8812au-dkms v4.3.21:
    * Support for new kernels
* ardupilot:
    * ArduCopter: 3.5.5
    * ArduPlane: 3.8.5
    * ArduRover: 3.3.0
    * ArduSub: 3.6.0-dev
* wmd v3.0:
    * Based on edged library
    * Setup txpower of AP
    * Seup name and password of AP
* acd v2.0:
    * Based on edge-daemon-skeleton
* WiFi-RSSI-daemon v1.0:
    * WiFi RSSI failsafe
    * Setup minimum signal level


### v1.4 (2018-04-02)

System:

* Fix edge name in hosts file
* Add RCIO updater module
* Install NetworkManager
* Disable some services:
    * dhcpcd
    * hostapd
    * dnsmasq
* Rewrite interfaces file

Modules:

* rcio-updater v1.0
* rcio-firmware v1.1:
    * Heatbeat support
    * Blinker support
* mavlink-router v1.1.1:
    * Add endpoint for wmd
* acd v1.2.1:
    * Fix heartbeat broadcasting
* Custom pymavlink with WiFi messages support
* wmd v2.0:
    * Support of new developed library to control NetworkManager
    * Possibility to connect as client
    * Module for parsing config file placed in /etc/wmd
    * Separate monitor that only listens to the device states and handles WiFi LED
    * Change LED indication
* csd v1.2:
    * Fix heartbeat broadcasting
    * Store parameters of video stream at Edge
    * Camera hotplug
    * ACK send to GCS


### v1.3 (2017-12-30)

System:

* Set max_usb_current to 1
* Udev rule for USB radio

Modules:

* ardupilot-wrapper v1.2:
    * Add port for USB Radio (ttyUSB.Radio)
    * Change port for external GPS (port B -> port E)

### v1.2 (2017-12-08)

System:

* Persistent storage and limit size for journald
* Remove link of wpa_supplicant from boot directory
* Make boot partition read only
* Change password of AP to `emlidedge`
* New MAVLink routing scheme for modules

Modules:

* Ardupilot:
    * ArduPlane 3.8.2
    * Change storage dir to /edge/ardupilot
    * Enable UAVCAN by default
* mavlink-router v1.1:
    * Route messages by SYS ID
    * Reject message if sender has the same SYS ID as endpoint
* Ardupilot-wrapper v1.1:
    * Fix creating new config file
    * Set MAVLink source component to 1 for SITL
    * Changed directory for logs from /home/pi/logs to /edge/journal for SITL
    * Added wmd service to list of observed systemd units
* acd v1.2:
    * Output version of Edge's firmware to GCS
* wmd v1.1:
    * Set unique SSID for AP
* csd v1.1:
    * SYS ID changed to 1

### v1.1 (2017-11-09)

System:

* Shrink image
* New partition - `/edge`
* Changed motd

Modules:

* Ardupilot
    * ArduCopter 3.5.3

### v1.0

System:

* Support CAN
* Support sensors
* HDMI Input suppport
* Hostname edge
* Driver for 8812au

Modules:

* Selftests
* rcio-firmware v1.0
* rcio-dkms v0.9.1
* Ardupilot:
    * Copter 3.5.2 with Edge support
* Mavlink-router v1.0
* Ardupilot-wrapper v1.0
* Camera-streaming-daemon v1.0
* WiFi-manager-daemon v1.0
* UAVCAN-id-allocator v1.0
* Ardupilot-configurator-daemon v1.0
