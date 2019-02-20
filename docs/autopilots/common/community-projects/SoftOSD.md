
### SoftOSD
-------

**Disclaimer**

SoftOSD is a personal project of Emlid community member George Andrikopoulos.

For any support please refer to him in the [project thread](http://community.emlid.com/t/raspberry-pi-osd-using-navio/725/58).

All following text in provided by the project author.

**End of disclaimer**

This is the DOC page of the SoftOSD software which is a software version of the "classic" Hardware OSD (OnScreen Display).

SoftOSD is the result of the NAVIO+ existance which is rich in great possibilities and development opportunities.

This software is a closed software , which means the source code is not available to the public.All the features of the software are given from the either the Raspberry Pi 2 platform of the NAVIO+ framework with great development capabilities.

The software is written in Qt Language with some declarive additions in QML. It is very light in terms of size (~80kb) and uses advanced software techniques in its implementation and function.
It uses 4 major threads that communicates with the NAVIO+:

a. 1 Second Thread.
  This thread is used for the medium priority comms like the battery level and consumption in mAh.
b. 10 Second Thread.
  This thread is used for the lowest priority like the Barometer and Temprature values.
c. 40 mSecond Thread.
  This thread is used for the highest priority sensors and feed like compass and Gyro Values.
d. 5 Second Thread.
  This is a spare thread for future use, like the Audio Modem and others sensors.
Threads are not guaranteed to work in their named Timed events but tests have shown that minor single digit msec offsets have been found in a very stressed cases.

SoftOSD has been debuged fully and found with no memory leaks , not even in its libraries used.This makes it a safe to use software in Raspberry Pi environment. ArduPilot has not been tested with SoftOSD at that time but any conqurent use of those two softwares its is sure that will work.
Offcourse in any case this doesnt mean that I take any responsibility of any damage might occure due to glitch of ArduPilot. SoftOSD does not perform any action in the sensos of NAVIO+ neither alters their nature , which means ...it just reads data.

### Installation
------------
As I have stated above SoftOSD is written in Qt and C++ which makes it a "bit" complex to distribute to others except those who have access to the Development environment. In order for all (users and developers) to be on the same page I have distributed the development image of the SD card of the Raspberry Pi to the community. SoftOSD is developed directly on the Pi (no cross compilers used) and the environment is based on the native NAVIO+ latest image for Raspberry Pi 2.

### Requirements
-------------
1. SD Card for NAVIO size 8GB.
2. Raspberry Pi 2 (1GB Ram)
3. NAVIO+ Autopilot
4. TV/Audio Raspberry cable (https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=83446)

The 4th is very important as cables might seem the same with others but the internal cabling is completely different. So please be very carefull when you buy/construct the cable. If you construct the cable take into consideration that the Audio Cables will be required in the future and it will good to have them constructed now. (Audio Modem etc).

### Instructions

1. Download the image from the link below
<    >

2. Write the image to the SD of your choice (8GB minimum)
3. Install the SD to the Raspberry with NAVIO+ and load the system.
4. Log in and Execute the following commands in the terminal (SSH Putty is fine)
  export QT_QPA_EGLFS_PHYSICAL_WIDTH=720
  export QT_QPA_EGLFS_PHYSICAL_HEIGHT=480
  This will tell the Qt what is the frame buffer size since no /dev/fb0 device exists or the query does not respond.
5. Move to the folder cd /home/pi/SoftOSDv0.57/softOSD
6. Excecute sudo nano /boot/config.txt
   remove comment from #sdtv_mode=2
   This will enable the SDTV OUT (Composite of the Raspberry Pi)
7. Remove any HDMI cable and reboot (sudo reboot)
8. Move to the folder cd /home/pi/SoftOSDv0.57/softOSD
9. Execute  tvservice --sdtvon "PAL 16:9"
    This will turn the TVOUT composite ON if you have HDMI Cable connected the monitor will blank.
---------------------------------------------------------------------------------------------------
All the above steps are preparing the Raspberry Pi for use by softOSD, they do not affect console.
Now we will use a trick to have Camera and Application "overlaid".

10. Execute raspivid -t 0 -fps 25 -op 150 &
    This will execute the video preview of Raspicam and display it on the output of the Raspberry.
    Lets check the options of the command.

    -t 0 -> Tells the programm to run the camera preview indefinetly (usually the preview runs for 5-8 seconds)

    -fps 25 -> Tells the programm to get 25 Frames Per Second from the Camera View.

    -op 150 -> This is the trick. This tells the Camera to have nearly the half opacity over the Frame Buffer.
              Since camera Preview and all other live views of PiCamera superimposes anything that runs currently (it puts everything on the background) I use the opacity trick to display the SoftOSD on the background.

    & -> Tells the program (raspivid) to run as a service in the background. If you want to stop the service simply run sudo pkill raspivid


11. Run ./softOSD
    The programm will run and the system will get the Gyro Cablibrated and calculate offsets.
    You will see on the screen the gimbals rolling arround and stabilized in the current posistion of the NAVIO+.
    This is an effect seen in the real life HUD in the majority of fighter planes...it is not mine ...it is sensor effect.    

### Additional Comments
    -------------------

The image is provided as is and can be used for Qt Development with full multimedia support.
The framework has been build natively (no cross compile) and all the development is perfomed on the platform.
Also the image has all the required applications for ArduPilot and video streaming like gstreamer 1.0 etc.

### V4L2 devices (USB etc)
    ----------------------

The image is V4L2 framework friendly. This means that you can replace the raspivid command with v4l2-ctl alternative with a camera of your choice. As you already know the USB cameras are not fast enough for Pi (USB issues) but the resolution is "low" (720 x480) and will be more close to reality, as the sensors will be much faster than the move. Minor issue as the sensor data/move and the video are "synced" in the Pi and they come to their own reality in the Trasmited Destination.

### GSTREAMER
    ---------

gStreamer can be used as it was used using the commands you used to like "raspivid -t 0 -h 720 -w 1080 -fps 25 -hf -b 2000000 -o - | gst-launch-1.0 -v fdsrc ! h264parse !  rtph264pay config-interval=1 pt=96 ! gdppay ! tcpserversink host=YOUR_RPI_IP_ADDRESS port=5000"
    interupt between the | and the raspivid command the ./softOSD.

This will stream the whole frame buffer including the SoftOSD to the pipeline for stream.
I havent tested it but I am pretty sure that it will work. If not there is always time to find a solution.
Dont forget to change the resolution of the raspivid to -h 480 -w 720 else the SoftOSD will be a mess. It does not Scale to fit...yet
