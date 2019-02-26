## ADC example

In this example ADC continuously measures voltage on all six channels available on Navio2. The first two channels are responsible for board voltage and servo rail voltage. Channels 2 and 3 show voltage and current levels in the “Power” connector respectively. The last two channels are present in "ADC" connector.

Download Navio2 drivers and examples code [here](../../common/dev/navio-repository-cloning/).

### C++

Move to the folder with the source code, compile and run the example:
```bash
cd C++/Examples/ADC
make
./ADC
```
### Python

Move to the folder with the source code and run the example:
```bash
cd Python
python ADC.py
```
The program performs measurement of all 6 ADC channels and outputs measured values in volts in six columns.
When channels inputs are not connected to anything there would probably be a little bit of potential.
```bash
A0: 4.7480V A1: 0.0860V A2: 0.0240V A3: 0.0200V A4: 0.0300V A5: 0.0140V 
A0: 4.7980V A1: 0.0860V A2: 0.0140V A3: 0.0220V A4: 0.0080V A5: 0.0160V 
A0: 4.7940V A1: 0.0860V A2: 0.0100V A3: 0.0100V A4: 0.0300V A5: 0.0140V 
A0: 4.7980V A1: 0.1040V A2: 0.0100V A3: 0.0200V A4: 0.0080V A5: 0.0300V 
A0: 4.7960V A1: 0.0900V A2: 0.0220V A3: 0.0080V A4: 0.0300V A5: 0.0140V 
A0: 4.7960V A1: 0.0860V A2: 0.0100V A3: 0.0220V A4: 0.0080V A5: 0.0320V
```
Mapping between A0 - A5 and ADC:  

* A0 - board voltage (shows 5V)  
* A1 - servo rail voltage  
* A2 - power module voltage (ADC0, POWER port)  
* A3 - power module current (ADC1, POWER port)  
* A4 - ADC2  (ADC port)  
* A5 - ADC3  (ADC port)

Numbers of A0 - A5 channels correspond to ArduPilot's ADC channels.

For further information see source code. Pay attention to ```adc.init()``` and ```adc.read()``` functions. ```adc.init()``` function initialize 6 ADC channels. After that it's possible to read value of channels 0-5 with ```adc.read()``` function. It takes channel number as an argument. 
