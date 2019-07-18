RTK is a technique used to improve the accuracy of a standalone GNSS receiver. Traditional GNSS receivers, like the one in a smartphone, could only determine the position with 2-4 meters accuracy. RTK can give you centimeter accuracy.

GNSS receivers measure how long it takes for a signal to travel from a satellite to the receiver. Transmitted signals travel through the ionosphere and atmosphere and are slowed down and perturbed on the way. For example, travel time on a cloudy day and in clear sky conditions would be different. That is why it is difficult for a standalone receiver to precisely determine its position. RTK is a technology that solves this issue.

## High real-time precision

Two receivers are used in RTK. One of them is stationary, another moves freely. They are called **base station** and **rover**. 

<p style="text-align:center" ><img src="../img/reach/rtk-introduction/base-rover.jpg" style="width: 800px;" /></p>

Base's mission is to stay in one place, calculate distortions in satellites signals, and send corrections to a moving receiver. Rover uses that data to achieve centimeter precise position. Any number of rovers can connect to one base if their input settings match the base's output.

<p style="text-align:center" ><img src="../img/reach/rtk-introduction/multiple-rovers.jpg" style="width: 800px;" /></p>

## Corrections over NTRIP

You don’t necessarily need a second unit for RTK all the time. Usually, there are local services that share base corrections over the Internet. This technology is called NTRIP.

NTRIP is a good option for areas with strong 3G/LTE coverage and a vast network of NTRIP bases nearby. In other cases, using the second receiver as a local base station has two advantages:

* autonomy in remote areas as there’s no need in the Internet connection
* independency from local providers, no additional fees by NTRIP service

<p style="text-align:center" ><img src="../img/reach/rtk-introduction/NTRIP-corrections.jpg" style="width: 800px;" /></p>

##Single-band and multi-band receivers

Roughly speaking, there are two types of receivers: single-band (L1) and multi-band (L1/L2 or more). Their differences come from how much data they can receive from satellites.

For example, it helps to increase the maximum distance between base and rover, which is also called **baseline**:

<center>

|     | Single-band maximum baseline | Multi-band maximum baseline |
|:---:|:------------:|:------------:|
| RTK | 10 km | 60 km |
| PPK | 30 km | 100 km |

</center>

Multi-band receiver is also way more robust when it comes to sky view. It can maintain centimeter precision even if you survey in challenging conditions: forest, city, mining sights, quarries, etc.

<br>

Further Reading:

* [How PPK works](ppk-introduction.md)
* [Placing the base](placing-the-base.md)
* [Working with NTRIP service](ntrip-workflow.md)
