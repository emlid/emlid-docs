##Intro

Temperature fluctuations can influence the data that is acquired from sensors on the board. So we use the heating to maintain a stable temperature. It allows to get more accurate data. Using QGC you can not only monitor temperature but also change it.

## Check temperature

You can check temperature of Edge's sensors using QGroundControl's `Status box`.

<div style="text-align: center;"><img src="../../img/qgc/temperature/status-box-without-temperature.png"></div><br>

After starting QGC press <img src="../../img/qgc/temperature/setting-button.png" style="width:30px; vertical-align: middle"> (over `Status box`)  and pick there `temperature (1)`

!!! note
    For better appearance you can pick `Large` 

<div style="text-align: center;"><img src="../../img/qgc/temperature/temperature-widget.png"></div><br>

Now you can monitor temperature of the vehicle's sensors!

!!! note
    If you don't see window with temperature, just click on status box multiple times.

<div style="text-align: center;"><img src="../../img/qgc/temperature/status-box-with-temperature.png"></div><br>

## Change temperature

To change temperature, go to the `Vehicle Setups` menu <img src="../../img/qgc/vehicle_setup_menu.png" style="width:30px; vertical-align: middle">  and choose `Parameters` tab.

<div style="text-align: center;"><img src="../../img/qgc/temperature/parameters.png"></div><br>

Fill the `Search` with "BRD_IMU_TARGTEMP" string and click on the found parameter. You will see `Parameter Editor`.

<div style="text-align: center;"><img src="../../img/qgc/temperature/target-temp-parameter.png"></div><br>

Enter the desired temperature and press `Save`:

!!! attention
    Please don't set the temperature to something that is very different from the environment as we can't heat the sensors endlessly, likewise their temperature can't be lower than environment's. Therefore **min temperature > temperature of environment, max temperature < +80 ºC**.

<div style="text-align: center;"><img src="../../img/qgc/temperature/new-target-temp-parameter.png"></div><br>

After that your board temperature will gradually change. It takes about 1-2 minutes.

!!! attention
    Calibrate your sensors only after temperature stabilizes.

