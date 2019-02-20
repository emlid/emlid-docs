
**MB85RC04**

Ferroelectric RAM has the same functionality as flash memory, but increased overall write speed, lower power consumption and significantly bigger maximum number of write-erase cycles. All this makes FRAM-type memory devices a popular choice in embedded systems. The model we used on NAVIO is Fujitsu’s MB85RC04 with 4096 bytes of storage. It is connected over I<sup>2</sup>C. MB85RC04 uses a special I<sup>2</sup>C addressing system, shown in the image below:

![address](http://www.emlid.com/wp-content/uploads/2014/10/Screen-Shot-2014-10-07-at-13.31.47.png)

S is a start condition, part of theI<sup>2</sup>C protocol. It is followed by bits 1010, which are a device address prefix. Then, come three upper bits of the register address. On our device, we use 9-bit addresses, which means A2 and A1 always remain zeroes. After this comes a Read/Write bit(on this picture it is a 0, representing a write operation). Then, the device has to send back an Acknowledge statement(A on the white background). After the ‘ACK’ is received, I<sup>2</sup>C master sends the lower 8 bits of the register address. After another ‘ACK’, it sends the write data to the FRAM device.

**FRAM example**

Our FRAM example is in the `C++/Examples/FRAM` folder. Fram.cpp file contains a sequence of write/read tests, which write and then read specific values under the specific address of the memory. If the values read are the same as the values written, then the test is passed.

Change the directory to C++/Examples/Fram, then make and run the example:

```bash
cd C++/Examples/FRAM
make
./FRAM
```

After that, you will see program’s output, showing what it wrote, what it read afterwards and if the memory test is passed(pay attention to the last line of the output).

**FRAM driver**

To interact with I<sup>2</sup>C devices, we use the I2Cdev library, and the FRAM driver is a simple extension to it. It takes care of the 9-bit registeraddressing and also keeps the device address. The function `writeByte()` has two input parameters: a 16-bit register_address, which is a memory write location, and a data byte, which is to be written to the device. Our memory has the capacity of 512 bytes, so it uses a 9-bit address for inside memory mapping. It takes the 9 least significant bits from the register_address parameter and ignores the rest. MB85RC04 user manual requires to use the 9th bit as a part of the device address in the I<sup>2</sup>C write sequence, so it’s all complied to one variable dev_address. After that, we use the standard I2Cdev function to write a single byte over I<sup>2</sup>C.
