from Panda import *
# You can add more photos to your nametag by placing some geometric solids in your animation

# You can put an arbitrary number of photos in a wheel, 6 photos on a cube, or 4 on a tetrahedron

a = photoWheel(["realpanda.jpg", "camplogo.jpg", "hurst.jpg" , "realpanda.jpg", "camplogo.jpg", "hurst.jpg"])

a.hpr = hpr(time*2, sin(time), 0)


#cube(t1, t2, t3, t4, t5, t6)



#tetra(t1, t2, t3, t4)



start()