# -*- coding: utf-8 -*-
from Panda import *

# Alter the initial position, velocity, and acceleration

camera.position=P3(0,-30, 10)
springLoc = P3(0,0,10)
sprinkK = 1
friction = -.3
def sn(t):
    return sin(t*3)/2.0+.5

def color1(r, g, b):
    return color(1-random01()*r*sn(localTime), 1-random01()*g*sn(localTime), 1-random01()*b*sn(localTime))

def launch(b, p0, v0):
    setType(b.velocity, P3Type)
    force = (b.position - springLoc) * (1- abs(b.position - springLoc)) + b.velocity * friction
    b.velocity = v0 + integral(force)
    b.position = p0 + integral(b.velocity)

def newBall1(m, v):
    p = panda()
    p.color = color1(1,1,1)
    launch(p, P3(2,0,5), P3(0,0, 0))

react(lbp, newBall1)


def newBall2(m, v):
    p = panda()
    p.color = color1(1,0,0)
    launch(p, P3(-2,0,5), P3(0,0, 0))

react(rbp, newBall2)



def newBall3(m, v):
    p = panda()
    p.color = color1(0,1,0)
    launch(p, P3(4,0,5), P3(0,0, 0))

react(lbp, newBall3)



def newBall4(m, v):
    p = panda()
    p.color = color1(1,1,0)
    launch(p, P3(-4,0,5), P3(0,0, 0))

react(rbp, newBall4)


def newBall5(m, v):
    p = panda()
    p.color = color1(1,0,1)
    launch(p, P3(-4,0,10), P3(0,0, 0))

react(lbp, newBall5)



def newBall6(m, v):
    p = panda()
    p.color = color1(0,1,1)
    launch(p, P3(4,0,10), P3(0,0, 0))

react(rbp, newBall6)


def newBall7(m, v):
    p = panda()
    p.color = color1(0,0,1)
    launch(p, P3(3,0,11), P3(0,0, 0))

react(lbp, newBall7)



def newBall8(m, v):
    p = panda()
    p.color = color1(1,1,1)
    launch(p, P3(-3,0,11), P3(0,0, 0))

react(rbp, newBall8)

start()
