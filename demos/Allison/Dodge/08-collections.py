# Demostrate collisions between objects and make a small avoidence game

from Panda import *

rectangle(P3(-4,1,-3),P3(4,1,-3), P3(-4,1,3), texture="space3.jpg")
score = var(0)
text(score)
planet=var(0)
text(planet)
textures=["mercurymap.jpg","venusmap.jpg","earthmap.jpg", "moonmap.jpg","marsmap.jpg","jupitermap.jpg","saturnmap.jpg","uranusmap.jpg","neptunemap.jpg","plutomap.jpg"]
nt=len(textures)
sizes=([.21,.3,.3,.2,.27,.8,.5,.5,.7,.2])
c=sphere(position=P3(-3,0,2.5), texture=textures[0],size=sizes[0])
missles = collection()
# Here's a bunny that moves left / right with the arrows:
b = sphere(size=.4, texture="sun1.jpg")
v = hold(P3(0,0,0), key("left-arrow", P3(-1, 0, 0)) + key("right-arrow", P3(1, 0, 0)) +
                    happen(getX(b.position) < -3, P3(1,0, 0))  + happen(getX(b.position) > 3, P3(-1, 0, 0)))
b.position = P3(0,0,-2) + integral(v)
b.hpr= hold(HPR(3.14,0,0), key('left-arrow', HPR(3.5,0,0))+key('right-arrow', HPR(-3.5,0,-0)))


def shootBall(m, v):
    pos=now(b.position)
    soccerBall(size = .1, position = pos+P3(0,0,.5) + integral(P3(0,0,3)), duration = .5, collection = missles,color=red)
    score.add(-1)
    
# This is what happens if a panda hits a bunny
def blowUp(m, v):
    if now(planet) == now(m.planet):
        planet.add(1)
        if now(planet) == nt-1:
            text("You Win!", color=green)
            text(score, size=4.5,position= P2(0,-.3),color=green)
            text(planet, size=4.5, position= P2(0,-.5),color=green)
            rectangle(P3(-4,1,-3),P3(4,1,-3), P3(-4,1,3), texture="space8.jpg")
        else:
            c.setTexture(textures[now(planet)+1])
            c.size=sizes[now(planet)+1]
            m.exit()
    else:
        m.exit()
        play("explosion1.wav")
        resetWorld()
        text("Game Over",size=7, position= P2(0,0), color=blue,)
        text(score, size=4.5,position= P2(0,-.3),color=green)
        text(planet, size=4.5, position= P2(0,-.5),color=green)
        rectangle(P3(-4,1,-3),P3(4,1,-3), P3(-4,1,3), texture="space8.jpg")
       
def destruct(m, pairs):
    for (m, ball) in pairs:
        m.exit()
        ball.exit()
        score.add(5)
        pos=now(m.position)
        shakenSparkles(position=pos, duration=.5,size=1)
    
# This sends a random panda from above.  If it hits the bunny, the bunny disappears
def randomPanda(m, v):
    i=randomInt(nt-1)
    p = sphere(position = P3(random11()*3, 0, 2-localTime), duration = 4.1,texture=textures[i],size=sizes[i],
                hpr=integral(HPR(randomRange(1,5),0,0)))
    p.planet=i
    p.react(hit(b,p), blowUp,)
    b.react(hit(p, missles), destruct)
# This sends a new panda down every .8 seconds
react(key(" "), shootBall)

ck = alarm(step = 2)
react(ck, randomPanda)


directionalLight(hpr=HPR(pi/4,pi/4,0), color = white)

ambientLight(color=color(.4,.4,.4))
# Todo:
#  Limit the number of soccerballs that the bunny can shoot.  Use a reactive variable
#  to represent this.  In shootBall, you can use now() to find out how many shots
#  are left.

start()
