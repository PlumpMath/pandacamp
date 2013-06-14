from Panda import *

world.color = black
camera.position = p3(0,-20,time/10-3)
fireWorks(position = p3(0,0,-.7))

def volcano(m, v):
    for i in range(5):
        phpr = hpr(randomRange(0,2*pi), randomRange(-pi/2,-pi/8),0)
        v = hprToP3(phpr)*3
        m = randomChoice([sphere, panda])
        p = m(size = randomRange(.05,.2), color = color(randomRange(0,1),randomRange(0,1),randomRange(0,1)))
        launch(p, p3(0,0,1), v)
        p.when(getZ(p.position) < -2, exitScene)

al = ambientLight(color = color(.5,.5,.5))
dl = directionalLight(hpr = hpr(0,-1,0) )




def h(t):
    return p3c(cos(t/4)+1,2*t,t/10-2)

def n(m,v):
    sphere(position = h(localTime), size = .09, color = color(randomRange(0,1),randomRange(0,1),randomRange(0,1)))

c = alarm(step = 2)

react(c, n)

start()


