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

# create the scene
grassScene()

# create the vehicle
car = jeep()

# set camera
camera.position = P3(0,5,1)
camera.hpr = HPR(pi,0,0)



# a is the angle of the steering wheel
angle=-.2*getX(mouse)  # The .2 gives a realistic turning radius
text(format("Angle: %f", angle))
# s is the speed of the car
speed = 3*(getY(mouse)+1) # The 3 gives speeds between 0 and 6

# the current heading is the integral of the turning rate
heading = integral(speed*angle)
# velocity vector has the magnitude of the speed and direction of the heading.  The pi/2 is because
# the jeep model faces -y.
setType(car.velocity,P3Type)
car.velocity = P3C(speed,heading-pi/2,0)
# Car position is the integral of the velocity
car.position = integral(car.velocity)
car.hpr = HPR(heading,0,0)

# run loop
start()
