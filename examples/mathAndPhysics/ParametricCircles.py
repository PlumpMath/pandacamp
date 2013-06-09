from Panda import *
# We're often interested in circular paths
# The basic trig functions, sine and cosine, create circular paths.
# The following function describes a circle that is centered at P3(0,0,0)
# and has a radius of 1.  The circle is in the y plane.

# The argument to sin and cos is an angle.  We measure angles in something
# called radians instead of degrees.  360 degrees = 2 * pi (~6.28) radians.
# Using this angle measurement sets the speed of the object on this path to 1

def f(t):
    return P3(2*sin(t), 0, 2*cos(t))

p = panda(position = f(time))


start()
