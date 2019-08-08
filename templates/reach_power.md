{% if model != "RTK" and model != "M+" %}
{% include "include/reach_power_rs.md" %}
{% else %}
{% if model == "RTK" %}
!!! tip ""
	Reach has been replaced with [Reach M+](https://emlid.com/reach). Documentation for Reach M+ can be found [here](https://docs.emlid.com/reachm-plus/).
{% endif %}

## How to power Reach {{ model }}

Emlid Reach {{ model }} module can be powered using **Micro-USB** port or **{{ power_port }}** ports. Power circuit is shared for all ports, so when you power the device over one port it will pass power to other ports.

!!! danger "Attention"
    Do not plug two power supplies at the same time as it may damage the device.

{% if model == "RTK" %}
<div style="text-align: center;"><img src="../img/reach/power-supply/wrong-power-supply.png" style="width: 550px;"></div><br>
{% else %}
<div style="text-align: center;"><img src="../img/reachm-plus/power-supply/wrong-power-supply.png" style="width: 550px;"></div><br>
{% endif %}

### Power supply over USB

{% if model == "RTK" %}
<div style="text-align: center;"><img src="../img/reach/power-supply/usb-power-supply.png" style="width: 550px;"></div><br>
{% else %}
<div style="text-align: center;"><img src="../img/reachm-plus/power-supply/usb-power-supply.png" style="width: 550px;"></div><br>
{% endif %}

You can power Reach over Micro-USB cable using power supplies like:

* Power bank
* USB wall adapter
* Computer USB ports

{% if model == "RTK" %}
<div style="text-align: center;"><img src="../img/reach/power-supply/power-supply-options.png" style="width: 550px;"></div><br>
{% else %}
<div style="text-align: center;"><img src="../img/reachm-plus/power-supply/power-supply-options.png" style="width: 550px;"></div><br>
{% endif %}

### Powering using {{ power_port }} ports

Reach can be powered by providing 5 Volts to corresponding pins on any of the two {{ power_port }} ports.

{% if model == "RTK" %}
<div style="text-align: center;"><img src="../img/reach/power-supply/df13-power-supply.png" style="width: 550px;"></div><br>
{% else %}
<div style="text-align: center;"><img src="../img/reachm-plus/power-supply/jst-gh-power-supply.png" style="width: 550px;"></div><br>
{% endif %}

When Reach is powered over {{ power_port }} port it will pass power to devices connected to Micro-USB OTG port such as flash drives, 3G\4G modems, USB radios etc.

{% if model == "RTK" %}
<div style="text-align: center;"><img src="../img/reach/power-supply/accessory-power-supply.png" style="width: 550px;"></div><br>
{% endif %}
{% endif %}
