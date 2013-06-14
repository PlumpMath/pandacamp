from Panda import *

# The integral function turns a speed into a position.

# Change the numbers in the velecity and p0:
# 1. start the panda on the left and move him to the right.
# 2. start the panda at the center and move him to the camera.
# 3. Finaly move the panda from the lower left corner to the upper right.

p0 = P3(0,0,0) # p0 is the intial position
velocity = P3(0,0,0)
pos = p0 + integral(velocity)

# The Spin of an object is determind by the head, pitch, and roll or hpr.
# The direction that the object faces can be changed with the number of
# the hpr of s0. To get a object to spin add a number to the hpr of the svelocity.

# Try this: redo the first instuction but get the panda to face the direction it's
# traveling.
# Next: get the panda to flip, spin around, and a combo of both spining and flipping.

s0 = HPR(0,0,0)
svelocity = HPR(0,0,0)
spin = s0 + integral(svelocity)

panda(position = pos, hpr = spin)

start()