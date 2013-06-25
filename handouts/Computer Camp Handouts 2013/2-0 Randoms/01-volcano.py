from Panda import *

def volcano(m, v):
        p = panda(size = .2)
        launch(p, p3(0,0,1), p3(1,0,2), p3(0,0,-3))
        when(p, getZ(p.position) < -2, exitScene)

c = alarm(step = .1)
react(c, volcano)

start()


