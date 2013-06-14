
from modelsMedevil import*
al = ambientLight(color = color(.8 , .8 , .8 ))
directionalLight (hpr = HPR(0,0,pi), color =color(.8,.9,.9) )
launchCamera("medevil")
rectangle(P3(-10000,-10000,0), P3(10000,-10000,0), P3(-10000,10000, 0), color = Color(.3,.3,0))
sphere(size = -10000, color = Color(.6,.7,.8))

castle(position= P3(50,50,0), size = 100)

tower(position = P3(150,50,0), size = 200)
tower(position = P3(-50,50,0), size= 200)


castle(position= P3(-1050,1050,0), size = 50)

tower(position = P3(-1150,-1050,0), size = 200)
tower(position = P3(1050,-1050,0), size= 200)

army = collection()
amo = collection()
walls = collection()
for i in range(10):
    hut1(position = P3(922*cos(i), 1017*sin(i*13), 0), size = 50)
for i in range(10):
    hut2(position = P3(737*cos(i), 69*sin(i*13), 0), size = 50)
for i in range(10):
    building(position = P3(513*cos(i), 713*sin(i*13), 0), size = 50)
for i in range(10):
    turret(position = P3(913*cos(i), 313*sin(i*13), 0), size = 50)
for i in range(60):
    if i <= 20:
        wall (position = P3(i*210,0,0)+P3(-1650,-1600,0),size= 200, color = Color(.3,.3,.4), collection = walls)
    if  i > 20 and i <= 40:
        wall(position= P3(-1850,-5850,0)+P3(0,i*210,0), hpr=HPR(pi/2,0,0),size= 200, color = Color(.3,.3,.4), collection = walls)
    elif i >40:
        wall(position= P3(2725,-10000,0)+P3(0,i*210,0), hpr=HPR(pi/2,0,0),size= 200, color = Color(.3,.3,.4), collection = walls)
for i in range(2):
    wall (position = P3(i*210,0,0)+P3(-450,-600,0),size= 200, color = Color(.3,.3,.4), collection = walls)
for i in range(2):
    wall (position = P3(i*210,0,0)+P3(250,-600,0),size= 200, color = Color(.3,.3,.4), collection = walls)
gallows(position= P3(0,-150,0), size = 50)
for i in range(4):
    catapult(position = P3(200+ i*200, -800, 0), hpr = HPR(3*pi/2, 0, 0),size = 75)
for i in range(4):
    catapult(position = P3(-100-i*200, -800, 0), hpr = HPR(3*pi/2, 0, 0),size = 75)

smith(position= P3(100,1000,0), size = 100)
fireish (position = P3(115,990,12), size = 6)
b = step (time)

for i in range(500) :
    j = i%60
    if j == 0:
        y = -8000 -i * 10
    v = P3 (0,integral(10),0)  
    panda(position = P3(-2600+j*100,y,0  )+v, size = 25, hpr = HPR(pi, 0,0))
    gun(position = P3(-2600+j*100,y,5  )+v, size = 25, hpr = HPR(pi, 0,0),collection = army)

for i in range(20):
    fireish(position = P3(i*210,0,0)+P3(-1650,-1650,0), size = 25)
for i in range(20):
        spear(position = P3(i*210-1650,-1800,0), size = 25, hpr = HPR(pi, 0,0))
for i in range(20):
        sword(position = P3(i*210-1650,-1850,0), size = 25, hpr = HPR(pi, 0,0))
for i in range(20):
        axe(position = P3(i*210-1650,-1900,0), size = 25, hpr = HPR(pi, 0,0))
for i in range(20):
        mace(position = P3(i*210-1650,-2000,0), size = 25, hpr = HPR(pi, 0,0))
#def fireGuns(m,v):
    #for a in army.allModels():
        #g = P3(0,0,integral(5))
        #v = P3(0,integral(8),0)+g
        #blimp(position =a.position + v, size = 25, collection = amo)
#def exitGuns(m,v):
    #for b in amo.allModels():
        #b.exit
    
#a = alarm(step =2)
#react(a , fireGuns)
#react(hit(amo.allModels(), walls.allModels()), exitGuns)
 



start() 