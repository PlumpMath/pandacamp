from Panda import *

# A function a way to do something more than once without having to
# type it in again and again.

# A function has a name and arguments - these parameters or arguments give
# "temporary" names to things that probably have a different name.  When you call
# a function, you tell the function what objects will get these temporary
# names.

# This function makes a panda at whatever x coordinate we want - this
# uses the temporary name "p".  p names a number - it could be any
# number, depending on what you pass in to makePanda:

def makePanda(p,c):
    panda(position = P3(p, 0, 0), color = c)

# Calling the function.

makePanda(1, red)
makePanda(1.5, blue)
makePanda(2, green)
makePanda(0, yellow)
makePanda(.5, purple)

start()
