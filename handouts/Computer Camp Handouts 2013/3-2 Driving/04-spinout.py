from Panda import *

# game music
#play("marioBrosTheme.mp3")

# create the vehicle
car = jeep(size = 0.25)

# create the racetrack
track = Racetrack("oval.txt", model = car)

text(format("Centripital force: %f", abs(car.angle*abs(car.velocity)*abs(car.velocity))))
# set camera
camera.rod(car, distance = 2)

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
def driving(model, p0, hpr0):

    play("engine.mp3")
    a1 = hold(0, key("rightArrow",  1) + keyUp("rightArrow",  0))
    a2 = hold(0, key("leftArrow",  -1) + keyUp("leftArrow",  0))
    a3 = hold(0, key("upArrow",  -1) + keyUp("upArrow",  0))
    a4 = hold(0, key("downArrow",  1) + keyUp("downArrow",  0))
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
    speed = integral(forward - friction)*10
    # heading
    h = getH(hpr0) + integral(speed * model.angle)
    car.hpr = hpr(h,0,0)
    car.velocity = p3c(speed,h+pi/2,0)
    car.position = p0 + integral(car.velocity)
    when1(car, track.inWall(car), restartCar)
    # car.when1(abs(car.angle*abs(car.velocity)*abs(car.velocity)) > 5, spinout)
# drive reaction
def restartCar(model, var):
    play("explosion2.wav")
    driving(car, p3(4,4,0), hpr(pi/2, 0, 0))

def spinout(model, var):
    p0 = now(model.position)
    hpr0 = now(model.hpr)
    v0 = now(model.velocity)
    model.position = p0 + integral(v0 * (1 - localTime / 3))
    model.hpr = hpr0 + hpr(integral(20 * (1 - localTime / 3)),0,0)
    play("bad.mp3")
    # drive away
    react1(model,wait(3), restartCar)


driving(car, p3(4,4,0), hpr(pi/2, 0, 0))

start()

''