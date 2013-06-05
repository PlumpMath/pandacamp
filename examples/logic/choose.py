from Panda import *

# A "conditional" allows you to choose one or the other alternative.
# We've seen "if" - there's another way to do this that allows you
# to constantly reconsider the choice:
# choose(test, (if True value), (if False value))
# For example, choose( time > 10, red, blue) will be either red or blue
# depending on the local time.

p = panda()

p.color = choose(time > 10 , red, blue)

p.position = choose(p.color == blue, p3(1,1,1), p3(0,0,0))

start()