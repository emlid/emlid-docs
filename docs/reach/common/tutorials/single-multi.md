## Getting started

The main idea behind the GNSS receiver work is receiving signals from satellites. Each satellite transmits radio signals in one or more frequency bands. Satellites in different constellations use different frequencies.

In the main, all receivers can be divided into two categories: single-band and multi-band. The core difference is that single-band receivers only work with one frequency, while multi-band receivers fetch several frequency bands.

<p style="text-align:center" ><img src="../img/reach/single-multi/satellites.jpg" style="width: 800px;" /></p>

## What’s the Difference

The main difference between single-band and multi-band receivers is the number of frequencies they can work with. Other differences technically are the consequences of it.

<center>

|     | Reach RS2 | Reach RS+ |
|:---:|:------------:|:------------:|
| Frequency bands | Multi-band | Single-band |
| Time to first fix | ~5 sec | 1-2 min |
| Positioning accuracy in RTK | H: 7 mm + 1 ppm | H: 7mm + 1 ppm |
| | V: 14 mm + 1 ppm | V: 14 mm + 1 ppm |
| Baseline in RTK mode | Up to 60 km | Up to 10 km |
| Baseline in PPK mode | Up to 100 km | Up to 20 km |
| 3.5G modem| Reach RS2 has embedded cellular modem | No |
| LoRa radio | Yes | Yes |

</center>

### RTK Initialisation Time

Several factors affect the time required to obtain a fix. This is where the number of tracked frequencies matter.

A multi-band receiver is capable of finding a fix solution much more quickly. Since multi-band receivers can work with more than one frequency band, they can use more satellite signals to establish the fix solution. The more signals that are available, the less time is needed to obtain the fix. Reach RS2 requires ~5 seconds to get fix solution.

Single-band receivers require more time since they can only process one kind of frequency—the L1 frequency. Reach RS+ needs a few minutes to get a fix solution. It doesn’t mean you need to wait for several minutes every time you collect a point. This time is only required at the beginning of the survey or in the case where the fix solution was lost.

### Baseline

<p style="text-align:center" ><img src="../img/reach/single-multi/base-rover.jpg" style="width: 800px;" /></p>

For different projects, you might need a different distance from the rover to the base. Working near a city, you are more likely to have a base nearby. However, if you mostly work in rural areas, base stations are likely to be further away.

Multi-band receivers can work at a longer baseline. Reach RS2, as a multi-band receiver, can operate with the baseline up to 60 km for RTK, while Reach RS+ single-band receiver’s baseline is limited to 10 km in RTK mode.

### Accuracy

Both single-band and multi-band receivers are capable of centimeter-level absolute accuracy. The main difference is that more factors can influence the stable fix solution in the single-band receiver. Thus, when using a single-band receiver, you can obtain the same absolute accuracy, but only if you have reasonable working conditions.

### Sky View Conditions

In the case of a blocked sky view, the more signals, the better, meaning the more signals you can catch, the sooner you get the fix solution. Due to their ability to process several frequencies and mitigate the multi-path impact, multi-band receivers can keep the reliable fix solution even in urban areas.

Single-band receivers need the open sky to work their best. Otherwise, it might be harder and take longer to establish a fix solution.

## Which One to Choose

Both single-band and multi-band receivers obtain the same level of accuracy in their perfect conditions – so, first of all, you need to analyze your case.

Single-band receivers are perfect for working in the field with shorter baselines and a clear sky view. Say, you’re working in agriculture and you need to divide your field into equal sectors or determine the position for trees in an orchard-to-be, a single-band receiver is enough. They also make a great base for PPK or drone mapping.
Multi-band receivers make a perfect fit for [PPP, such as OPUS or NRCan](ppp-introduction.md), and high-accuracy surveying in tougher conditions. If you’re working in the city and you have a longer baseline, or the base station is too far, plus you want the job to be done fast, a multi-band receiver is your choice. It gets the fix solution faster despite the possible obstacles and distance from the base.

## Conclusion

In the majority of cases, the single-band receiver is enough to perform an accurate survey and collect reliable data. It also helps you save yourself a penny budget-wise. However, if you are not sure your working conditions will be perfect or you simply don’t want to worry about possible technical limitations, stick to the multi-band receiver. It will be a more reliable option.

If you have any questions or still have doubts about whether you need a single-band or multi-band receiver, do not hesitate to start a thread on the [community forum](https://community.emlid.com/).

## Further reading

- [How RTK works](rtk-introduction.md)
- [Precise Point Positioning (PPP)](ppp-introduction.md)
- [Placing the base](placing-the-base.md)
