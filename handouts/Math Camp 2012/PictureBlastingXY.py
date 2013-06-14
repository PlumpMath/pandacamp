from Panda import *

pieces = blastPicture("mathcamp.jpg", 5, 5)

for p in pieces:
    p.position = itime(at(P3(random11(), random11(), random11())) + to(2, p.location))

start()