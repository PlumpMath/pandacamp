from Panda import*
from ourModels import*

sphere(size = -10000,texture = "SPACE6.jpg")
launchCamera("spaceAdventure")

al = ambientLight(color = white)
dl = directionalLight(color = white, hpr = HPR(-5,0,-5) )

vel1 = P3(-5*cos(time)*cos(time), 5*-sin(time), 0)
s1 = space4(position = P3(0,100,0), size = .9, hpr = HPR(time/10, 0, 0))
a1 = alien(position = s1.position + P3(0,0,.8), size = .6)
#pointLight(position = P3(0,5,-5), color = white)

tardis(position = P3(40,50,4), hpr = HPR(time, 0, 0), size = 3)
s2 = space5(position = P3(-40, 50, -3))
#dropOff(position = s2.position + P3(0,0,.5))
spaceship(position= P3(0,20,.5),hpr=HPR(time,0,0))
s = spaceship()
hprs = HPR(pi/2, 0, 0)
v = P3(-25*sin(3),0,0)
s.position = P3(40,100,0)+ integral(v)
s.hpr = hprs
a = alien(position = P3(-.1,0,.5+cos(time)/40) + s.position, size = .2, hpr = hprs + HPR(pi,0,0))

def blowUp(m, v):
    play("explosion1.wav")
    s1.exit()
    s.exit()
    a1.exit()
    a.exit()
    fireish(position = s1.position, duration = .5)
s.react(hit(s,s1), blowUp)

#a.position = P3(0,0,abs(sin(5)))

for i in range(100):
    space4(size = randomRange(2,.5), position = P3(randomRange(100,-100), randomRange(100,-100), randomRange(100,-100)), hpr = HPR(randomRange(time,-time), randomRange(time,-time), randomRange(time,-time)))
    space5(size = randomRange(2,.5), position = P3(randomRange(100,-100), randomRange(100,-100), randomRange(100,-100)), hpr = HPR(randomRange(time,-time), randomRange(time,-time), randomRange(time,-time)))

for i in range(100):
    space4(size = randomRange(2,.5), position = P3(randomRange(-70,-20), randomRange(20,-20), randomRange(-10,10)), hpr = HPR(randomRange(time,-time), randomRange(time,-time), randomRange(time,-time)))
    space5(size = randomRange(2,.5), position = P3(randomRange(-70,-20), randomRange(20,-20), randomRange(-10,10)), hpr = HPR(randomRange(time,-time), randomRange(time,-time), randomRange(time,-time)))

for i in range(10):
    alien(size = randomRange(.5,1), position = P3(randomRange(-70,-20), randomRange(20,-20), randomRange(10,-10)), hpr = HPR(randomRange(time,-time), randomRange(time,-time), randomRange(time,-time)))


start()