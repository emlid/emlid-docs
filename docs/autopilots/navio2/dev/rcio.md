### SYSFS

On Navio2 PWM, ADC, SBUS and PPM are integrated in Linux sysfs allowing for easy access from any programming language. 
Sysfs is a virtual file system that exports info about kernel subsystem and hardware devices. 

For instance, sysfs provides easy access to attributes of Navio's PWM (`/sys/class/pwm/pwmchip0/`) or RC input structures (`/sys/kernel/rcio/rcin/`).

### RCIO status

If you face problem with PWM generating or RC input decoding check the status of Navio's onboard RCIO.

To get the status execute this command:
```bash
pi@navio:~ $ cat /sys/kernel/rcio/status/alive
```
RCIO is powered on and detected by Raspberry Pi if the result of above operation is `1`. 

`0` shows that RCIO is not connected. First of all check the hardware connection between Navio2 and Raspberry Pi. 
Navio2 should be fixed using screws as stated in our [hardware setup docs](../../ardupilot/hardware-setup/#attaching-navio2-to-a-raspberry-pi). 
