# intro to Panda/01-panda.py
from Panda import *

panda()
# Create a panda at (0,0,0) and view it from different angles by setting
# the camera in different places
# Use camera.position = p3(x,y,z) to set your camera.
# Use panda(position = p3(x,y,z)) to create a panda
# If you don't assign a position to the panda it will be at position (0,0,0).
# How can you tell how tall the panda is?

# Note that the camera is by default pointed at positive Y
# Note that the bear is standing on the XY plane and facing -Y (the camera)
# Note that the field of view is such that standing 5 back shows z from
#   about -1 to 1
# Try going left (1, -5, 0) or close in (0, -1, 0) or (0, -2 0.5)

# Move the panda to (0,2,0) to see it go away from the camera

# Add another model like a bunny or a jeep to the scene
# Where is the "grab point" on each model?
# How big are these objects?  Which way do they face?

# Experiment with the hpr of this panda.  Create a second panda at P3(1, 0, 0) with a different hpr.
# Use hpr to create a hpr object.

# Move the camera using
# sliders to adjust the location and heading of the camera

# The sliderHPR and sliderP3 functions create sliders that return hpr / p3 information.
# Use max = and min = on the sliderP3 to set the numbers in the -10 to 10 range
# use label = "something" to give the sliders good names.

# Use text to display the P3 and HPR

# Here are all of the things you can adjust on a model:
#  position
#  hpr
#  color
#  size

# There are a lot of color names like red or orange.
# use the color function to create an arbitrary color: color(1, 0, 0) is red

# What happens when the size is negative?

start()