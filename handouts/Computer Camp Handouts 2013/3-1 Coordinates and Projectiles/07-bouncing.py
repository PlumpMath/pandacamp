from Panda import *

# Alter the initial position, velocity, and acceleration

camera.position=p3(0,-30, 6)
gravity = p3(0,0,-5)



def bounceFloor(m, v):
    v = now(m.velocity)
    p = now(m.position)
    v1 = p3(getX(v), getY(v), -getZ(v))
    launch(m, p, v1)


def newBall(m, v):
    p = panda()
    launch(p, p3(0,0,10), p3(0,0, 5))
    when(p,(getZ(p.position) < 0) & (getZ(p.velocity) < 0), bounceFloor)

react(lbp(), newBall)

start()
