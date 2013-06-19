
from modelsMedevil import*
al = ambientLight(color = color(.8 , .8 , .8 ))
directionalLight (hpr = hpr(0,0,pi), color =color(.8,.9,.9) )
launchCamera("medevil")
rectangle(p3(-10000,-10000,0), p3(10000,-10000,0), p3(-10000,10000, 0), color = Color(.3,.3,0))
sphere(size = -10000, color = Color(.6,.7,.8),texture = "eveningsky.png" )

castle(position= p3(50,50,0), size = 100)

tower(position = p3(150,50,0), size = 200)
tower(position = p3(-50,50,0), size= 200)


castle(position= p3(-1050,1050,0), size = 50)

tower(position = p3(-1150,-1050,0), size = 200)
tower(position = p3(1050,-1050,0), size= 200)

for i in range(10):
    hut1(position = p3(922*cos(i), 1017*sin(i*13), 0), size = 50)
for i in range(10):
    hut2(position = p3(737*cos(i), 69*sin(i*13), 0), size = 50)
for i in range(10):
    building(position = p3(513*cos(i), 713*sin(i*13), 0), size = 50)
for i in range(10):
    turret(position = p3(913*cos(i), 313*sin(i*13), 0), size = 50)
for i in range(60):
    if i <= 20:
        wall (position = p3(i*210,0,0)+p3(-1650,-1600,0),size= 200, color = Color(.3,.3,.4), kind = "walls")
    if  i > 20 and i <= 40:
        wall(position= p3(-1850,-5850,0)+p3(0,i*210,0), hpr=hpr(pi/2,0,0),size= 200, color = Color(.3,.3,.4), kind = "walls")
    elif i >40:
        wall(position= p3(2725,-10000,0)+p3(0,i*210,0), hpr=hpr(pi/2,0,0),size= 200, color = Color(.3,.3,.4), kind = "walls")
for i in range(2):
    wall (position = p3(i*210,0,0)+p3(-450,-600,0),size= 200, color = Color(.3,.3,.4), kind = "walls")
for i in range(2):
    wall (position = p3(i*210,0,0)+p3(250,-600,0),size= 200, color = Color(.3,.3,.4), kind = "walls")
gallows(position= p3(0,-150,0), size = 50)
for i in range(4):
    catapult(position = p3(200+ i*200, -800, 0), hpr = hpr(3*pi/2, 0, 0),size = 75)
for i in range(4):
    catapult(position = p3(-100-i*200, -800, 0), hpr = hpr(3*pi/2, 0, 0),size = 75)

smith(position= p3(100,1000,0), size = 100)
fireish (position = p3(115,990,12), size = 6)
b = step (time)

for i in range(500) :
    j = i%60
    if j == 0:
        y = -8000 -i * 10
    v = p3 (0,integral(10),0)
    panda(position = p3(-2600+j*100,y,0  )+v, size = 25, hpr = hpr(pi, 0,0))
    gun(position = p3(-2600+j*100,y,5  )+v, size = 25, hpr = hpr(pi, 0,0),kind ="army")

for i in range(20):
    fireish(position = p3(i*210,0,0)+p3(-1650,-1650,0), size = 25)
for i in range(20):
        spear(position = p3(i*210-1650,-1800,0), size = 25, hpr = hpr(pi, 0,0))
for i in range(20):
        sword(position = p3(i*210-1650,-1850,0), size = 25, hpr = hpr(pi, 0,0))
for i in range(20):
        axe(position = p3(i*210-1650,-1900,0), size = 25, hpr = hpr(pi, 0,0))
for i in range(20):
        mace(position = p3(i*210-1650,-2000,0), size = 25, hpr = hpr(pi, 0,0))
#def fireGuns(m,v):
    #for a in army.allModels():
        #g = p3(0,0,integral(5))
        #v = p3(0,integral(8),0)+g
        #blimp(position =a.position + v, size = 25, collection = amo)
#def exitGuns(m,v):
    #for b in amo.allModels():
        #b.exit

#a = alarm(step =2)
#react(a , fireGuns)
#react(hit(amo.allModels(), walls.allModels()), exitGuns)




start()