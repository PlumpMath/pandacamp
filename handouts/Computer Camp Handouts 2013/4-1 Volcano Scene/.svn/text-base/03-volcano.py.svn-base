from Panda import *

def volcano(m, v):
        p = panda(size = .2)
        launch(p, P3(2,0,0), P3(1,0,2))
        p.when(getZ(p.position) < -2, exitScene)

c = alarm(step = .1)
react(c, volcano)
start()


