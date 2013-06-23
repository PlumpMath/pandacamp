from Panda import *

# Another way to move from one place to another in through interpolation.
# You can create a path using at and to:
# At puts you at a location and to moves you to a new location over a given amount of time.

# The "at" and "to" functions define a path - if you want to move along the path as time passes,
# the itime function uses the current time to select a place along the path.

p = panda()
path = at(p3(0,0,0)) + to(1, p3(1, 0, 0)) + to(1, p3(-1, 0, 1))  # This path takes 3 seconds (why?)

p.position = itime(path)


# Add another point to the path

# Create a path for the hpr of the panda

start()