### What is Reach and what is it for?

Reach is an RTK GNSS receiver for applications when your standard GPS with several meters accuracy just won’t cut it. It relies on RTK (real-time kinematics) technology to deliver centimeter level accuracy.

RTK was here for a long time, used mostly by surveyors and unaffordable to hobbyists and makers. If you needed centimeter precise positioning you had to spend thousands of dollars on an RTK system. With Reach we want to change that.

Reach runs open-source RTK processing software called RTKLIB written by Tomoji Takasu. Previously a computer was required to run RTKLIB, but now all RTKLIB features are available directly on Reach.

### What is an RTK?

RTK is a technique used to improve the accuracy of gps system. Traditional GPS receivers, like one you can find in your smartphone, or on most robotic platforms could only determine  their position with 2-4 meters accuracy. RTK can give you centimeters.

The whole GPS system is based on measuring how long does it take for a signal to travel from a satellite to the receiver. Knowing the precise orbits of the space vehicles – the ephemeris, and at least 4 travel times one can determine his position on the planet.
Given the L1 GPS carrier frequency is 1575MHz, each wave is around 19cm in length. A receiver also measures the carrier phase of each of the signals. Theoretically, this should have given  us millimeter precision, so why do we still have to struggle with 2-4 meters accuracy? What are the sources of error, and what we can do to remove them?

The satellites orbit at 20 200 km above Earth surface. Transmitted signals travel through ionosphere and atmosphere and are slowed down and perturbed on the way. For example, travel time on cloudy day and in clear sky conditions would be different! Many factors can increase position error, the great thing is that we can assume that these factors do not change much in one area.

There are GPS augmentation systems (DGPS), like SBAS or WAAS that measure current signal perturbations on many ground control stations all over the world, build a error propagation model and broadcast corrections through satellites or radio. Many commercial receivers can use these signals for submeter positioning accuracy. But what to do if you want to get closer to centimeters?

The technology that would let us do it is called RTK (real-time kinematics). Two receivers are used, one of them is stationary and is called “base station”, the other one is “rover”. The base station measures errors, and knowing that it is stationary transmits corrections to the rover. The idea is simple, but not the math. Commercial systems could be subcentimeter precise and would cost you a fortune($5k+).

Also, if you do not need the precise coordinates in real-time, you can just record the data from the rover and the base and process it afterwards thus eliminating need in constant radiolink. This method is called post processing and is the most precise among all.

** Comparison of RTK and standalone coordinates **

*Static mode:*

<p style="text-align:center" ><img src="../img/reach/rtk-introduction/reach-static-rtk-demo.png" style="width: 800px;" /></p>

*Kinematic mode:*

<p style="text-align:center" ><img src="../img/reach/rtk-introduction/reach-kinematic-rtk-demo.png" style="width: 800px;" /></p>
