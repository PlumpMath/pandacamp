# 01-racecar.py
#
# In virtual worlds there are different ways to recreate movement seen in the real world.
# In this file we try to recreate the movement of a car using
# Read the code along with the comments and try to understand how the behavior of a real car is being recreated.
#
# Run the file and drive the car around using the mouse to steer (move left and right) and to accelerate (move up and down).
# Does this car behave like a real car?
# Try running the next file and compare the two. Does this still seem realistic?

from Panda import *


friction = slider(min = 0, max = 2, label = "friction", init = 1)
text(format("Friction: %f", friction))

# create the scene
grassScene()

# create the vehicle
car = jeep()

# set camera
camera.position = P3(0,5,1)
camera.hpr = HPR(pi+integral(hold(0, key("left-arrow", .3) + key("right-arrow", -.3) + key(" ", 0))),0,0)  #  Lets you turn your head



# a is the angle of the steering wheel - the .2 gives this a realistic range
angle=-.2*getX(mouse)
# speed
setType(car.velocity,P3Type)
# The frictional force is proportional to the car velocity and goes against the direction of travel
fc = -friction * abs(car.velocity)
# s is the speed of the car
force = 2*(getY(mouse)+1) # this is now a force instead of a speed.  Range is 0 to 4
# speed
speed = integral(force + fc)
text(format("Speed: %f", speed))
# the current heading is the integral of the turning rate
heading = integral(speed*angle)
# velocity vector has the magnitude of the speed and direction of the heading.  The pi/2 is because
# the jeep model faces -y.
car.velocity = P3C(speed,heading-pi/2,0)
# Car position is the integral of the velocity
car.position = integral(car.velocity)

car.hpr = HPR(heading,0,0)

# run loop
start()
