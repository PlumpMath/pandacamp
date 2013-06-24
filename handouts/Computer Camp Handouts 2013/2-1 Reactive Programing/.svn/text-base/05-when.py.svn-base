from Panda import *

# Use when just like react except that this takes a condition (a true / false) proposition
# instead of an event.


# Make a panda moving right
score = var(0)
text(score)
speed = var(1)
    
p = panda(position = P3(time, 0, 0))

def startOver(m, v):
    m.position = P3(speed*localTime, 0, 0)
    score.add(1)
    speed.times(1.1)
    
p.when(getX(p.position) > 2, startOver)

# Add another reaction to move the panda back right when the X coordinate becomes < -2.

# We'll also use a variable, score, to keep track of how many times the panda bounces
# You can change the variable using .add, as in score.add(1).

# Once you have the score working, add another variable to keep track of how fast the panda
# is going.  Every time the panda bounces, multiple the speed by 1.1 (use .times(1.1)).
# How will you make the panda move faster using this speed variable?

start()