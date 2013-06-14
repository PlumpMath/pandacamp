from Panda import *

rectangle(P3(-4,0,-3), P3(4,0,-3), P3(-4,0,3), texture = "Clouds2.jpg")
text(time, size = 1.7, color = white)

al = ambientLight(color = color(.5,.5,.5))
dl = directionalLight(hpr = HPR(0,-1,0) )

p = panda(hpr = HPR(pi*.5,0,0), size = .4, color = color(.5,.5,sin(time)))

v = hold(P3(0,0,0), key("arrow_up", P3(0,0,1.5))+key("arrow_down", P3(0,0,-1.5))+key("arrow_left", P3(-1.5,0,0))+key("arrow_right", P3(1.5,0,0)) +
                    happen(getX(p.position) < -3, P3(1,0, 0))  + happen(getX(p.position) > 3, P3(-1, 0, 0))+ happen(getZ(p.position)> 2.4, P3(0,0,-1))+ happen(getZ(p.position)<-2.4, P3(0,0,1)))
p.position = P3(0,-.8,0)+integral(v)



def endGame(m, v):
    m.exit()
    p.exit()
    text(format("Fly free! Your score: %i seconds", now(time)), size = 3, position = P3(0,0,0), color = blue)

def randomBall(m, v):
    s = sphere(position = P3(4-localTime, -.8, randomRange(-2.5,2.5)), size = randomRange(.05,.2), duration = 8, color = color(randomRange(.8,1),randomRange(.8,1),randomRange(.8,1)))
    s.react(hit(s,p), endGame)

a = alarm(step = .5)
react(a, randomBall)

start()