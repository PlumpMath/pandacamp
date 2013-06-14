# Demostrate collisions between objects and make a small avoidence game

from Panda import *

missles = collection()
# Here's a bunny that moves left / right with the arrows:
b = bunny()
v = hold(P3(0,0,0), key("left-arrow", P3(-1, 0, 0)) + key("right-arrow", P3(1, 0, 0)))
b.position = P3(0,0,-2) + integral(v)


def shootBall(m, v):
    soccerBall(size = .1, position = now(b.position) + integral(P3(0,0,3)), duration = 2, collection = missles)
    
# This is what happens if a panda hits a bunny
def blowUp(m, v):
    m.exit()
    play("explosion1.wav")
    resetWorld()
    text("Game Over")
    
       
def destruct(m, pairs):
    for (m, ball) in pairs:
        m.exit()
        ball.exit()
    
# This sends a random panda from above.  If it hits the bunny, the bunny disappears
def randomPanda(m, v):
    p = panda(position = P3(random11()*3, 0, 2-localTime), size = .3, duration = 4.1)
    b.react(hit(b,p), blowUp)
    b.react(hit(p, missles), destruct)

# This sends a new panda down every .8 seconds
react(key(" "), shootBall)

c = alarm(step = 2)
react(c, randomPanda)

# Todo:
#  Limit the number of soccerballs that the bunny can shoot.  Use a reactive variable
#  to represent this.  In shootBall, you can use now() to find out how many shots
#  are left.

start()
