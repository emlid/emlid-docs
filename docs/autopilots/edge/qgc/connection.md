To set up connection select QGC settings on the top window <span style="text-align: center;"><img src="../../img/quickstart/qgc_settings_button.png" style="width: 30px; vertical-align:middle"></span> from the main menu.

<div style="text-align: center;"><img src="../../img/quickstart/qgc_main_window_settings_selected.png"></div><br>

In the opened settings tab click on `Comm Link` tab.

<div style="text-align: center;"><img src="../../img/quickstart/qgc_comm_links_selected.png"></div><br>

The appeared menu allows you to manually create communication links and connect to them. Click `Add` to create new connection to Edge. After that you’ll see a tab with link settings.

<div style="text-align: center;"><img src="../../img/qgc/create_new_link.png"></div><br>

You can create one of the following connections:

* Serial
* UDP
* TCP
* Log Reply

By default use UDP connection for Edge

* Select UDP as a connection type
* Give a name to this connection and make it automatically connect on start
* Add a target host
    * Click `Add` and type in the IP of Edge (192.168.0.1) or just Edge’s hostname (edge)
    * Press Enter
    * Leave the default port (14550) as is
    * Click `OK` button

For Serial connection you will need to specify Baud Rate.

After these steps you’ll see the new link added with the name you specified

* Now you can connect to Edge, press `Connect` for the created link

<div style="text-align: center;"><img src="../../img/quickstart/qgc_comm_links_connect_selected.png"></div><br>

* QGC will connect to Edge and will start receiving its parameters
