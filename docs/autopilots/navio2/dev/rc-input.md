## RC input example

To be used in autopilot applications Navio needs to decode RC input. Navio2 supports both S.Bus and PPM input, which combines information about all PWM channels from the receiver in one sequence, which could be transferred over single wire. Channel values sent by remote controller will be decoded and then used for servo control.

RCInput example shows value of chosen PWM channel. You can specify the channel in source code.  
Connect PPM or S.Bus output from your RC receiver to the PPM/SB Input pin on Navio2. Note that your Navio should be powered off before connecting the receiver. 

If you haven't already done that, download Navio2 drivers and examples code [here](../../common/dev/navio-repository-cloning/).

### C++

Move to the folder with the source code, compile and run the example:
```bash
cd C++/Examples/RCInput
make
sudo ./RCInput
```
### Python

Move to the folder with the source code and run the example:
```bash
cd Python
sudo python RCInput.py
```
The program performs measurement of selected PWM channel and outputs measured values to console. The value will change if you move a stick on your RC transmitter. 

```bash
1087
1087
1087
1224
1322
1322
```

For further information see source code. Pay attention to ```rcin.init()``` and ```rcin.read()``` functions. ```rcin.init()``` function initialize 8 PWM channels. After that it's possible to read value of channels 0-7 with ```rcin.read()``` function. It takes channel number as an argument and you can change it.
