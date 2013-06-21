# Create a simple game using click detection.  Use clock to generate objects

from Panda import *

# Place a random panda on the screen.  If clicked, it goes away.
# leftClick is an event that happens when a particular model is clicked on
def randomPanda(m, v):
    if (random01() < .7):
        p = panda(position = P3(3*random01(), 0, 2*random01()), size = .2, duration = 2)
        p.react(leftClick(p), exitScene)
    else:
        p = jeep(position = P3(3*random01(), 0, 2*random01()), size = .2, duration = 2)
        p.react(rightClick(p), exitScene)

# Alarm generates an event at a given timestep (step)

c = alarm(step = .8)
react(c, randomPanda)


# Turn this into a game by doing the following:
#   Create a variable for the score
#   Stop the game after some amount of time
#   Add an explosion effect when a model is clicked
#   Make the models move instead of sit still
#   Add another kind of model





start()
