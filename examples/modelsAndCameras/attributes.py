
from Panda import *

# The "." notation allows you to observe the position, hpr, size, or color
# of a named model.

p1 = panda(position = P3(-1, 0, 0))
p2 = panda(position = P3(1, 0, 0)


# To experiment with the size of a model.

p2.size = 2

# To experiment with the color of a model.
# Note that predifined colors are in the color documentation.

p1.color = red

# HPR stands for the Heading(turning your model left or right), Pitch (tilting your
# model up and down), and Roll (turning your model upside down) of a model.
# The parameters are angles in radians, so 2*pi is the same angle as 0,
# and 45 degress is 0.12 r pi/4 and 90 degress is 1.57 or pi/2.

p2.hpr = hpr(0.12, 0, 0)


start()


