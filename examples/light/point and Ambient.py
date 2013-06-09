from Panda import *

camera.position = P3(0, -16, 0)
#three pandas rotating on H P and R respectively
p1 = panda(position = P3(-1.5,0,0), hpr = HPR(time,0,0))
p2 = panda(position = P3(.5,0,0), hpr = HPR(0,time,0))
p2 = panda(position = P3(2.5,0,0), hpr = HPR(0,0, time))

#two sliders to control the brightness of the lights
s1 = slider(max = 1, min = 0, label="PL bright")
s2 = slider(max = 1, min = 0, label="AL bright")

#slider that controls position of point light
pls = slider(max = 7, min = 0, label="PL position")

#a small panda matching the movement of the light source
lightmarker = panda(position = P3C(4, pls , .25), size = .1)

#the point light source
pl = pointLight(color = color(s1 , s1 , s1 ), position = P3C(4, pls , .25))

#an ambient light source
al = ambientLight(color = color(s2 , s2 , s2 ))

# You'll note that the use of point lights makes the scene a lot more
# dramatic!  Without ambient light the models are completely black were they
# face away from the point light.

# Note how unnatural the gray background is - set world.color to black for a
# more natural scene.
world.color = black


start()

