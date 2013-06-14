# Demostrate collisions between objects and make a small avoidence game

from Panda import *

rectangle(p3(-4,1,-3),p3(4,1,-3), p3(-4,1,3), texture="space3.jpg")
score = var(0)
text(score)
planet=var(0)
text(planet)
textures=["venusmap.jpg","earthmap.jpg", "moonmap.jpg","marsmap.jpg","jupitermap.jpg","saturnmap.jpg","uranusmap.jpg","neptunemap.jpg","plutomap.jpg"]
nt=len(textures)
sizes=([.21,.3,.3,.2,.27,.8,.5,.5,.7,.2])
c=sphere(position=P3(-3,0,2.5), texture=textures[0],size=sizes[0])

# Here's a bunny that moves left / right with the arrows:
b = sphere(size=.4, texture="sun1.jpg")
v = hold(p3(0,0,0), key("leftArrow", P3(-1, 0, 0)) + key("rightArrow", P3(1, 0, 0)) +
                    happen(getX(b.position) < -3, p3(1,0, 0))  + happen(getX(b.position) > 3, p3(-1, 0, 0)))
b.position = p3(0,0,-2) + integral(v)
b.hpr= hold(hpr(3.14,0,0), key('leftArrow', hpr(3.5,0,0))+key('rightArrow', hpr(-3.5,0,-0)))


def shootBall(m, v):
    pos=now(b.position)
    soccerBall(size = .1, position = pos+p3(0,0,.5) + integral(p3(0,0,3)), duration = .5,color=red, kind = missle)
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
            exit(m)
    else:
        exit(m)
        play("explosion1.wav")
        resetWorld()
        text("Game Over",size=7, position= P2(0,0), color=blue,)
        text(score, size=4.5,position= P2(0,-.3),color=green)
        text(planet, size=4.5, position= P2(0,-.5),color=green)
        rectangle(P3(-4,1,-3),P3(4,1,-3), P3(-4,1,3), texture="space8.jpg")

def destruct(m, ball):
        exit(m)
        exit(ball)
        score.add(5)
        pos=now(m.position)
        shakenSparkles(position=pos, duration=.5,size=1)

# This sends a random panda from above.  If it hits the bunny, the bunny disappears
def randomPlanet(m, v):
    i=randomInt(nt-1)
    p = sphere(position = p3(random11()*3, 0, 2-localTime), duration = 4.1,texture=textures[i],size=sizes[i],
                hpr=integral(hpr(randomRange(1,5),0,0)))
    p.planet=i
    p.react(hit(b,p), blowUp)
    b.reactAll(hit(p, "missle"), destruct)
# This sends a new panda down every .8 seconds
react(key(" "), shootBall)

ck = alarm( 2)
react(ck, randomPlanet)


directionalLight(hpr=hpr(pi/4,pi/4,0), color = white)

ambientLight(color=color(.4,.4,.4))
# Todo:
#  Limit the number of soccerballs that the bunny can shoot.  Use a reactive variable
#  to represent this.  In shootBall, you can use now() to find out how many shots
#  are left.

start()
