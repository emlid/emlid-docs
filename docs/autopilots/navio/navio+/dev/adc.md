**ADS1115**

ADS1115 is a precision analog-to-digital converter (ADC) with 16 bits of resolution. The ADS1115 features an onboard reference and oscillator. Data is transferred via an I<sup>2</sup>C serial interface. The ADS1115 can perform conversions at rates up to 860 samples per second (SPS). Both large and small signals to be measured with high resolution ranging from 156mV to 3.3V. The ADS1115 also features an input multiplexer (MUX) that provides two differential or four single-ended inputs. The ADS1115 operates either in continuous conversion mode or a single-shot mode that automatically powers down after a conversion and greatly reduces current consumption during idle periods.

**ADS1115 example**

If you haven't already done that, download Navio drivers and examples code [here](../../common/dev/navio-repository-cloning/).

In this example ADC continuously measures voltage on all four pins available on the DF13 connector marked "ADC" on Navio. On Navio+ two ADC channels are present in "Power" connector and two on the bottom of the board. Result in mV is printed to console. 

***C++***

Move to the folder with the source code, compile and run the example:

```bash
cd C++/Examples/ADC
make
./ADC
```

***Python***

Move to the folder with the source code and run the example:

```bash
cd Python
python ADC.py
```

The program performs measurement of all 4 ADC channels and outputs measured values in millivolts in four columns. When channels inputs are not connected to anything there would probably be a little bit of potential.

```bash
A0: 0.5731mV A1: 0.5709mV A2: 0.5717mV A3: 0.5715mV
A0: 0.5716mV A1: 0.5715mV A2: 0.5717mV A3: 0.5726mV
A0: 0.5717mV A1: 0.5709mV A2: 0.5724mV A3: 0.5713mV
A0: 0.5711mV A1: 0.5717mV A2: 0.5721mV A3: 0.5715mV
A0: 0.5707mV A1: 0.5715mV A2: 0.5715mV A3: 0.5715mV
A0: 0.5724mV A1: 0.5731mV A2: 0.5719mV A3: 0.5713mV
```

For more detailed information please refer to the ADS1115 [datasheet](http://www.ti.com/lit/gpn/ads1115).
