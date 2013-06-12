from Panda import *

# For loops itterate over the same code for a given number of times defined
# by the range. For loops itterarte from 0 to the n-1.


# This example is making 5 pandas in row whose path is subject to time.

def path(t):
    return P3(t-2, 0, sin(t*2))

for x in range(5):
    panda(position = path(time-x))

start()