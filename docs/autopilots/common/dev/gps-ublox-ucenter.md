### Connecting with U-center

![ucenter](http://www.emlid.com/wp-content/uploads/2014/10/U-center.png)
It is possible to connect to Navio's onboard u-blox GPS module from u-center software. To do that ublox-spi-to-tcp application has to be run on Raspberry:

The utility is available from our GitHub Navio repository. You can find cloning instructions [here](navio-repository-cloning/).

```bash
cd Utilities/ublox-spi-to-tcp
make
./ublox-spi-to-tcp 5000
```

It will open port 5000 and will wait for a connection.

Open u-center, navigate to Receiver - Port - Network connection - New. Enter the IP address of your Raspberry:

![utcp](http://www.emlid.com/wp-content/uploads/2014/10/UTCP.png)

You should see messages coming from the receiver in the Packet console as well as other visual data.
