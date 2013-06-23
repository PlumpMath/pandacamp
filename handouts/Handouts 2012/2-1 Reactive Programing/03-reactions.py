from Panda import *


# You attach a reaction to a model by giving the triggering event and the name of the reaction function.

# exitScene is a built in reaction function

# This tells the panda to exit the scene when the right mouse button is pressed (lbp).
p = panda()
react(p, rbp(), exitScene)


# This reaction function is used to respond to a mouse click by launching a soccer ball.
# The first parameter is the model that is reacting - the now function is used to find the current
# value of a signal like the position. The soccer ball moves up from the position of the model.

# The value comes from the event that causes the reaction.  lbp doesn't generate a value so we ignore it.

def launch(model, value):
    pos = now(model.position)
    soccerBall(position = pos + integral(p3(0,0,4)), size = .05)

react(p, lbp(), launch)

# Activities
#   Write a velocity controller that uses the arrow keys to move the panda left and right
#   Make the panda face left or right depending on which way he's going
#   Make the soccer ball come up from the top of the panda instead of the bottom
#   Launch a ball on left mouse or on the space key
#   Change the launch event to generate a color and use this to change the color of the soccer ball
#   Launch a blue ball with the space key and a red one with the left button

# You can create reactions that are not attached to models.  Create a reaction function
# which launches a model into the scene that moves from left to right.
# Launce this model when the space key is pressed.

start()