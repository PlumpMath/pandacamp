from Panda import *

# Basic projectile motion

p = panda()
gravity = P3(0,0,-5)
velocity = integral(gravity)
pos = integral(velocity)
p.position = pos

# How to set the starting position?  The starting velocity?
start()