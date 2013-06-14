from Panda import *


# blastPicture takes a picture and slices it up into a bunch of rectangles.  Each of these has
# properties .x, .y, and .location.  If you put each fragment in its .location you'll see the picture
# is fully assembled.  

fragments = blastPicture("realpanda.jpg", 5, 5)  # Cut a panda into 25 squares

for p in fragments:
    p.position = p.location
    p.hpr = HPR(time*random01(), 0, 0)



start()