from Panda import *
# Abstraction is finding patterns and turning them into functions

# Suppose you want to create a line of different objects.  These all have
# a y and z coordinate of 0 but different x coordinates.
# There are lots of different kinds of things.

def f(m, x):
    m(position = p3(x, 0, 0), hpr = hpr(time, 0, 0))

f(panda, 2)
f(penguin, 1)
f(balloonBoy, 0)
f(bee, -1)

start()
