# Connecting Reach to the Internet

Connect Reach to the Internet to update ReachView to the latest version or to get the corrections from your NTRIP service.

??? note "Connecting Reach to the Internet via a built-in cellular modem"
	##Video guide

	The video below covers the process of SIM card setup.

	<center>

	<div style="text-align: center;"><iframe width="560" height="315" src="https://www.youtube.com/embed/YJ2VzsKx9zQ" allowfullscreen></iframe></div>

	</center>

	## Text guide

	### SIM card setup

	!!! note ""
		Make sure you have a nano-SIM card. You can cut your SIM сard to the format.

	* Find the SIM card slot under the black sealing

	!!! danger ""
		To prevent slot damage, please use it with care.

	* Slide the metallic cover to the right to unlock the slot

	<div style="text-align: center;"><img src="../img/reachrs2/connecting-to-the-internet/1-sim-card.png" style="width: 200px;"></div>

	* Pull the cover up to open the SIM card slot

	<div style="text-align: center;"><img src="../img/reachrs2/connecting-to-the-internet/2-sim-card.png" style="width: 200px;"></div>

	* Insert your SIM card into the metallic cover

	<div style="text-align: center;"><img src="../img/reachrs2/connecting-to-the-internet/3-sim-card.png" style="width: 200px;"></div>

	* Return the slot cover into the horizontal position and slide left to lock the slot

	<div style="text-align: center;"><img src="../img/reachrs2/connecting-to-the-internet/4-sim-card.png" style="width: 200px;"></div>

	### Configuring Mobile Data

	* Power up your receiver and connect to it via ReachView app on your device

	??? note "Connecting to Reach with iOS/Android device"

		1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [Apple Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
		2. Go to Wi-Fi settings on your device
		3. Connect to Reach hotspot. It appears as **reach:XX:XX**
		4. Enter password **emlidreach**
		5. Launch ReachView app
		6. Choose Reach from the list

	??? note "Connecting via a web browser from any device"

		1. Go to Wi-Fi settings on your device
		2. Connect to Reach hotspot. It appears as **reach:XX:XX**
		3. Enter password **emlidreach**
		4. Launch a web browser (we recommend using Chrome or Mozilla)
		5. Go to 192.168.42.1

	* Wait until Reach finishes loading your SIM сard

	!!! note ""
		If the SIM сard requires a PIN code, the app will ask you to type it into the pop-up field. If you don't know your PIN code, contact your cellular service provider for this information.

	You will see the network bars indicating a connected SIM сard. 

	* Go to [Mobile data tab](reachview/mobile-data.md) and enable cellular network

	<div style="text-align: center;"><img src="../img/reachrs2/connecting-to-the-internet/mobile-data.png" style="width: 800px;"></div>

	If everything is correct, you will see the network bars and the connection type next to the battery icon showing Mobile data is turned on.

??? note "Connecting Reach to the Internet over Wi-Fi"
	## Connecting to ReachView

	??? note "Connecting to Reach with iOS/Android device"

		1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [Apple Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
		2. Go to Wi-Fi settings on your device
		3. Connect to Reach hotspot. It appears as **reach:XX:XX**
		4. Enter password **emlidreach**
		5. Launch ReachView app
		6. Choose Reach from the list

	??? note "Connecting via a web browser from any device"

		1. Go to Wi-Fi settings on your device
		2. Connect to Reach hotspot. It appears as **reach:XX:XX**
		3. Enter password **emlidreach**
		4. Launch a web browser (we recommend using Chrome or Mozilla)
		5. Go to 192.168.42.1


	## Connecting to Wi-Fi

	* Go to the Wi-Fi tab

	* Choose Wi-Fi network
		
		* Choose the available one if it’s visible
		
		* If you can’t see your mobile hotspot, press *Connect to a hidden network*

	<p style="text-align:center" ><img src="../img/reachrs2/connecting-to-the-internet/hidden-network.gif" style="width: 800px;" /></p>

	* Fill in the connection form
		
		<details close>
		<summary> **Steps for Wi-Fi network** </summary>

		For Wi-Fi network fill in a password

		</details>


		<details close>
		<summary> **Steps for mobile hotspot** </summary>

		For mobile hotspot fill in Network name. Choose Security type and add a password if you have it.

		</details>


		!!! danger "Double check the password!"
			You can unmask the password by clicking on an eye symbol at the end of a password field.

	<p style="text-align:center" ><img src="../img/reachrs2/connecting-to-the-internet/new-connection.gif" style="width: 800px;" /></p>

	* Press the *Connect* button. Network LED should start blinking blue on Reach

		<p style="text-align:center" ><img src="../img/reachrs2/connecting-to-the-internet/network-scan.gif" style="width: 200px;" /></p>


	## Connecting process

	??? note "Steps for Wi-Fi network"

		If you connecting to Wi-Fi wait until the Network LED stays solid blue.


	??? note "Steps for mobile hotspot"

		If you connecting to mobile hotspot do the following steps:

		* Enable Wi-Fi hotspot on your mobile device
		* Check that it has the same name and password as you filled in the previous step
		* Now reboot the device with the **Power** button
		* Reach should connect to your hotspot during the next boot


	* If the connection is successful, you will see the Network LED stays solid blue

		<p style="text-align:center" ><img src="../img/reachrs2/connecting-to-the-internet/client-mode.png" style="width: 200px;" /></p>

	* If the connection fails, you will see the Network LED stays solid white

		<p style="text-align:center" ><img src="../img/reachrs2/connecting-to-the-internet/hotspot.png" style="width: 200px;" /></p>

		!!! tip "If the connection fails:"
			* Connect to Reach hotspot again
			* Check entered password
			* Check that your network is configured correctly
			* Try another Wi-Fi network


	## Go back to ReachView

	??? note "Connecting to Reach with iOS/Android device"
		
		1. Connect your mobile device to the same Wi-Fi network as Reach
		2. Scan for available Reach devices
		3. Choose Reach from the list in the app


	??? note "Connecting via a web browser from any device"

		1. Connect your device to the same Wi-Fi network as Reach
		2. Use [one of the Network Scan utility](https://docs.emlid.com/reachrs/quickstart/first-setup/#accessing-reach-rsrs-device-in-a-network) or ReachView app to determine the Reach IP address 
		3. Go to IP address in a web browser


Once Reach connects to the Internet, you can:

* [Update the receiver](../reachview/settings/#check-app-version)
* [Connect to NTRIP](../common/tutorials/ntrip-workflow/)