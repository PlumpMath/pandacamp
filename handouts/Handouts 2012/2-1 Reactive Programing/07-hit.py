# Demostrate collisions between objects and make a small avoidence game

from Panda import *

# Here's a bunny that moves left / right with the arrows:
b = bunny()
v = hold(P3(0,0,0), key("left-arrow", P3(-1, 0, 0)) + key("right-arrow", P3(1, 0, 0)))
b.position = P3(0,0,-2) + integral(v)

# This is what happens if a panda hits a bunny
def blowUp(m, v):
    m.exit()
    play("explosion1.wav")
    resetWorld()
    text("Game Over")
    
       
# This sends a random panda from above.  If it hits the bunny, the bunny disappears
def randomPanda(m, v):
    p = panda(position = P3(random11()*3, 0, 2-localTime), size = .3, duration = 4.1)
    b.react(hit(b,p), blowUp)

# This sends a new panda down every .8 seconds

c = alarm(step = .8)
react(c, randomPanda)

# Todo:
#  Keep the bunny from going off the edge by putting in events that recognize the edges
#   of the game - use "happen" to turn a boolean into an event.  
#   The event happen(getX(p.position) > 2, v)) happens whenever the x coordinate of p's position > 2 and it
#   generates value "v" when it happens
#  Add a score that goes up with every new panda.  Display the score at the end of the game
#  Add an explosion and a 2 second delay before the game ends
#  Add a second kind of object dropping from above

start()
