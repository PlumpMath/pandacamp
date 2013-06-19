from Panda import *

camera.position=p3(0,-30, 6)
gravity = p3(0,0,-5)
l=boeing707(size = 3)
def col(t):
    return interpolate(t, forever(at(red) + to(.5, purple) + to(.5, blue) + to(.5, green) + to(.5, yellow) + to(.5, orange) + to(.5, red)))

def moveLeft(m,p):
    p = m.position.now()
    l.position=  p + p3(-localTime*3, 0, 0)

def moveRight(m,p):
    p = m.position.now()
    l.position=  p + p3(localTime*3, 0, 0)
    #to (1,p3(getX(l.position)-1, 0, getZ(l.position))))
l.react(lbp, moveLeft)
l.react(rbp, moveRight)

def launch(b, p0, v0):
    setType(b.velocity, p3Type)
    b.velocity = v0 + integral(gravity)
    b.position = p0 + integral(b.velocity)

def bounceFloor(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = p3(getX(v), getY(v), -getZ(v)*.95)
    launch(m, p, v1)

def bounceRight(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = p3(-getX(v), getY(v), getZ(v))
    launch(m, p, v1)

def bounceLeft(m, v):
    v = m.velocity.now()
    p = m.position.now()
    v1 = p3(-getX(v), getY(v), getZ(v))
    launch(m, p, v1)

def newBall(m, v):
    p = r2d2(size = 2)
    launch(p, p3(0,0,10), p3(5, 0, 5))
    p.when((getZ(p.position) < 0) & (getZ(p.velocity) < 0) & (abs(p.position - l.position)<2.5), bounceFloor)
    p.when((getX(p.position) > 10) & (getX(p.velocity) > 0 ), bounceRight)
    p.when((getX(p.position) < -10) & (getX(p.velocity) < 0 ), bounceRight)
    p.when1((getZ(p.position) < -2), die)

def die(m,v):
    text(("You Lose"), position = P2(-.3,.3),size = 10)

world.color = col(localTime/2)

a = alarm(start = 1, step = .4)

react1(a, newBall)
start()