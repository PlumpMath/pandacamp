from Panda import *

# Use a clock and a velocity controller for a random path.

# This function generates a random direction
def f(x):
    return p3(random11(), random11(), random11())

# This generates a new random direction every .8 seconds

dirs = mapE(f, alarm(step = .8))
# Current direction is most recent direction
dir = hold(p3(0,0,0), dirs)
# Basic velocity control
p = panda(position = integral(integral(dir)))


#  Do this for 20 pandas
#
start()
