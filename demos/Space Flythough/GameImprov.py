from Panda import*
from ourModels import*
#sphere(size = -500, color = white)
space4(position = P3(0,3,0))

#part1 : set up
a=getX(mouse)
b=getY(mouse)
p0 = P3(0,0,0)
hpr0 = HPR(0,0,0)
hprp = HPR(-a/2, b/2, 0)

#part2 : camera set up
camera.hpr = hpr0 + integral(hprp)
h = getH(camera.hpr)+pi/2
fv = hold(0, key('w', 5) + keyUp('w', 0))
v = P3C(fv, h, 0)

#part3 : objects
s = sphere(position = integral(v))
camera.position = s.position


start()