from Panda import *

c = alarm(step = .5)

def launch(m, v):
    p = panda(position = p3c(sin(time*3), localTime, localTime))
    pointForward(p)

react(c, launch)
camera.position = p3(0, -15, 5)

grassScene()
start()
