import g

# This defines the models available to the students.  For each model, we have a size
# factor (localSize) that attempts to fit the model in the standard cube (-1,-1,-1) - (1,1,1).
# Each model also has a local offset to define the central point of rotation.  This is usually
# (0,0,0) but some models require a different center from the one in design space.
# Finally, a local orientation gives a default orientation.

# Every model corresponds to an egg file in models/panda-model (?).  The name in the model
# object is used for error messages.

# Models with joints need a list of joint names and animations

# Other parameters are passed into the modelHandle object

# modelHandle is defined in Handle.py

from Model import *
from pandac.PandaModules import Filename
import os, sys

#Reorganized the models -Matt
## Why is this pathname different???  -- jcp
#pandas
def panda(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle(fileName = "panda-model.egg.pz", name = 'Panda',
                       localSize = .002*.91, localPosition = P3(0,.21,0),
                       localOrientation = HPR(0,0,0), **a)

#jointed models
def ralph(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("Ralph/ralph.egg", name = 'Ralph',
                       localSize = .18,
                       joints = [('neck', 'Neck'), ('leftWrist', 'LeftWrist'),
                                 ('rightWrist', 'RightWrist'),
                                 ('jaw', 'Jaw'), ('leftElbow', 'LeftElbow'),
                                 ('rightShoulder', 'RightShoulder'), ('leftShoulder', 'LeftShoulder'), ('leftKnee', 'LeftKnee'),
                                 ('rightKnee', 'RightKnee')], animations = {"walk" : g.pandaPath + "/models/Ralph/ralph-walk.egg"}, frame = 4,  **a )

def sonic(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("sonic/sonic.egg", name = "Sonic",
                       localSize = 0.036,  localOrientation = HPR(0,   0.66,   0.00),
                       joints = [('neck', 'Neck'), ('leftEyeBrow', 'LeftEyeBrow'), ('rightEyeBrow', 'RightEyeBrow'),
                                 ('leftLowerSpike', 'LeftLowerSpike'), ('lowerRightSpike', 'LowerRightSpike'),
                                 ('topSpike', 'TopSpike'), ('leftMiddleSpike', 'LeftMiddleSpike'),
                                 ('rightMiddleSpike', 'RightMiddleSpike'), ('lowerSpike', 'LowerSpike'),
                                 ('jaw', 'Jaw'),
                                 ('leftShoulder', 'LeftShoulder'), ('rightShoulder', 'LeftShoulder1'),
                                 ('leftElbow', 'LeftElbow'), ('rightElbow', 'LeftElbow1'),
                                 ('leftWrist', 'LeftWrist'), ('rightWrist', 'LeftWrist1'),
                                 ('leftHip', 'LeftHip'), ('rightHip', 'RightHip'),
                                 ('leftKnee', 'LeftKnee'), ('rightKnee', 'RightKnee'),
                                 ('leftAnkle', 'LeftAnkle'), ('rightAnkle', 'RightAnkle'), ], animations = {"walk" : g.pandaPath + "/models/sonic/sonic-run.egg"}, frame = 11, **a)



def sphere(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("sphere/sphere.egg", name = 'Sphere', localSize = .25, **a)


def soccerBall(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("soccerBall/soccerBall.egg", name = "SoccerBall",
                    localSize = 1.86842024326, localPosition = P3(0.0, 0.0, -0.0877192616463), localOrientation = HPR(0.0, 0, 0), **a)


def volleyball(**a):#Works as of 6-23-08 ~ Kendric
    #Formerly volleyBall. -Alexandra
    return modelHandle("volleyBall/volleyball.egg", name = "VolleyBall",
                    localSize = 1.8, **a)



def stretcher(**a):
    return modelHandle("stretcher/strecher.egg",
                       name = "Stretcher", localPosition = P3(0, 0, -.648),
                       localSize = .0163, **a)

def chair(**a):
    #Formerly deskChair. -Alexandra
    return modelHandle("deskChair/deskchair.egg", name = "DeskChair",
                       localSize = .0011579, localPosition = P3(0, 0, -.455),
                       localOrientation = HPR(3.09, 0, 0), **a)


#characters/Creatures

def gorilla(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("gorilla/gorilla.egg", name = "Gorilla",
                       localSize = .123, localOrientation = HPR(0, -.05, 0),
                       localPosition = P3(0,0,0), **a)

def bunny(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("bunny/bunny.egg", name = "Bunny",
                       localSize = .195, **a)

def boyBalloon(**a):#Works as of 6-23-08 ~ Kendric - terrifying
    return modelHandle("boyballoon/boymodel.egg",
                       name = "Boy", localSize = .00145, localOrientation = HPR(0, 0, 0),
                       localPosition = P3(0, 0, -.17),
                       **a)


def r2d2(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("r2d2/r2d2.egg", name = "R2d2",
                       localSize = .38, localOrientation = HPR(-3.09,0,0),
                        **a)

def girl(**a):
    #Formerly eve. -Alexandra
    return modelHandle("eve/eve.egg", name = "Eve",
                       localSize = .1757, localPosition = P3(0, 0, -.043),
                        **a)

#def monster(**a):
#    return modelHandle(g.pandaPath + "/models/monster/monster1", name = "monster1",
#                       localSize = 0.3921, localPosition = P3(0, 0, 0),
#                       localOrientation = HPR(0, 0, 0),
#                       joints = [#('rootDummy', 'RootDummy'), ('root', 'Root'),
#                                 ('rightShoulder', 'R_Shoulder'), ('rightElbow', 'R_Elbow'),
#                                 ('rightWrist', 'R_Wrist'), ('rightClaw', 'R_Claw'),
#                                 ('leftShoulder', 'L_Shoulder'), ('leftElbow', 'L_Elbow'),
#                                 ('leftWrist', 'L_Wrist'), ('leftClaw', 'L_Claw'),
##                                 ('effector1', 'effector1'), ('effector2', 'effector2'), ('effector3', 'effector3'),
##                                 ('effector4', 'effector4'),('effector5', 'effector5'), ('effector6', 'effector6'),
#                                 ('lidRoot', 'LidRoot'), ('lid', 'Lid'),
#                                 ('tentacle1Root', 'Tentacle1_Root'), ('tentacle1Mid', 'Tentacle1_Mid'), ('tentacle1Tip', 'Tentacle1_Tip'),
#                                 ('tentacle2Root', 'Tentacle2_Root'), ('tentacle2Mid', 'Tentacle2_Mid'), ('tentacle2Tip', 'Tentacle2_Tip'),
#                                 ('tentacle3Root', 'Tentacle3_Root'), ('tentacle3Mid', 'Tentacle3_Mid'), ('tentacle3Tip', 'Tentacle3_Tip'),
#                                 ('tentacle4Root', 'Tentacle4_Root'), ('tentacle4Mid', 'Tentacle4_Mid'), ('tentacle4Tip', 'Tentacle4_Tip'),
##                                 ('nurbsCircle1', 'nurbsCircle1'), ('nurbsCircle2', 'nurbsCircle2'), ('nurbsCircle3', 'nurbsCircle3'),
##                                 ('nurbsCircle4', 'nurbsCircle4'), ('nurbsCircle5', 'nurbsCircle5'), ('nurbsCircle6', 'nurbsCircle6')
#                                 ],
#                                 animations = {"explode" : g.pandaPath + "/models/monster/monster1-explode.egg"}, frame = 3, **a)

def tails(**a):
    return modelHandle("tails/tails.egg", name = "tails",
                       localSize = 0.03368, localPosition = P3(0, 0, -.07),
                       localOrientation = HPR(-3.14159, 0, 0), **a)



 #Vehicles
#def crudeplane(**a):#Have not tested - Matt
#    return modelHandle("crude_plane.egg", name = "Crudeplane",
#                    localSize = 2, **a)

def truck(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("truck/cartruck.egg", name = "Truck",
                    localPosition = P3(0, 0, -.01), localSize = .44, **a)

def ford(**a):#Works as of 6-23-08 ~ Kendric - has error message, but seems to work fine regardless.
    #Formerly fordCar. -Alexandra
    return modelHandle("fordCar/ford.egg", name = "FordCar",
                      localSize = .14, localPosition = P3(.38, -.63, 0),
                      localOrientation = HPR(0, 0, 0),
                      **a)

def jeep(**a):#Works as of 6-23-08 ~ Kendric
    #Error about window texture, but works. -Alexandra
    return modelHandle("jeep/jeep.egg", name = "Jeep",
                       localSize = .1, **a)

def boeing707(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("boeing707/boeing707.egg",
                       name = "Boeing707", localSize = .02, localOrientation = HPR(3.14159, 0, 0),
                       localPosition = P3(0, 0, 0),
                       **a)

def hangGlider(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("hangglider/hang-glider-1.egg",
                       name = "Hangglider",
                       localPosition = P3(0, 0, 0.175), localOrientation = HPR(0, 3.14159, 3.14159),
                       localSize = .0654,
                       **a)


#Buildings/Scenery
def russianBuilding(**a):
    #Formerly russianBuilding. -Alexandra
    return modelHandle("russianBuilding/tetris-building.egg",
                       name = "RussianBuilding",localSize = .074, **a)

def discoHall(**a):  # Seems broken - no local size?
    return modelHandle("discohall/disco_hall.egg", name = 'Disco Hall', **a)

def grassScene(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("environment.egg.pz", name = 'Environment', **a)

# Not a scene and needs to be sized correctly
#def trainEngineScene(**a):#Works as of 6-23-08 ~ Kendric
#    return modelHandle("trainengine/trainengine.egg",
#                       name = "Trainengine",
#                       localPosition = P3(.7, 0, 0),
#                       **a)

def forestSky(**a):#Works as of 6-23-08 ~ Kendric - I think.  Looks cool.
    return modelHandle("forestSky/forestsky.egg", name = "ForestSky",
                        **a)

def farmSky(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("farmSky/farmsky.egg", name = "FarmSky",
                        **a)

def sunset(**a):
    return modelHandle("sunset/sunset.egg", name = "Sunset",
                        **a)

#def celestial(**a):   # Seems broken?
#    return modelHandle("celestial/celestial.egg", name = "Celestial",
#                        localSize = .016, **a)