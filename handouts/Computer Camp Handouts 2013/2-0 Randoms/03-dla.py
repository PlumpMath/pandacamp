from Panda import *



camera.position = p3(0,0,100)
camera.hpr = hpr(0,-pi/2,0)


worldSize = 25
vel = 100
def bounceLeft(m, v):
    n = now(m.position)
    m.position = p3(-worldSize, getY(n), 0) + integral(p3c(vel,randomRange(0, pi)-pi/2, 0))

def bounceRight(m, v):
    n = now(m.position)
    m.position = p3(worldSize, getY(n), 0) + integral(p3c(vel,randomRange(pi, 2*pi)-pi/2, 0))

def bounceTop(m, v):
    n = now(m.position)
    m.position = p3(getX(n), worldSize, 0) + integral(p3c(vel,randomRange(-pi/2, pi/2)-pi/2, 0))

def bounceBottom(m, v):
    n = now(m.position)
    m.position = p3(getX(n), -worldSize, 0) + integral(p3c(vel,randomRange(pi/2, 3*pi/2)-pi/2, 0))

def hitStatic(m1, m2):
    exit(m1)
    sphere(position = now(m1.position), kind = "static", color = color(random01(), random01(), random01()))
    genBall()

def genBall():
    b = soccerBall(position = p3c(worldSize,randomRange(0, pi), 0) +\
                   integral(p3c(vel,randomRange(0, 2*pi), 0)), kind = "bouncer")
    when(b,getX(b.position)>worldSize, bounceRight)
    when(b,getX(b.position)<-worldSize, bounceLeft)
    when(b,getY(b.position)>worldSize, bounceTop)
    when(b,getY(b.position)<-worldSize, bounceBottom)
    react(b, hit("bouncer", "static"), hitStatic)

genBall()

volleyBall(position = p3(0,0,0), kind="static")
start()


