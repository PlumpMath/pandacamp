
from Panda import *
# Light sources can move - use the sliders to see how the illumination changes
# Note that the sphere doesn't block the light inside - there are no shadows in our 3-D world
panda(position = p3(0,0,0))

lp = sliderP3(min = -10, max = 10, label = "light")

pointLight(position = lp)
sphere(position = lp, size = 0.2)

start()
