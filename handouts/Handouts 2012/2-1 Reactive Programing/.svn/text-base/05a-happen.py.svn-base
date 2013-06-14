from Panda import *

# Use "happen" to make an event from a boolean


# Make a velocity controller
p = panda()
v = hold(P3(0,0,0), key("left-arrow", P3(-2, 0, 0)) + key("right-arrow", P3(2, 0, 0)) +
                    happen(getX(p.position) < -3, P3(0,0, 0))  + happen(getX(p.position) > 3, P3(0, 0, 0)))


p.position = integral(v)



start()