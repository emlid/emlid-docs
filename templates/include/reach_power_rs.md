{% if model == "RS/RS+" %} 
Reach RS/RS+ has built-in LiFePO4 battery providing 30 hours of operating time. 
{% else %}
Reach RS2 has built-in LiFePO4 battery providing up to 22 hours of autonomous work when logging data and up to 16 hours as a 3G rover. 
{% endif %}

## Charging over USB

You can power and charge Reach {{ model }} over {{ usb }} cable using power supplies like:

* Power bank
* USB wall adapter

## Powering Reach {{ model }} from the external connector

{% if model == "RS/RS+" %} 
!!! note ""
	Works only for Reach RS+

Reach RS+ can automatically turn on when the power is supplied to the device via an external 9-pin bottom connector with a voltage in the range from 5V to 40V.
{% else %}
Reach RS2 can automatically turn on when the power is supplied to the device via [an external 9-pin bottom connector](../specs/#electrical-specs) with a voltage in the range from 6V to 40V. [You can enable this feature in the ReachView Settings tab.](reachview/settings.md)
{% endif %}

To charge the receiver 5 watts is required. For operating 7,5 watts on average is required (10 watts maximum). 
