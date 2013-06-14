from Panda import*

#main object
p0 = P3(0,0,0)
#hpr0 = HPR(pi,0,0)
#vel = P3(getX(mouse),0,getY(mouse))
vel2 = hold(p0, key('w', P3(0,0,1)) + key('a', P3(-1,0,0)) + key('s', P3(0,0,-1)) + key('d', P3(1,0,0)) + key('space', P3(0,0,0)) + key('arrow_up', P3(0,2,0)) + key('arrow_down', P3(0,-2,0)))
s = sphere(position = p0 + integral(vel2))

#camera
camera.position = s.position
panda(position = P3(0,10,0))

start()