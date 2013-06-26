from Panda import *

camera.position = p3(0,-100, 0)

head = soccerBall(size = .5)

head.dir = hold(p3(0,0,1), key("upArrow", p3(0,0,1)) + key("downArrow", p3(0,0,-1)) + \
                      key("leftArrow", p3(-1,0,0)) + key("rightArrow", p3(1,0,0)))

a = alarm(.2)
head.length = static(3)


def moveHead(m, v):
    d = now(head.dir)
    loc = now(head.position)
    sphere(position =  loc, size = .45, color = color(random01(), random01(), random01()), duration = head.length, kind = "tail")
    head.position = loc + d


react(a, moveHead)

def eat(m, v):
    exit(v)
    head.length = head.length + 1
    print head.length
    volleyBall(position = p3(randomInt(-40,40),0,randomInt(-40,40)), kind="food", size = .45)

def die(m, v):
    resetWorld()
    text(head.length)

food = volleyBall(position = p3(5,0,5), kind="food", size = .45)
reactAll(hit(head, "tail"), die)
reactAll(hit(head, "food"), eat)
start()
