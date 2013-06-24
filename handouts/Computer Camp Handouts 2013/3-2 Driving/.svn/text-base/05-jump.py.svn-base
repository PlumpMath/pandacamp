from Panda import *

# game music
#play("marioBrosTheme.mp3")

# create the vehicle
car = jeep(size = 0.25)
text(car.position)
# create the racetrack
track = Racetrack("oval.txt", model = car)


# set camera
camera.flatrod(car, distance = 2)

# force constant
fK = 2
# friction constant
fcK = 0.5
# centripetal force threshold
thresh = 10
# velocity variable
setType(car.velocity, P3Type)
setType(car.angle, numType)


# driving state
def driving(model, p0, hpr0, speed0):
    a1 = hold(0, key("arrow_right",  1) + keyUp("arrow_right",  0))
    a2 = hold(0, key("arrow_left",  -1) + keyUp("arrow_left",  0))
    a3 = hold(0, key("arrow_up",  -1) + keyUp("arrow_up",  0))
    a4 = hold(0, key("arrow_down",  1) + keyUp("arrow_down",  0))
    delta = a1 + a2
    dspeed = a3 + a4

    decay = -1.95*model.angle
    model.angle = integral(delta + decay)

    # the force on the vehicle
    forward = fK * integral(dspeed)
    # velocity
    fvelocity = abs(car.velocity)*abs(car.velocity)
    # friction on vehicle
    # get friction from track
    pushBack = track.friction(car.position)
    friction = -pushBack * fvelocity
    # speed
    speed = speed0 + integral(forward - friction)*10
    # heading
    h = getH(hpr0) + integral(speed * model.angle)
    car.hpr = HPR(h,0,0)
    car.velocity = P3C(speed,h+pi/2,0)
    car.position = p0 + integral(car.velocity)


# drive reaction
def restartCar(model, var):
    play("explosion2.wav")
    driving(car, P3(4,4,0), HPR(pi/2, 0, 0), 0)



def chp(hpr):
    return HPR(getH(hpr), -getP(hpr), getR(hpr))
def jump(model, var):
    p0 = now(model.position)
    v0 = now(model.velocity)
    hpr0 = now(model.hpr)
    
    model.velocity = P3(getX(v0), getY(v0), .5) + integral(P3(0,0,-1))
    model.position = p0 + integral(model.velocity)
    
    model.hpr = chp(P3toHPR(deriv(model.position, HPRtoP3(hpr0))))
    
    model.when1(getZ(model.position)<0, drive)

def drive(model, var):
    p0 = now(model.position)
    hpr0 = now(model.hpr)
    v0 = now(model.velocity)
    driving(model, P3(getX(p0), getY(p0), 0), HPR(getH(hpr0), 0, 0), -abs(v0))

car.when(track.inWall(car), restartCar)
car.react(lbp, jump)
driving(car, P3(4,4,0), HPR(pi/2, 0, 0), 0)

start()