from Panda import *

camera.position = p3(0,0,100)
camera.hpr = hpr(0,-pi/2,0)

def createParticle(n):
    if n == 0:
        return panda(color = red)
    elif n == 1:
        return panda(color = yellow)
    elif n == 2:
        return panda(color = blue)
    else:
        return panda(color = white)

def createP(pos, vel, dir, n):
        m = createParticle(n)
        m.position = pos + integral(p3c(vel, dir-pi/2, 0))
        m.hpr=hpr(dir,0,0)
        def step():
            if random01() < .2 and n < 4:
                exit(m)
                here=now(m.position)
                createP(here, vel, dir + .5, n+1)
                createP(here, vel, dir - 0.5, n+1)
            else:
                wait(.1, step)
        wait(.1, step)        

createP(p3(0,0,0), 1, 0, 0)

start()


