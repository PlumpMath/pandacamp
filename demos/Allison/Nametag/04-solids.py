from Panda import *
# You can add more photos to your nametag by placing some geometric solids in your animation

# You can put an arbitrary number of photos in a wheel, 6 photos on a cube, or 4 on a tetrahedron
world.color=blue
a = photoWheel(["campday1.jpg", "allison.jpg", "camp2.jpg" , "campday1.jpg", "allison.jpg", "camp2.jpg"])

a.hpr = HPR (0,time/2,0)



     
fragments = blastPicture("camp4.jpg", 10, 10)  # Cut a panda into 25 squares
camera.position=P3(0,-4,0)
for p in fragments:  
    t=randomRange(1,2)
    path=at(P3(randomRange(-3,3),randomRange(-3,3),randomRange(-2,2)))+to(2+t, P3(randomRange(-3,3),randomRange(-3,3),randomRange(-2,2)))+to(2+t, P3(randomRange(-3,3),randomRange(-3,3),randomRange(-2,2))) +to(3-t,p.location)    
    path2 = at(HPR(0,0,0)) + to(2, HPR(0, 0, 3))+to (2, HPR(0, 0, 3))+to (2, HPR(0, 0, 3)) +to (2, HPR(0, 0, 0))
    p.position=itime(path)
    p.hpr=itime(path2)
start()