from Panda import *

# Here's a simple example of an animated nametag.

# Break the picture into a 5x5 grid
fragments = blastPicture("camplogo.jpg", 5, 5)

# Make each fragment travel from 0,0,0 to its final location.  The randomRange(.01) keeps them from all being at
# exactly the same y coordinate - take this out to see what happens when to pictures are at exactly the same place.

for f in fragments:
    f.position = itime(at(P3(0, randomRange(.01), 0)) + to(2, f.location))
    # After 4 seconds, start changing the HPR of each piece.
    f.hpr = integral(step(time-4)*HPR(2, 1, .5))
    
    
# Do the following:
#  a)  Change the motion to start the picture all together and after 2 seconds blast it into bits
#  b)  Use sin in the y coordinate so that the pictures "wave".  Add f.x/5 to the argument to sin to make it flutter.
#  c)  Use random numbers to make each piece rotate at a different rate or move in a different direction

start()
