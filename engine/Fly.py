# To change this template, choose Tools | Templates
# and open the template in the editor.


from Panda import *


m = boeing707()

camera.position = p3(0,-50,0)

friction = -0.1
climbK = 1
rv = getX(mouse)
pv = getY(mouse)
gravity = p3(0,0,-1)
thrust = slider(max = 5)
m.position = p3(15, 0, 0) + integral(m.velocity)
m.velocity = p3(-5,0,0) + integral(m.accel)
roll = 0 + integral(rv*abs(m.velocity))
hpr1 = p3ToHpr(m.velocity)
m.hpr = hpr(getH(hpr1), getP(hpr1), roll)
m.accel = gravity + abs(m.velocity) * friction * norm(m.velocity) + getUp(m.hpr)*climbK*abs(m.velocity)
start()