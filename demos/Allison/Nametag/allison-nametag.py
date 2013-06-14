from Panda import *
#Allison Camp 2012

world.color=blue
camera.position=p3(0,-4,0)

a = photoWheel(["campday1.jpg", "allison.jpg", "camp2.jpg" , "campday1.jpg", "allison.jpg", "camp2.jpg"])
a.hpr = hpr(0,time/2,0)

fragments = blastPicture("camp4.jpg", 10, 10)

for p in fragments:
    t=randomRange(1,2)
    path=at(p3(randomRange(-3,3),randomRange(-3,3),randomRange(-2,2))) + \
         to(2+t, p3(randomRange(-3,3),randomRange(-3,3),randomRange(-2,2))) + \
         to(2+t, P3(randomRange(-3,3),randomRange(-3,3),randomRange(-2,2))) + \
         to(3-t,p.location)
    path2 = at(hpr(0,0,0)) + to(2, hpr(0, 0, 3)) + to(2, hpr(0, 0, 3)) + to(2, HPR(0, 0, 3)) +to (2, hpr(0, 0, 0))
    p.position=itime(path)
    p.hpr=itime(path2)

start()