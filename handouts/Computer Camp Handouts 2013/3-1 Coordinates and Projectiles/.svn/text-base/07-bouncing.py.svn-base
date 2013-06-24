from Panda import *

# Alter the initial position, velocity, and acceleration

camera.position=P3(0,-30, 6)
gravity = P3(0,0,-5)

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(gravity)
    b.position = p0 + integral(b.velocity)

def bounceFloor(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = P3(getX(v), getY(v), -getZ(v))
    launch(m, p, v1)


def newBall(m, v):
    p = panda()
    launch(p, P3(0,0,10), P3(0,0, 5))
    p.when((getZ(p.position) < 0) & (getZ(p.velocity) < 0), bounceFloor)

react(lbp, newBall)

start()
