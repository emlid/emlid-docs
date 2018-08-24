<p style="text-align:center" ><img src="../img/reachview/settings/settings.png" style="width: 800px;" /></p>

### Check app version  
Every time you power up Reach in a Wi-Fi network it will check for new ReachView update and notify you accordingly.

!!! note
    Update check is only done one time during boot process. If you want to force new version check please proceed to ReachView Updater. It is available on port 5000, for example `http://reach.local:5000`. It will automatically scan Emlid update servers when you open it. Learn more about ReachView updater [here](updater).

### Night mode 
Night mode allows you to turn off the LEDs until the next reboot of the device. 

### System report
The tool is used to facilitate issues reports. There are two kinds: one in plain text, and one as a zip archive. The former is for the forum, and makes it easy to share settings, network state and app version. The latter is for harder cases and contains system logs and technical details of your device.

!!! note "Getting system report"
	<p style="text-align:center"><img src="../img/reachview/settings/system-report.gif" style="width: 800px;" /></p>

### Change Reach name  
Reach name can be changed in order to distinguish between multiple devices. A very common pattern is to name devices according to their base or rover function. Device name is the base for hotspot name and local network name. The default name is “reach”, changing it will also affect local name `http://reach.local` and hotspot name `reach:xx:xx`.

### Reset settings to default  
Click “Reset setting to default” button to return all settings to factory configuration. Only logs and wireless settings are preserved. If you would like to perform a complete factory reset and wipe all your data you can [reflash firmware image](firmware-reflashing).

### Change hotspot password
Default hotspot password is “emlidreach”, you can change it for security reasons. If you forget your new hotspot password you can still access Reach by bringing it to a known Wi-Fi network. If you lost access to Reach you can [reflash firmware image](firmware-reflashing) and set it up again.

### Logging settings
Specify how ReachView will handle full memory behavior here, it can either stop logging or override old logs in favour of new ones. In most cases “rolling logs” is recommended.

### Log split period
New log file will be created every N hours, while preserving previous log as well. This setting allows you to control the size of the files that you work with.



