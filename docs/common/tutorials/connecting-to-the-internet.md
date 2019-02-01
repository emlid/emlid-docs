# Connecting Reach to the Internet

Connect Reach to the Internet to update ReachView to the latest version or to get the corrections from your NTRIP service.


## Connecting to ReachView

<details close>
<summary> **Connecting to Reach with iOS/Android device** </summary>

1. Get the app from [Google Play](https://play.google.com/store/apps/details?id=com.reachview) or [Apple Store](https://itunes.apple.com/us/app/reachview/id1295196887?mt=8)
2. Go to Wi-Fi settings on your device
3. Connect to Reach hotspot. It appears as **reach:XX:XX**
4. Enter password **emlidreach**
5. Launch ReachView app
6. Choose Reach from the list

</details>


<details close>
<summary> **Connecting via a web browser from any device** </summary>

1. Go to Wi-Fi settings on your device
2. Connect to Reach hotspot. It appears as **reach:XX:XX**
3. Enter password **emlidreach**
4. Launch a web browser (we recommend using Chrome or Mozilla)
5. Go to 192.168.42.1

</details>


## Connecting to Wi-Fi

* Go to the Wi-Fi tab

* Choose Wi-Fi network
	
	* Choose the available one if it’s visible
	
	* If you can’t see your mobile hotspot, press **Connect to a hidden network**

<p style="text-align:center" ><img src="../img/reach/connecting-to-the-internet/hidden-network.gif" style="width: 800px;" /></p>

* Fill in the connection form
	
	<details close>
	<summary> **Steps for Wi-Fi network** </summary>

	For Wi-Fi network fill in a password

	</details>


	<details close>
	<summary> **Steps for mobile hotspot** </summary>

	For mobile hotspot fill in Network name. Choose Security type and add a password if you have it.

	</details>


	!!! attention " Double check the password! "
		You can unmask the password by clicking on an eye symbol at the end of a password field.

<p style="text-align:center" ><img src="../img/reach/connecting-to-the-internet/new-connection.gif" style="width: 800px;" /></p>

* Press the **Connect** button. Blue LED should start blinking on Reach

	<p style="text-align:center" ><img src="../img/reach/connecting-to-the-internet/network-scan.gif" style="width: 400px;" /></p>


## Connecting process

<details close>
<summary> **Steps for Wi-Fi network** </summary>

If you connecting to Wi-Fi wait until the blue LED starts blinking slowly.

</details>


<details close>
<summary> **Steps for mobile hotspot** </summary>

If you connecting to mobile hotspot do the following steps:

* Enable Wi-Fi hotspot on your mobile device
* Check that it has the same name and password as you filled in the previous step
* Now reboot the device with the **Power** button
* Reach should connect to your hotspot during the next boot

</details>


* If the connection is successful, you will see blue LED is blinking slowly

	<p style="text-align:center" ><img src="../img/reach/connecting-to-the-internet/running-client.gif" style="width: 400px;" /></p>

* If the connection fails, you will see the blue LED stays solid

	<p style="text-align:center" ><img src="../img/reach/connecting-to-the-internet/running-hotspot.png" style="width: 400px;" /></p>

	!!! tip " If the connection fails: "
		* Connect to Reach hotspot again
		* Check entered password
		* Check that your network is configured correctly
		* Try another Wi-Fi network


## Go back to ReachView

<details close>
<summary> **Connecting to Reach with iOS/Android device** </summary>
	
1. Connect your mobile device to the same Wi-Fi network as Reach
2. Scan for available Reach devices
3. Choose Reach from the list in the app

</details>


<details close>
<summary> **Connecting via a web browser from any device** </summary>

1. Connect your device to the same Wi-Fi network as Reach
2. Use [one of the Network Scan utility](https://docs.emlid.com/reachrs/quickstart/#accessing-reach-rsrs-device-in-a-network) or ReachView app to determine the Reach IP address 
3. Go to IP address in a web browser

</details>


Once Reach is connected to a Wi-Fi, you can:

* [Update the receiver](/common/reachview/settings/#check-app-version)
* [Connect to NTRIP](/common/reachview/correction-input/#ntrip)