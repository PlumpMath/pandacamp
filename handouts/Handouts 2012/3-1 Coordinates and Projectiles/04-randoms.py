from Panda import *

# Random placement of objects

# Some of the random number functions:
#  random01() - between 0 and 1
#  random11() - between -1 and 1
#  randomRange(low, high) or RandomRange(high)  - between low and high or 0 and high
#  randomChoice([c1, c2, c3, c4, ...]) - choose one of these values randomly
#  randomInt(low, high) or randomInt(high)  - integers between low and high or 0 and high

for i in range(10):
    panda(position = P3(3*random11(), 0, 2*random11()))

# Activities:
#   Add random headings - how do you get numbers between 0 and 2*pi?
#   Make the number of pandas random
#   Choose from a fixed set of colors
#   Choose a completely random color
#   Start all pandas at P3(0,0,0) and choose a random direction to explode them
#     (generate a random HPR and then set the panda HPR and the velocity using HPRtoP3
start()

