from Panda import *

pieces = blastPicture("mathcamp.jpg", 5, 5)

for p in pieces:
    p.position = itime(at(p.location) + move((p.x+5*p.y) % 8, P3(0,0,0)) + to(1, P3(20,0,0)))

start()