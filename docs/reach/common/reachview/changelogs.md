## Reach Panel changelog

### v2.24.0
([release](https://community.emlid.com/t/reachview-v2-24-0-with-reachview-3-beta-support-is-out/22050))

##### Features

* Allow using special characters like “/” in the NTRIP credentials
* Recovery for surveying projects
* Shutdown on the bottom connector on RS+
* Access the receiver from public IP for RS2
* Shutdown indication when in night mode
* Restart RTK engine if the correction input was updated (available on all L1 devices)

##### Bug fixes

* Fix the issue when the position might get lost when the mobile data is lost
* Now it is allowed setting up the output rate to 0.1 Hz only for 1006 RTCM3 message
* Eliminated some rare hotspot drops when a SIM card is inserted
* Get sound notifications on volume change back
* Fix ‘Send NMEA’ checkbox glitch
* Fix some Bluetooth related issues on device loading
* Fix hiding manual mode when the base coordinates are received
* Fix selected logs removal when leaving the Logging tab
* Fix incorrectly processed antenna height from some NTRIP providers
* Fix status tab units formatting
* Fix LoRa constraints for Thailand and Indonesia
* Fix misbehavior with the toggle on the Bluetooth tab
* Fix caching survey projects and logs with the same name
* Fix the “unsaved” label on the RTK Settings tab

### v2.22.7
([release](https://community.emlid.com/t/reachview-v2-22-is-out-for-all-reach-devices/17834))

##### Features

* Recovering data stream after an Internet connection drops
* "Raw data debug" to facilitate debugging
* Mobile data usage statistics
* ZDA NMEA message
* Disable the power button blinking on stakeout
* Faster NTRIP tab loading
* Subtract antenna height during point averaging
* RMS values for Reach RS2
* Accuracy is added to the Status tab for Reach RS2
* "Loading" state when initializing the SIM-card for Reach RS2

##### Bug fixes

* Hotspot Wi-Fi connection drop
* Fix VRS for some NTRIPs
* Manual base position is now applied correctly
* Full System Report can now be downloaded with SIM card inserted on Reach RS2
* LEDs charge estimation works as expected
* Stop transmitting data when Base Mode is disabled
* 0% hangs in processing of RINEX
* The Cancel button in the Survey tab now works correctly on iOS
* Fix missing epochs in raw data logs and bug with some L2 carrier dropped during conversion to RINEX
* NTRIP URL is now case-independent
* Incorrect RINEX log size representation
* NMEA GGA messages now show correct heights
* Disability to switch from GLONASS to BeiDou in the original Reach, Reach RS and Reach M+/RS+
* Fix processing corrections when all RTCM3 messages are selected in the Base mode tab, but the satellite system isn’t selected in the RTK settings
* Fix the version badge
* Fix a bug with the 1000 AR ratio value
* Entering the fractional antenna height in the Base mode tab in manual mode now works correctly
* LoRa frequency constraints for Australia are updated
* Correction input/position output stream status is now correct
* Fix RTK status freezes after USB-to-PC setup
* Fix issue causing sudden shutdowns on some Reach RS+ and Reach RS2 units
* Fix potential missing timemarks on Reach M+
* Fix possible errors in the RINEX L2 conversions on Reach M2
* Fix incorrect checksum for NMEA GPGSV, GLGSV, GAGSV, and GBGSV messages
* Fix vague toggle behavior on the Logging tab
* Fix SNR status view for base satellites
* Sort satellites in RINEX log
* Fix RTCM3 to RINEX conversions for L2 frequency (GPS, GLONASS)
* Fix some issues with extra time marks on Reach M2
* Fix sudden shutdowns appearing on some of RS2
* Enable shutdown indication in night mode on RS2
* Fix some cases of Test 2 failures on Reach RS2 and Reach Module 
* Blink LEDs for two seconds in night mode after a short button tap on Reach RS2
* Fix the situation when RS2 can’t turn on after storage in the cold until plugged into the charger
* Fix the issue when the position might get lost when the mobile data is lost
* Fix a rare situation when RS+ can get stuck on loading and blinks green LED longer than anticipated
* Address an issue that led to an erroneous green LED blinking pattern on RS+
* Miscellaneous UI improvements

### v2.20.8 Reach RS2 update
([release](https://community.emlid.com/t/rs2-reachview-v2-20-8/15641))

##### Features

* Auto-shutdown on bottom connector unplugging 
* Mobile data usage statistics
* Loading performance of ReachView is improved
* GST NMEA message

##### Bug fixes

* DOP formatting in point collector
* The Import button on the Survey’s map now works as expected
* Fix a bug with clicking on the Bluetooth tab
* Fix Bluetooth tab accessibility in portrait mode
* RINEX file recorded on board of Reach now contains all observations
* Baseline length is no longer displayed after NTRIP connection drops
* Fix stakeout misbehaviour
* Disclaimer about further upgrades for original Reach and Reach RS is added
* GGA message in NMEA output now shows the correct number of satellites

### v2.18.0
([release](https://community.emlid.com/t/reachview-v2-18-1/14591))

##### Bug fixes

* "LoRa is not connected" message popping up on some RS and RS+ receivers
* Android scanner app is now able to download logs, projects or project templates
* iOS scanner app now supports iPhone X series
* LoRa radio now supports complex constraints with several ranges
* Fix a bug with project list's dropdown menus geting stuck in some cases
* Wi-Fi now can see channels 12-14
* Fix jumping correction input tab  
* Pop-up menus behavior is more consistent
* RTCM transmission via Bluetooth is now more stable
* Bluetooth name change now applies immediately, not after reboot
* Red Power LED now works correctly on RS+

### v2.16.0
([release](https://community.emlid.com/t/reachview-v2-16-0-point-stakeout/11894))

##### Features

* Point stakeout
* Smart antenna/pole height - don't think about the actual antenna height anymore.
* Geodata import in CSV, GeoJSON, DXF
* LoRa support for Reach M+
* Automatic boot using the bottom connector on Reach RS+

##### Bug fixes

* Bluetooth connection unstable for some Android and Windows devices
* Onboard RINEX logs had some observations missing (compared to manually converted raw logs)
* Default trail length reduced on the status tab to avoid performance issues
* Prevent user from opening the projects twice


### v2.14.0
([release](https://community.emlid.com/t/reachview-v2-14/10729))

##### Features

* GLONASS inter frequency biases correction. The general recommendation - always have GLONASS AR set to on.
* Improved Beidou processing significantly
* New reworked survey project view
* Fast and pretty Wi-Fi settings tab

##### Bug fixes

* Reach will now restart the processing if base position changes during processing
* NMEA feedback to NTRIP casters will contain a real solution status, not just single
* You are not required to punch in any info when creating a new project, you can just click next
* Reworked disconnect dialog
* Reach will now not reconnect to a different device and will ask you to refresh the page
* ERB fixed to include DOPs and number of satellites while the solution is single
* Fully charged battery state indicator bug


### v2.11.0
([release](https://community.emlid.com/t/reachview-v2-11-0-our-second-stable-release/9473))

##### Features

* Additional correction and GNSS predictor are deprecated
* Second position output is back
* New project export formats: CSV and DroneDeploy CSV
* Surveying: point collection start and end times are saved into the project
* LED: blink green to indicate app loading during startup
* Shutdown and reboot buttons are added in ReachView
* New logos are added

##### Bug fixes

* Fix Wi-Fi not always connecting to known networks on startup
* Corrected position RMS values
* Twitchy on/off switch in base mode


### v2.10.2 dev update
([release](https://community.emlid.com/t/reachview-v2-10-2-dev-update-csv-export/8374))

##### Features

* CSV export. All projects now have a new export option - CSV
* The points now have collection time start and end stamps
* Shutdown & Reboot buttons added

##### Bug fixes

* WLAN connection problem on startup
* Blink the green LED until the app has started, then go solid
* Fix Reach RS app header on devices with small screen
* Some logs disappear from the system
* NMEA format heavily improved


### v2.10.0
([release](https://community.emlid.com/t/reachview-v2-10-0-dev-updates/8322))

##### Features

* Ability to switch between stable and dev updates
* “System reports” to facilitate describing issues
* Peru users will now have their LoRa frequency bands automatically limited to a 915100 - 927900 kHz range

##### Bug fixes

* After losing network connection in client mode, Reach will no longer be “stuck” connected to nothing, but will be actively reconnecting to the missing network
* Support for GLONASS MSM 1084, which does not contain the satellites’ frequencies
* No longer write L2 flags to the Reach-generated RINEX file header
* Changing device name does not produce a reaction in the app
* Fix DNS not working with certain types of USB modems
* Another fix for working with QZSS corrections
* The “@” symbol breaks NTRIP configuration screen, if used in username or password. The “:” and “/” symbols are still forbidden!


### v2.9.0
([release](https://community.emlid.com/t/reachview-v2-9-2-rtk-performance-boost/7443))

##### Features

* Phase-bias is reset on large residuals, making going back to fixed mode much easier, eliminating solution drifting off
* We can now use observations from different epochs, increasing solution reliability in case of correction link data loss

##### Bug fixes

* Sometimes downloading logs failed until you perform a refresh
* Point view inside survey projects would not show big heights
* Reconnecting USB on Reach RS stops the data until new settings are applied


### v2.8.0
([release](https://community.emlid.com/t/reachview-v2-8-0-native-android-app-ios-coming-soon/7253))

##### Features

* Add a service to advertise the receivers, so that they are recognizable by the native app

##### Bug fixes

* Surveying projects data isn’t synced to disk, which sometimes results in data loss
* Antenna height resolution in point collection is limited to two decimals instead of three


### v2.7.0
([release](https://community.emlid.com/t/reachview-v2-7-0-extended-led-support/6743))

##### Features

* Extended LED support. Reach LED will reflect network connection status, point collection and app state. In addition, Reach RS's PWR LED will show battery and power status
* Added a special button to blink the LEDs manually. Should help you locate which Reach you are currently working with, if you have many
* Added "Night mode". Allows you to turn off the LEDs until the next reboot

##### Bug fixes

* Network scan might hang indefinitely on boot with fast blinking
* Removed malfunctioning instantaneous option from GPS AR modes

### v2.6.0
([release](https://community.emlid.com/t/reachview-v2-6-0-rinex-logging/6487))

##### Features

* RINEX logs. Now you can skip the RTKCONV part in your post-processing routine. The RINEX converter has been updated and handles Galileo observations as well. Logging to RINEX is optional, you can choose raw data format just like you do with position log. After the log is finished, you get a nice compressed zip archive.
* New NMEA messages - GST and VTG. They contain velocity and accuracy information and should improve experience using Reach with external point collection software.

##### Bug fixes

* Fixed the antenna height field, which forced iOS users to use a numeric keyboard with no float point
* Some really big heights might not have been displayed correctly in the surveying screen
* Added units in the battery view on Reach RS
* Fixed SNR chart's weird "paint drip" animation glitch
* Fixed SNR mask configuration sometimes inactive
* Fixed camera trigger failing in the recent versions
* Improved GNSS predictor's time step

### v2.5.0

##### Features

* Added bluetooth as an IO option to correction input and correction output

### v2.4.0
([release](https://community.emlid.com/t/reachview-v2-4-0-galileo-support/5887/7))

##### Features

* Galileo support

##### Bug fixes

* Fixed a bug, which interfered with turning Glonass on or off
* Changed a notification message for Reach RS on low sat levels


### v2.3.1
([release](https://community.emlid.com/t/reachview-v2-3-1-point-collection/5855/8))

##### Bug fixes

* Fixed an issue with cache, which prevented the new Survey tab from opening immediately after the update


### v2.3.0
([release](https://community.emlid.com/t/reachview-v2-3-0-point-collection/5855/16))

##### Features

* Point collection support
* Collection screen with a realtime progress indicator, RTK and averaging statuses
* Collect the points either manually or with project-wide auto-save rules
* Project view with a map and summary point list
* Export your data to DXF, GeoJSON, Esri shapefiles


### v2.2.7
([release](https://community.emlid.com/t/reachview-v2-2-7/5523))

##### Features

* 3G/LTE USB modem support

##### Bug fixes

* Fixed an app crash, which happened if you turn off the base output configured to use LoRa
* Reworked USB-OTG on Reach RS. It didn't function properly on the pre-production units, but now those days are in the past


### v2.2.5 beta
([release](https://community.emlid.com/t/reachview-beta-v2-2-5/4988))

##### Bug fixes

* NTRIP issues fix
* Patch ERB to include correct geoid and ellipsoid heights


### v2.2.4 beta
([release](https://community.emlid.com/t/reachview-beta-v2-2-5/4988))

##### Features

* Update notifications


### v2.2.3 beta
([release](https://community.emlid.com/t/reachview-beta-v2-2-5/4988))

##### Bug fixes

* Fix bug of Reach crashing after a short period of work time


### v2.2.2 beta
([release](https://community.emlid.com/t/reachview-beta-v2-2-5/4988))

##### Bug fixes

* Fixed RTKLIB memory leak
* LoRa driver has got a heavy update
* Logs got a slight looks update and the whole tab will behave in a more stable fashion
* Fixed small frontend issues, like the LLH/XYZ selector placed poorly


### v2.2.1 beta
([release](https://community.emlid.com/t/reachview-beta-v2-2-5/4988))

##### Bug fixes

* The logs will not act insane when opening the logs tab
* Solution will not get lost
* The solution log will not restart for no apparent reason
* Solution format selector works as it is supposed to
* Merged RTCM3 fix by RtklibExplorer

### v2.2 beta
([release](https://community.emlid.com/t/reachview-beta-v2-2-5/4988))

##### Bug fixes
* Fixed wrong log split time
* Caching issues. While this is not a complete fix yet, this seriously improves the overall experience
* App prevented from crashing due to empty configuration files
* Increased timestamp precision in the solution output
* Solution log format mixup resolved
* Base coordinate reaveraging button is fixed

##### Features

* Reach RS support


### v2.1.6 beta
([release](https://community.emlid.com/t/reachview-beta-v2-1-6-is-out/4664))

##### Bug fixes
* Added units for the max acceleration settings
* Logging page reapplies logging settings


##### Features

* Added a special camera tab. Shows the time of the last received time mark and allows to setup Reach to trigger the camera automatically
* Added a button to delete logs from a whole day
* Automatically retrieve mountpoints available on an NTRIP service
* The solution log now has a selector, which lets you choose log format


### v2.1.5 beta

* Fix the bug with logs not saving their state after reboot

### v2.1.4 beta
([release](https://community.emlid.com/t/reachview-beta-v2-1-5-update/4544))

##### Bug fixes
* In-app connect to open wi-fi validation fails
* Loading screen disappears too early
* Logging: delete is glitchy with multiple files
* Satellite chart sorting: SBAS sats are separated from the rest
* Base sat levels are still displayed after corrections stop

##### Features

* RTKLIB update to newer beta. RTKLIB has been heavily updated
* Firefox support. Front-end has been updated to fix the insane behavior in this browser
* Display base on the map. 
* Smaller grid size. The minimum grid size has been decreased to 500mm

### v2.1.3 beta
([release](https://community.emlid.com/t/reachview-2-beta-v2-1-3-and-new-image/4495))

##### Bug fixes
* Disconnect not always working properly
* Make more informative disconnect notifications
* Implement NTRIP Server for base mode
* Display base on the map
* Base mode: add ability to average float
* Remember coordinate format after page refresh
* Fix a bug with map follow feature

##### Features

* New sattelite sorting

### v2.1.2 beta
([release](https://community.emlid.com/t/reachview-2-beta-v2-1-1/4404/49))

* Fixes Serial/USB problems


### v2.1.1 beta
([release](https://community.emlid.com/t/reachview-2-beta-v2-1-1/4404))

* Bug fixes
* Updater progress bar implemented
* Added loading screen

### v2.0 beta
([release](https://community.emlid.com/t/reachview-2-beta-release/4304))

* App rebuild. Improved general stability, user experience and usability. 

### v0.4.9

* Updated rtkrcv binary to RTKLIB 2.4.3 beta 16

### v0.4.8

* Fixed a bug with base not stopping correctly every time

### v0.4.7

* Updated RTKLIB binaries to 2.4.3 b16 and added a couple of patches by rtklibexplorer

### v0.4.6

* Updated **prnaccel** and **arlockcnt** values in default config files for better RTK results

### v0.4.5

* Added log delete confirmation popup
* Added button to delete logs by day
* Correction logs are now present in the logs tab

### v0.4.4

* Added RTKLIB integrity check on startup, which fixes the bug with logs not downloading properly
* Updated rtkrcv for better performance with dynamic filter on. 
* Updated rtkrcv send to more complete NMEA GGA to the base
* Improve startup time

### v0.4.3

* Updated repository readme

### v0.4.2

* Fixed lat-lon mix up in the status header

### v0.4.1

* Fixed a bug with two solutions set to file
* Fixed a bug with conversion cancellation
* JS console inside the app now shows full RTKLIB status

### v0.4.0

* Added support for UBX time marks when converting logs to RINEX

### v0.3.4

* Fixed an issue with Solution output 2 not working by itself

### v0.3.3

* Updated RINEX conversion timer to be more reailistic

### v0.3.2

* Added space meter to the logs tab
* RINEX logs now include SNR, doppler frequency and more
* Minimized probability of Reach forgetting its state

### v0.3.1

* Added Dynamic filter option to the rover's general tab.
* Fixed an issue where bluetooth.service file could be corrupted
* Added USB baud rate option

### v0.3.0

* Added ERB protocol support for Pixhawk integration

### v0.2.2

* Fixed not starting properly without an internet connection

### v0.2.1

* Fixed an issue where users with older ReachView version could not update correctly

### v0.2.0

* Added support for bluetooth scanning and pairing via ReachView
* Enabled bluetooth solution and log output

### v0.1.4

* Added Emlid favicon to the app

### v0.1.3

* ReachView will now show a blocking warning message when Reach is disconnected

### v0.1.2

* Added more headers to disable caching in browsers

### v0.1.1

* Set system time according to NTP(if available) or GPS on startup
* ReachView will start processing/logging until time is set

### v0.1.0

* Updated log tab looks
* Added reboot and turn off wi-fi buttons to settings tab
* Added image version to settings tab
* Added RINEX version chooser to settings tab
* Serial ports are now are now chosen from a select control
* Bugfixes

### v0.0.5

* Automatic log conversion to RINEX
* Fixed the issue, where base mode would not restart immediately
* Small visual updates and bugfixes

### v0.0.4

* Default receiver settings have been changed
* You can now set used GNSS systems and solution frequency for both base and rover modes
* Multiple bugfixes and improvements

### v0.0.3

* Moved the chart engine from [Chart.js](http://www.chartjs.org/) to [d3.js](http://d3js.org/)
* Added a separate "settings tab" with the update button and network information
* Pressing the update button now triggers an animation
* Minor visual updates to all tabs

### v0.0.2

* Fixed internal issue preventing the units from getting "<font color="yellow">Float</font>" or "<font color="green">Fix</font>" solution statuses in RTK modes

### v0.0.1

* First release


## Reach image changelog

### v2.1 beta
([release](https://community.emlid.com/t/reachview-2-beta-v2-1-3-and-new-image/4495))
([download link](https://files.emlid.com/images/ReachImage_v2.1_beta.zip))

* Intel's flashing tool issues solved



### v1.2

* Fixed the issue with unreliable Wi-Fi setup(mostly known as "Password does not match issue")
* Added various self-tests for corrupt internal software

### v1.1

* Fixed the issue preventing Reach from booting with a radio connected to a DF-13 connector
* Changes to boot setup process

### v1.0

* First release
