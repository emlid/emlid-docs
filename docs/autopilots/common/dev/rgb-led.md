## RGB LED

If you haven't already done that, download drivers and examples code [here](navio-repository-cloning.md).

### C++

Move to the folder with the source code, compile and run the example
```bash
cd C++/Examples/LED
make
sudo ./LED
```
### Python

Move to the folder with the code and run the example:
```bash
cd Python
sudo python LED.py
```  

In this example Navio LED  changes color every second and outputs the color name to console.
```bash
LED is yellow
LED is green
LED is cyan
LED is blue
```

For further information see source code. You can change LED color using ```led.setColor()``` function, which takes color name as an argument. List of colors defined in ```C++/Navio/Navio2/RGBled.cpp```
