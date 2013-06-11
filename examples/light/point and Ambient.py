from Panda import *

camera.position = p3(0, -16, 0)
#three pandas rotating on H P and R respectively
p1 = panda(position = p3(-1.5,0,0), hpr = hpr(time,0,0))
p2 = panda(position = p3(.5,0,0), hpr = hpr(0,time,0))
p2 = panda(position = p3(2.5,0,0), hpr = hpr(0,0, time))

#two sliders to control the brightness of the lights
s1 = slider(max = 1, min = 0, label="Point Light Luminosity")
s2 = slider(max = 1, min = 0, label="Ambient Light Luminosity")

#slider that controls position of point light
pls = slider(max = 7, min = 0, label="Point Light Position")

#a small panda matching the movement of the light source
lightmarker = panda(position = p3c(4, pls , .25), size = .1)

#the point light source
pl = pointLight(color = color(s1 , s1 , s1 ), position = p3c(4, pls , .25))

#an ambient light source
al = ambientLight(color = color(s2 , s2 , s2 ))

# You'll note that the use of point lights makes the scene a lot more
# dramatic!  Without ambient light the models are completely black were they
# face away from the point light.

# Note how unnatural the gray background is - set world.color to black for a
# more natural scene.
world.color = black


start()

