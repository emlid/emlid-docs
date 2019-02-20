#Windows IoT

----------

**Disclaimer**

The Windows IoT SDK is a personal project of Emlid community member [Tony Wall](http://community.emlid.com/users/codechief).

For any support please refer to him in the [project thread](http://community.emlid.com/t/windows-10-iot-image-for-navio/381/last).

All following text is provided by the project author.

**End of disclaimer**

----------

## Project

In 2015 Microsoft announced official support for the Raspberry Pi 2 running Windows 10 on their new "IoT" (Internet of Things) platform. Soon after work started on an open source SDK for Navio with the following goals:

 - Enable access to all the great sensors of the Navio HAT for Windows DIY projects.
 - Prove the concept of an autopilot running a Windows OS (quadcopter in stabilized flight mode).
 - Provide the tools necessary for the community to extend existing autopilots to Windows and/or create an entirely new system.

This document describes how to develop your own code for Navio running on Windows 10 IoT, or just try-out the test and sample apps for yourself. You can follow the progress at the [Emlid forum thread](http://community.emlid.com/t/windows-10-iot-image-for-navio/381/last) or the [Hackster.io project](https://www.hackster.io/team-code-for-robots/navio-sdk-for-windows-iot). If you like it please "respect" the Hackster project to return some kudos to the creator ;-)


## Getting Started

This section describes how to start development by installing Windows IoT on your device, Visual Studio on your PC, then finally how to clone, build and run the code.


### Tools

Links to download the development tools and basic instructions what to install are provided by Microsoft here:

[Getting Started with Windows IoT](http://ms-iot.github.io/content/en-US/GetStarted.htm)

The "IoT Dashboard" tool eases the process of downloading the OS image to the Raspberry Pi 2, then helps you connect and configure devices over the network. End-users need only install the dashboard, or you could provide them with a preloaded SD card.

Alternatively you can download the ISO image and release notes here:

[Other Downloads](http://ms-iot.github.io/content/en-US/Downloads.htm)

Since device driver source code has been added to the solution, you will also need to install the latest Windows Driver Kit (WDK) available in the "Install WDK 10" link on this page:

[Driver Kit Downloads](https://msdn.microsoft.com/en-US/windows/hardware/dn913721%28v=vs.8.5%29.aspx?f=255&MSPPError=-2147217396)


## Development

The current Navio SDK "framework" is a Windows Universal library, so can be consumed by any Windows Universal application written in any .NET language supported by IoT. Simply use the NuGet Package Manager of Visual Studio to add the [Emlid.WindowsIot.Hardware](https://www.nuget.org/packages/Emlid.WindowsIoT.Hardware) package, then write some code with the various Navio*Device classes to utilize the hardware.

Deployment is easy with the Visual Studio produced Windows Universal packages. They are precompiled and load directly onto the IoT device. You can deploy them via Visual Studio during development, via the web interface for end users, script them with PowerShell or include them on a preloaded SD card image.


### Preparation

It is strongly recommended you complete some basic training before attempting to build and deploy your first IoT project. Even experienced Windows developers will have to get to grips with some of the special build and deployment requirements for the ARM processor and remote IoT device connections. Also the IoT system is still under early development, even though the desktop Windows 10 builds are finished.

 1. Follow instructions to build, deploy and debug Microsoft's [IoT "Hello World" sample](http://ms-iot.github.io/content/en-US/win10/samples/HelloWorld.htm).
 2. In Visual Studio open the "Tools - Extensions and Updates..." dialog.
 3. Select the "Updates" tab then update the GitHub extension and "Windows IoT Core Project Templates".
 4. Optionally update all others items (multiple starts will be necessary).
Update the GitHub extension (menu "Tools - Extensions and Updates...").
 5. Select the "Online" tab, search for then install the "Productivity Power Tools 2015" extension.


### Building the SDK from Source

1. Click "Team Explorer" then the "Plug" icon (manage connections).
2. Under "Local Git Repositories" click the "Clone" link then enter the URL of the GitHub project "[https://github.com/emlid/Navio-SDK-Windows-IoT](https://github.com/emlid/Navio-SDK-Windows-IoT)", choose a local path into which the files will be downloaded then the "Clone" button.
3. Open the solution by selecting the "File - Open - Project/Solution..." menu option then the solution (.sln) file from the local repository directory you just cloned.
4. In the Solution Explorer window, right-click the solution root then select "Power Commands - Open Command Prompt" and enter the commands:
  ```
  cd Tools\Scripts
  PowerShell.exe -File "Setup Local.ps1"
  exit
  ```
5. On the build toolbar, ensure that "Debug" configuration and "ARM" platform is selected.
6. In the "Build" menu select "Rebuild Solution". 
7. Some NuGet packages may be loaded, then the build will start and should complete without any errors.


### Build and Run the Hardware Test App

The Hardware Test app is currently only distributed as source. Later it will also be available for stand-alone use (without any development tools).

1. Ensure the Remote Debugging Tools are running on the IoT device. Use the web interface (easily accessible via the dashboard tool) "Debugging" page to start it and also check the remote name and port, which must match in your deployment configuration.
2. On the build toolbar, ensure the "ARM" processor is selected and the "Navio Hardware Test" startup project.
3. Click the drop-down arrow next to the green "play" icon, then "Remote Machine".
4. If this is the first time you deployed to a remote machine the configuration dialog will appear, then you should enter the "name:port" of the target device and choose no authentication.
5. With the remote machine still selected, click the "Play" icon to build, deploy and run the sample.
6. The solution should compile, deploy and run on the Navio/RasPi. Use the mouse to select "LED & PWM" (the rest is not implemented yet). Check the frequency, set some sliders (best PWM near bottom) then click the Output ON.
7. Play with the sliders to test your LED and servos/ESCs.
8. Monitor the output window for any messages, and look at the physical device for any feedback, e.g. LED colours or servo movement.
9. Click "Close" then "Exit" to finish.


### Build and Run the Samples

Currently the sample applications are "Background Application" projects, which means they run directly from Visual Studio with no UI. All output is sent back via debug messages to the Visual Studio "Output" window.

1. Ensure the Remote Debugging Tools are running on the IoT device. Use the web interface (easily accessible via the dashboard tool) "Debugging" page to start it and also check the remote name and port, which must match in your deployment configuration.
2. On the build toolbar, ensure the "ARM" processor is selected and the "Navio Hardware Test" startup project.
3. Click the drop-down arrow next to the green "play" icon, then "Remote Machine".
4. If this is the first time you deployed to a remote machine the configuration dialog will appear, then you should enter the "name:port" of the target device and choose no authentication.
5. With the remote machine still selected, click the "Play" icon to build, deploy and run the sample.

Monitor the output window for any messages, and look at the physical device for any feedback, e.g. LED colours or servo movement.


## Known Issues

1. Since Update 1 and IoT build 10586 it is necessary to manually start the remote debugging tools via the web interface before deployment will be successful. Also the remote machine name must be edited to include the port of the remote debugger, which appears in the confirmation dialog when starting them via the web interface, e.g. MyDeviceName:8116.
2. RC Input is super slow because we are in the middle of conversion to C++ and drivers. Software decoding is too slow and unreliable in user mode on the Raspberry Pi, so it is delayed until after all the other components are implemented. Navio2 may be supported first because it has decoding hardware.


## Roadmap

The current framework release is known as the "user mode" framework. Later it will be converted into a Windows Runtime Component so it it can be consumed by other languages than .NET, such as native C++ and NodeJS. The development language will also switch to lower-level C++ runtime components which will work in tandem with new Navio specific device drivers for performance and reliability. Once device drivers are available, a custom IoT image will also be produced to ease installation. OEM build instructions will also be included so you can integrate the individual drivers into your own IoT image.

The framework will remain, but the Navio*Device classes will be redirected to call the new lower level components. However it is inevitable that some breaking changes will occur. At least the user mode framework will continue to run on standard IoT images (without drivers installed) so you have to possibility to stay with the older NuGet package versions and upgrade when it suits you.

It remains to be seen what Microsoft will provide for provisioning and deployment of end user applications, and if there will be any other editions than "core". There could even be Windows Store support, some other kind of one-click installation. We can already provide manual download links to "side-load" standard packages onto the device via the web interface. The goal is to achieve "plug and play" installation and configuration of Navio and Navio enabled apps running Windows IoT.


### Milestone 1: "Core SDK"

Mission statement: "Full hardware support for Navio on Windows IoT."

1. LED & PWM (PCA9685) device, sample and test app (100% complete).
2. RC Input (PPM over GPIO) device, sample and test app (60% complete).
3. IMU (MPU9250) device, sample and test app.
4. Barometer (MS5611) device, sample and test app (100% complete).
5. GPS (U-Blox NEO-MN8, possibly NEO7M, NEO-6T too) device, sample and test app.
6. ADC (ADS1115) device, sample and test app.
7. FRAM (MB85RC04) device, sample and test app (100% complete).
 

### Milestone 2: "Windows Drone PoC"

Mission statement: "Answer the question; can you really fly a drone with Windows IoT?"

1. Motor control and PID logic for a quadcopter.
2. FMU test app, enable raw flight with RC input in stabilize mode.
3. Manual (acrobatic) mode and switch capability.
3. RTL failsafe mode and switch.
4. GPS fence failsafe with auto-correction.
5. MAVLink proxy, including Ground Control Station support.


### Future Milestones:

Mission statement: "Expand support and add new devices."

1. Support other multi-rotor types in the PoC application.
2. FrSky telemetry.
3. FrSky SPort (sensors) device(s) and test app(s).
4. U-Center GPS proxy for easy configuration / upgrade of GPS.
5. RTKLib integration for highly accurate GPS.
6. Emlid REACH integration, similar to Windows Remote Arduino or as close to full IoT Intel Galileo (Intel Edison) support as possible (depends on how good Microsoft's support is in this area).
7. Expand the Windows drone sample, possibly spinning-off a new autopilot (includes support for other vehicle types, e.g. planes and rovers).
8. Experiment with Windows HAL for ArduPilot (requires a good Linux code bridge like Cygwin, but for IoT).
9. Expand samples for other (than drone) projects, e.g. general robotics, trackers and DIY solutions.


## Change Log

*2016.01.02* v1.0.7

1. FRAM memory device implemented, both the MB85RC256V of Navio+ and MB85RC04V of Navio.
2. General test app GUI display, usability and multi-threading improvements.

Continued development of the core SDK. FRAM complete and fully tested on Navio+ device. Support for the original Navio's FRAM chip had been coded but has not been fully tested.


*2015.12.28* v1.0.6

1. Barometer (pressure and temperature sensor) implemented.
2. LED cycle feature added to LED & PWM test app.

Continued development of the existing C# sensor library. Note the barometer temperature is always about hotter that then environment because of heating by surrounding components, e.g. the Raspberry Pi processor is sitting underneath it. For that reason you will also see the temperature rise in the hardware test app, because the processor is being taxed with the GUI functionality.


*2015.12.22* v1.0.5
 
1. Device driver "capability" proof of concept. Working skeleton RC input kernel mode WDF driver which successfully deploys and can be communicated with from a user mode Universal application.
2. Various patches and documentation updates to existing source code and samples.
3. Updated solution to work with latest IoT December 2015 OS build 10586, SDK/WDK 1511, Visual Studio 2015 Update 1.
 
This is an interim check-in which does not add any end-user (consumer developer) functionality, but solves the technical requirement to be able to write a kernel mode driver and communicate from user mode.
Because of the difficulties with the VS2015 tools and lack of improvement in update 1 (which actually got worse in some aspects) focus will temporarily shift back to the user mode framework for all other features than RC Input.
Also with the release of Navio 2 which has RC Input hardware, the device driver can wait a little while, so we can first gain the full chipset functionality in user mode and maybe see if a simple quadcopter can hover with it (and a joystick instead of RC input).
Commitment is still there to produce high performance (real-time) and robust drivers shortly after a successful user mode PoC.


*2015.10.06* v1.0.4

1. RC input C# proof of concept complete (so far as worthwhile). Only accurate to ~1 second due to "floating GPIO" limitation (see notes below). 
2. Completed RC Input in hardware test app and added new RC Input C# sample.
3. Added NuGet package. No need to download source and compile to use the hardware from now on! The package URL is: https://www.nuget.org/packages/Emlid.WindowsIot.Hardware

Due to a Microsoft IoT image limitation, specifically with the GPIO #4 pin hard-wired to RC Input on the Navio, we cannot achieve any kind of acceptable performance in "user mode" code.
Furthermore, the current UWP API has a lack of support for time critical threads in "user mode". It is necessary to bring forwards the conversion to C++ and device drivers.
The next release will include only drivers and provide access via a C++/CX coded Windows Runtime Component. C# code and any other language can then be used as normal for user applications.


*2015.08.25*

1. RC input progress. Test app enables use of RC Input, but no GUI interaction yet. For now use the Output window of Visual Studio to see debug messages reporting decoded PPM values. They appear to be correct, but some tuning of rounding and frame error detection is required.


*2015.08.14*

1. RC Input hardware classes done in their first untested form.
2. RC Input model and preliminary view added to hardware test app, but not enabled yet.
3. Minor clean-up and coding standards in other classes and projects.


*2015.07.31*

1. Updated solution to Visual Studio 2015 RTM.
2. Hardware Test App - Fixed theme/resource errors and applied "Emlid green" instead of default "IoT pink".
3. SetLED - Fixed error in buffer write routine.
