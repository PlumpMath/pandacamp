
from Panda import *
# Adjust the slider to set the speed of the panda.

speed = slider(min = -1, max = 1, init = 0)

# The "integral" operation turns speed into position.

xPos = integral(speed)

p = panda(position = p3(xPos , 0, 0))

text(format("Speed: %5.3f", speed))
text(format("Position: %5.3f", getX(p.position)))

start()