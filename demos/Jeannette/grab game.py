# intro to Panda/01-panda.py
from Panda import *

score = var(0)
tries = var(5)

#text("Score: " + string(score), color = green)
#text("Tries: " + string(tries), color = green)

camera.position = P3(0,0,20)
camera.hpr = HPR(0,-pi/2,0)
world.color = black

b = bunny(position = P3(getX(mouse),getY(mouse),17))

def bunnyDrop(m,v):
    b.position = b.position.now() + integral(P3(0,0,-8))
    b.when1(getZ(b.position) < 0, bunnyRise)
    tries.add(-1)
    if tries.get() < 0:
         text( "Great game! Your final score is " + string(score), position = P3(0,0,0), size = 2.5, color = green)
         text("...but you can do better.",position = P3(0,-.3,0), size = 2.5, color = green)
         fireWorks(position = P3(0,0,0), size = 3)
         b.exit()


def bunnyRise(m,v):
    m.position = b.position.now() + integral(P3(0,0,8))
    m.when1(getZ(b.position)>17 , bunnyStop)

def bunnyStop(m,v):
    b.position = b.position.now() - P3(getX(mouse).now(), getY(mouse).now(), 0) + P3(getX(mouse),getY(mouse), 0)
    b.react1(lbp, bunnyDrop)
b.react1(lbp, bunnyDrop)

def pickup(m,v):
    m.position = b.position.now()+P3(0,0,-5)+ integral(P3(0,0,8.5))
    score.add(1)

def makeTargets(m,v):
    p = panda(position = P3(random11()*2,random11()*3,0), hpr = HPR(random11(),random11(),random11()), size = random01(), color = color(random01(),random01(),random01()))
    p.react1(hit(p,b),pickup)



for i in range(31):
    makeTargets(b,0)





start()