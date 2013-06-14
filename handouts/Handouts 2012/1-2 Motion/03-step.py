
from Panda import *

# The step function is one that changes from 0 to 1 as the input goes from negative to positive,
# You can use this to delay movement or move to a new place.
# While step transitions when the input is 0, you can make the transition at any time by subtracting the time
# of the transition from the argument.  For example, step(time-2) steps at time 2.

# This panda jumps at time 2

panda(position = P3(step(time-2), 0, 0))

# When you combine step with a velocity controller you get delayed motion.

# Multiply the velocity below by a step to make the motion start later
p0 = P3(0,0,0) # p0 is the intial position
velocity = P3(0,0,0)
pos = p0 + integral(velocity)
# Change the panda to use this position
# You can use "smoothStep" instead of steo if you want to start slowly
start()