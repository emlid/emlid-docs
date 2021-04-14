# Connecting Reach to the Internet

Connect Reach to the Internet to update ReachView 3 to the latest version or to get the corrections from your NTRIP service.


## Connecting to ReachView 3

??? note "Connecting to Reach with iOS/Android device"

	1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.emlid.reachview3) or [Apple Store](https://apps.apple.com/us/app/reachview-3/id1463967138)
	2. Go to *Wi-Fi settings* on your device
	3. Connect to Reach hotspot. It appears as **reach:XX:XX**
	4. Enter password **emlidreach**
	5. Launch the ReachView 3 app
	6. Choose Reach from the list

??? note "Connecting via a web browser from any device"

	1. Go to *Wi-Fi settings* on your device
	2. Connect to Reach hotspot. It appears as **reach:XX:XX**
	3. Enter password **emlidreach**
	4. Launch a web browser (we recommend using Chrome or Mozilla)
	5. Go to 192.168.42.1


## Connecting to Wi-Fi

* Go to the *Wi-Fi* tab

* Choose Wi-Fi network
	
	* Choose the available one if it’s visible
	
	* If you can’t see your mobile hotspot, press *Connect to a hidden network*

<p style="text-align:center" ><img src="../img/quickstart/connecting-to-the-internet/new-connection.png" style="height: 550px;" /></p>

* Fill in the connection form
	
	<details close>
	<summary> **Steps for Wi-Fi network** </summary>

	For Wi-Fi network fill in a password

	</details>


	<details close>
	<summary> **Steps for mobile hotspot** </summary>

	For mobile hotspot fill in *Network name*. Choose *Security type* and add a password if you have it.

	</details>


	!!! danger "Double check the password!"
		You can unmask the password by clicking on an eye symbol at the end of the password field.

<p style="text-align:center" ><img src="../img/quickstart/connecting-to-the-internet/hidden-network.png" style="height: 550px;" /></p>

* Press the *Connect* button. The blue LED should start blinking on Reach

	<p style="text-align:center" ><img src="../img/quickstart/connecting-to-the-internet/network-scan.gif" style="width: 400px;" /></p>


## Connecting process

??? note "Steps for Wi-Fi network"

	When connecting to Wi-Fi, wait until the blue LED starts blinking slowly.


??? note "Steps for mobile hotspot"

	When connecting to mobile hotspot, do the following steps:

	* Enable Wi-Fi hotspot on your mobile device
	* Check that it has the same name and password as you filled in the previous step
	* Now reboot the device with the *Power* button
	* Reach should connect to your hotspot during the next boot


* If the connection is successful, you will see the blue LED is blinking slowly

	<p style="text-align:center" ><img src="../img/quickstart/connecting-to-the-internet/running-client.gif" style="width: 400px;" /></p>

* If the connection fails, you will see the blue LED stays solid

	<p style="text-align:center" ><img src="../img/quickstart/connecting-to-the-internet/running-hotspot.png" style="width: 400px;" /></p>

	!!! tip "If the connection fails:"
		* Connect to Reach hotspot again
		* Check entered password
		* Check that your network is configured correctly
		* Try another Wi-Fi network


## Go back to ReachView 3

??? note "Connecting to Reach with iOS/Android device"
	
	1. Connect your mobile device to the same Wi-Fi network as Reach
	2. Scan for available Reach devices
	3. Choose Reach from the list in the app


??? note "Connecting via a web browser from any device"

	1. Connect your device to the same Wi-Fi network as Reach
	2. Use ReachView 3 to determine the Reach IP address 
	3. Go to IP address in a web browser

## Connecting to iOS hotspot

!!! note
	Starting with the iPhone 12 series, enable the *Maximize compatibility* option on its *Personal hotspot page*. This will switch its hotspot to 2.4 GHz and ensure connection to Reach.

The video below explains how you can connect Reach to hotspot of the iOS device.

<center>

<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/3HzC0hKL5f8" allowfullscreen></iframe></div>

</center>

Once Reach is connected to a Wi-Fi, you can:

* Update the receiver
* [Connect to NTRIP](../../reachview/correction-input/#ntrip)
