from Panda import *


(picture, pieces) = slicePicture( "AlienPandas.png", columns = 10, rows = 10, size = 2)
cube("Jeannette1.png", "Jeannette1.png", "Jeannette1.png", "Jeannette1.png", "Jeannette1.png", "Jeannette1.png", position = P3(2,-1,-1.5), hpr= HPR(time,time*.2,time*.6), size = sin(time))
warpSpeed(position = P3(0,0,0))
world.color = black

sphere(hpr = HPR(time,0,0), texture = "earthmap.jpg", size = 3, position = P3(0, 20, -2))
panda(position = P3(0,20,1), size = 3)
r2d2(position = P3(time/1.5,19,time/1.5), hpr = HPR(time*1.8, time*1.8, time*1.2))
fireish(size = smoothStep(time-4)*2, position = P3(0,18,-2), hpr = HPR(getX(mouse),0,0))
explosion(size = smoothStep(time-5)*2, position = P3(0,19,0))

for piece in pieces:
    piece.hpr = smoothStep(time-4)*integral(HPR(random11(),random11(), random11()))

camera.position = P3(0,(time*(time-3))-11,0)

start()