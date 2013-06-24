from Panda import *

# game music
#play("marioBrosTheme.mp3")

# create the vehicle
car = jeep(size = 0.25)

# create the racetrack
track = Racetrack("oval.txt", model = car)


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
    # vehicle movement variable
    # steering wheel angle
#    a = getX(mouse)


#    soundmove.play()

#    play("engine.mp3")
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
    speed = integral(forward - friction)*10
    # heading
    h = getH(hpr0) + integral(speed * model.angle)
    car.hpr = HPR(h,0,0)
    car.velocity = P3C(speed,h+pi/2,0)
    car.position = p0 + integral(car.velocity)
    car.when1(track.inWall(car), restartCar)

# drive reaction
def restartCar(model, var):
    play("explosion2.wav")
    driving(car, P3(4,4,0), HPR(pi/2, 0, 0))

driving(car, P3(4,4,0), HPR(pi/2, 0, 0))

start()
