# This demonstrates the P3 and HPR classes and shows how the camera works.
# Can you tell where the camera is?

from Panda import *

p = panda()
p.position = sliderP3(label = "pos", min = -7, max = 7)
p.hpr = sliderHPR(label="hpr")
text(format("panda position: %s", p.position), size = 1.6, position = P2(-.5, .9))
text(format("panda hpr: %s", p.hpr), size = 1.6, position = P2(-.5, .8))

start()
