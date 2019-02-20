
## Overview
Open QGroundControl, go to ``Setup`` menu and select ``WiFi`` tab. You will see the window.

<div style="text-align: center;"><img src="../../img/qgc/wifi/main-page.png"></div><br>

* ``Box 1`` displays current WiFi status:
    * *Access point mode* (Default state) - Edge works as hotspot and share WiFi signal with other clients.
    * *Client mode* - Edge is connected to selected WiFi network.

!!! Note
	You also can check status of WiFi in a ``Summary`` tab.


* ``Box 2`` displays list of saved networks (stored on Edge).
You can add/delete and connect to a network. If some network is set by default, you can switch
between WiFi modes by clicking on *switch* button in Box 1.

## Switch to client mode and back

Click on ``Add`` button. You will see the dialog with WiFi preferences. Enter 
SSID, security type and password, if need.

<div style="text-align: center;"><img src="../../img/qgc/wifi/add-wifi-dialog.png"></div><br>

Press on ``Ok`` and network will be saved to an Edge. Next, select
network from the networks list and set one by default (``Set by default`` button).

<div style="text-align: center;"><img src="../../img/qgc/wifi/list-with-one-default-network.png"></div><br>

Well, switch to ``Client`` mode by push on *switch* button in the ``Box 1``.
You will see *Switching...* message and Edge will be disconnected. 

<div style="text-align: center;"><img src="../../img/qgc/wifi/switching.png"></div><br>
!!! Note
    If Edge WiFi LED has
    a green color - everything is well, otherwise this means that you made a mistake in SSID or password
    of WiFi network. (More about [WiFi LEDs](../led-status.md))
!!! tip 
    ``Switch`` button colors are the same as colors on Edge WiFi indicator.
	Green for Client mode and Blue for Access Point.

Connect your computer to WiFi network (to which an Edge is connected).
Go to ``General Settings`` and choose ``Comm Links``. Disconnect from previously created comm link  
(see [Configuring QGroundControl for Edge](../quickstart.md#qgcconf)). Add new IP of Edge by type ``edge.local``.

<div style="text-align: center;"><img src="../../img/qgc/wifi/comm-links-settings.png"></div><br>
!!! attention
    On Windows for getting IP address via ``edge.local`` you should download and install [Bonjour](https://support.apple.com/kb/dl999?locale=en_US).

Save all and push on ``Connect``. Return back to ``Setup`` menu. If everything is done well, QGC will connect to an
Edge via WiFi.

<div style="text-align: center;"><img src="../../img/qgc/wifi/client-mode.png"></div><br>

You can easily return to ``Access Point`` mode by click on *switch* button and reconnect your computer to Edge hotspot.

## Hotspot settings

To change the Tx Power, open `Hotspot settings`, and enter preferred value.
<div style="text-align: center;"><img src="../../img/qgc/wifi/hotspot-settings.png"></div><br>

To change hotspot SSID or/and password, click on `Open dialog` button. If you don't want to change password/SSID, leave the field empty.
<div style="text-align: center;"><img src="../../img/qgc/wifi/hotspot-conf-dialog.png"></div><br>