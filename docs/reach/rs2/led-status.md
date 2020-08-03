Reach RS2 has several LEDs which are used as status indicators for different parts of the system.

![](../img/reachrs2/led-status/rs2.png){.reciever}

<div class="reciever-wrapper">    
<div class="reciever-container">
<div class="reciever-description">
    <h4>Battery</h4>
    <p>The lights above the power button indicate the battery charge level. If the loading animation is over, then you can connect your phone to Reach.</p>
</div>
<div class="reciever-status">
    <div class="status-wrapper"><img src="../img/reachrs2/led-status/booting.gif"><span>Loading</span></div>
    <div class="status-wrapper"><img src="../img/reachrs2/led-status/full-charge.jpg"><span>Full charge</span></div>
    <div class="status-wrapper"><img src="../img/reachrs2/led-status/charging.gif"><span>Charging</span></div>
    <div class="status-wrapper"><img src="../img/reachrs2/led-status/low-battery.jpg"><span>Low battery</span></div>
    <div class="status-wrapper"><img src="../img/reachrs2/led-status/Nech_boot.gif"><span>Not enough charge to boot</span></div>
</div>
</div>
<div class="reciever-container">
    <div class="reciever-description"> 
    <h4>Network</h4>
    <p>During boot, Reach RS2 enters a network scan state and searches for known networks to connect to. If it doesn't find a known network, it switches to hotspot mode.</p>
    </div>
    <div class="reciever-status">
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/broadcasting.png"><div class="wrapper-text">
        <span class="op-45">Solid:</span><span>Broadcasting Wi-Fi</span></div></div>
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/network-led.png"><div class="wrapper-text">
        <span class="op-45">Solid:</span><span>Connected to Wi-Fi network</span></div></div>
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/network scan.gif"><div class="wrapper-text">
        <span class="op-45">Blinking:</span><span>Scanning networks</span></div></div>
    </div>
</div>
<div class="reciever-container">
    <div class="reciever-description"><h4>RTK Status</h4>
    <p>This LED is used to display ReachView RTK status. RTK status has two colors: white and blue. White indicates incoming corrections, and blue indicates whether outgoing corrections are enabled. If the outgoing ones are turned off, there will only be a white LED. If enabled, the light will switch between white and blue every two seconds.</p>
    </div>
    <div class="reciever-status">
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/single.gif"><div class="wrapper-text">
        <span class="op-45">Slow blinking:</span><span>Single</span></div></div>
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/float.gif"><div class="wrapper-text">
        <span class="op-45">Fast blinking:</span><span>Float</span></div></div>
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/fix.png"><div class="wrapper-text">
        <span class="op-45">Solid:</span><span>Fix</span></div></div>
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/correction_output_is_turned_on.png"><div class="wrapper-text">
        <span class="op-45">Solid:</span><span>Corrections output is turned on</span></div></div>
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/rtk-status-led.png"><div class="wrapper-text">
        <span>No solution status</span></div></div>
    </div>
</div>
<div class="reciever-container">
    <div class="reciever-description">
        <h4>Power</h4>
        <p>The LED on the Power button shows two things: whether the receiver is on/off and the point collection process. When Reach is turned on, it lights up with a solid white light. When the point collection has started, the light flashes rapidly.</p>
    </div>
    <div class="reciever-status">
        <div class="status-wrapper"><img src="../img/reachrs2/led-status/point-collecting.gif"><div class="wrapper-text">
        <span>Point collection</span></div></div>
    </div>
</div>
</div>
