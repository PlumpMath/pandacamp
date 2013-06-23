from Panda import *
from modelJean import *

world.color = black
camera.position = P3(0,-20,0) #time/10
#fireWorks(position = P3(0,0,-.7))

vol(size = .8, position = P3(0,0,-1.3))

def makePanda(pos, size):
    hprs = P3toHPR(P3(getX(pos),getY(pos),0))
    panda(position = P3(getX(pos),getY(pos),-4), size = size * 4, hpr = hprs)
    

def volcano(m, v):
    for i in range(5):
        hpr = HPR(randomRange(0,2*pi), randomRange(-pi/2,-pi/8),0)
        v = HPRtoP3(hpr)*5
        m = sphere
        p = m(size = randomRange(.05,.2), color = color(randomRange(0,1),randomRange(0,1),randomRange(0,1)),
              hpr = hpr)
        launch(p, P3(0,0,-.2), v)
        p.when1(getZ(p.position) < -2.5, spawnPanda)

#    pan = panda(position = P3(getX(v), getY(v), -4))
    #text(pan.position)
        
al = ambientLight(color = color(.5,.5,.5))
dl = directionalLight(hpr = HPR(0,-1,0) )

def spawnPanda(m, v):
    p = now(m.position)
    hpr = now(m.hpr)
    h = getH(hpr)
    c = now(m.color)
    m.exit()
    panda(position = p + integral(HPRtoP3(HPR(h, 0, 0))), hpr = HPR(h, 0, 0), duration = 2, color = c, size = .3)
c = alarm(step = .1)
react(c,volcano)

start()