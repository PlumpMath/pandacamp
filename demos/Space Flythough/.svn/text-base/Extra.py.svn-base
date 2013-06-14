from Panda import*
sphere(size = -10000, texture = "horizon.jpg" )
#scoring
score = var(0)
text(score)
speed = var(1)

#camera
camera.position = P3(0,-20,0)

#collection start
missles = collection()

#main object
p = panda()
p0 = P3(0,0,0)
vel = hold(p0, key('w', P3(0,0,2)) + key('s', P3(0,0,-2)) + key('d', P3(2,0,0)) + key('a', P3(-2,0,0)) + key('space', P3(0,0,0)))
p.position = p0 + integral(vel)

#actions
def shootBall(m, v):
    soccerBall(size = .1, position = now(p.position) + integral(P3(0,0,3)), duration = 2, collection = missles)
def destruct(m, pairs):
    for (m, ball) in pairs:
        m.exit()
        ball.exit()
        score.add(1)
def blowUp(m, v):
    m.exit()
    resetWorld()
    text("OOOoooOoOoOoh You got pwned!!!!!!", color = purple, size = 3, position = P3(0,0,0))
def randomBunny(m,v):
    b = bunny(position = P3(random11()*3, 0, 5-localTime), size = .3, duration = 9.1)
    p.react(hit(p,b), blowUp)
    p.react(hit(b, missles), destruct)

#reactions    
c = alarm(step = 1.5)
react(c, randomBunny)
    
p.react(lbp, shootBall)

start()
