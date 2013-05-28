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

#pandas
def panda(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle(fileName = "panda-model.egg.pz", name = 'Panda',
                       localSize = 0.00178, localPosition = P3( 0, 0.21, 0), localOrientation = HPR(0, 0, 0),
                       cRadius = 1.0, cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)

#jointed models
def ralph(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("Ralph/ralph.egg", name = 'Ralph',
                       localSize = .18, 
                       cRadius = 0.2,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl',
                       joints = [('neck', 'Neck'), ('leftWrist', 'LeftWrist'),
                                 ('rightWrist', 'RightWrist'),
                                 ('jaw', 'Jaw'), ('leftElbow', 'LeftElbow'),
                                 ('rightShoulder', 'RightShoulder'), ('leftShoulder', 'LeftShoulder'), ('leftKnee', 'LeftKnee'),
                                 ('rightKnee', 'RightKnee')], animations = {"walk" : g.pandaPath + "/models/Ralph/ralph-walk.egg"}, 
                                 defaultAnimation = "walk", frame = 4,  **a )

def sonic(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("sonic/sonic.egg", name = "Sonic",
                       localSize = 0.036,  localOrientation = HPR(0,   0.66-1.27,   0.00), 
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
                                 ('leftAnkle', 'LeftAnkle'), ('rightAnkle', 'RightAnkle'), ], animations = {"walk" : g.pandaPath + "/models/sonic/sonic-run.egg"}, 
                                 defaultAnimation = "walk", frame = 11, **a)


def bender(**a):
    return modelHandle("customModels/Bender2.egg", name="Bender",
                        localSize = 0.173130127862,
                        joints = [('Head',"Head"),('Neck',"Neck"),('Main',"Main"),
                                  ('Arm_L',"Arm.L"),('Arm_R',"Arm.R"),('Leg_L',"Leg.L"),
                                  ('Leg_R',"Leg.R"),('Shoulder_R',"Shoulder.R"),('Shoulder_L',"Shoulder.L"),
                                  ('Hip_R',"Hip.R"),('Hip_L',"Hip.L")],
                        **a)



def testModel(**a):
    return modelHandle("customModels/test.egg", name="testModel",
    localSize = 0.141613497853,
    joints = [('Main','Main'),('Limb','Limb')],
    **a)

def sphere(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("sphere/sphere.egg", name = 'Sphere', localSize = .31, cRadius = 1, cFloor = -1, cTop = 1, cType = 'sphere', **a)


def soccerBall(**a):#Works as of 6-23-08 ~ Kendric
    return sphere(texture = "soccer.jpg", **a)


def volleyBall(**a):#Works as of 6-23-08 ~ Kendric
    #Formerly volleyBall. -Alexandra
    return modelHandle("volleyBall/volleyball.egg", name = "VolleyBall",
                        cRadius = 1, cFloor = -1, cTop = 1, cType = 'sphere',
                    localSize = 1.8, **a)



def stretcher(**a):
    return modelHandle("stretcher/strecher.egg",
                       name = "Stretcher", localSize = 0.018, localPosition = P3(  -0.04,    0.02,    0.69), localOrientation = HPR(  -3.14,    0.00,    0.00),\
                       cRadius = 0.93, cFloor = 0.0, cTop = 0.93, cType = 'cyl',
                        **a)

def chair(**a):
    #Formerly deskChair. -Alexandra
    return modelHandle("deskChair/deskchair.egg", name = "DeskChair",
                       localSize = 0.0012, localPosition = P3(0.03,0, 0.46), localOrientation = HPR(   3.14,    0.00,    0.00),
                       cRadius = 0.36, cFloor = 0.0, cTop = 1.0, cType = 'cyl'
                       **a)


#characters/Creatures

def gorilla(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("gorilla/gorilla.egg", name = "Gorilla",
                       localSize = 0.134071993101, localPosition = P3(   0.00,    0.19,    0.00),
                       localOrientation = HPR(   0.00,    0.00,    0.00),cRadius = 0.570175409317,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)

def bunny(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("bunny/bunny.egg", name = "Bunny",
                       localSize = 0.241066308596, localPosition = P3(   0.00,    0.04,    0.00),
                       localOrientation = HPR(   0.00,    0.00,    0.00), cRadius = 0.333333313465,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)

def boyBalloon(**a):#Works as of 6-23-08 ~ Kendric - terrifying
    return modelHandle("boyballoon/boymodel.egg",name = "Boy",
                localSize = 0.0043, localPosition = P3(  -0.28,    0.00,    0.49), \
                localOrientation = HPR(   0.06,    0.00,    0.06), cRadius = 0.41, cFloor = 0.0, cTop = 1.0, cType = 'cyl'
                       **a)


def r2d2(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("r2d2/r2d2.egg", name = "R2d2",
                       localSize = .4, localOrientation = HPR(-3.09,0,0),localPosition = P3(   0.00,   -0.11,    0.00),\
                           cRadius = 0.403508931398, cType = 'cyl', 
                        **a)

def girl(**a):
    #Formerly eve. -Alexandra
    return modelHandle("eve/eve.egg", name = "Eve",
                       localSize = 0.217174404282, localPosition = P3(   0.00,    0.00,    0.00),
                       localOrientation = HPR(   0.00,    0.00,    0.00), cRadius = 0.26315793395,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl',**a)

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
                       localSize = 0.0410595140695, localPosition = P3(   0.02,   -0.04,    0.00),
                       localOrientation = HPR(   0.00,    0.00,    0.00), cRadius = 0.473684489727,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)



 #Vehicles
#def crudeplane(**a):#Have not tested - Matt
#    return modelHandle("crude_plane.egg", name = "Crudeplane",
#                    localSize = 2, **a)

def truck(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("truck/cartruck.egg", name = "Truck",
                    localSize = 0.29258979374, localPosition = P3(   0.00,    0.11,    0.00),
                    localOrientation = HPR(   0.00,    0.00,    0.00), cRadius = 0.64912289381,
                    cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)

def ford(**a):#Works as of 6-23-08 ~ Kendric - has error message, but seems to work fine regardless.
    #Formerly fordCar. -Alexandra
    return modelHandle("fordCar/ford.egg", name = "FordCar",
                      localSize = 0.116412728843, localPosition = P3(   0.32,   -0.56,    0.00),
                      localOrientation = HPR(   0.00,    0.00,    0.00), cRadius = 0.798245787621,
                      cFloor = 0.0, cTop = 1.0, cType = 'cyl',**a)

def jeep(**a):#Works as of 6-23-08 ~ Kendric
    #Error about window texture, but works. -Alexandra
    return modelHandle("jeep/jeep.egg", name = "Jeep",
                       localSize = 0.0884279838097, localPosition = P3(   0.02,    0.02,    0.00),
                       localOrientation = HPR(   0.00,    0.00,    0.00),cRadius = 0.745614230633,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)

def boeing707(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("boeing707/boeing707.egg",name = "Boeing707", 
                        localSize = 0.0179508233691, localPosition = P3(   0.02,    0.02,    0.00),
                        localOrientation = HPR(  -3.14,    0.00,    0.00),cRadius = 0.719298481941,
                        cFloor = 0.0, cTop = .3, cType = 'cyl',**a)
                       
def blimp(**a):
    return modelHandle("alice-vehicles--blimp/blimp.egg", name="Blimp",
    localSize = 0.0129979178232, localPosition = P3(   0.00,    0.00,    0.00),
    localOrientation = HPR(  -3.14,    0.00,    0.00), cRadius = 0.903508841991,
    cFloor = 0.0, cTop = 1.0, cType = 'sphere',
    **a)

def spaceship(**a):
    return modelHandle("alice-scifi--fighter/fighter.egg", name="Spaceship",
    localSize = 0.0477077047052, localPosition = P3(   0.00,    0.11,    0.00),
    localOrientation = HPR(   3.14,    0.00,    0.00), cRadius = 0.807017505169,
    cFloor = -0.157894611359, cTop = 0.228070497513, cType = 'cyl',
    **a)

def hangGlider(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("hangglider/hang-glider-1.egg",name = "Hangglider",
                       localSize = 0.0563841689036, localPosition = P3(   0.02,    0.11,    0.00),
                       localOrientation = HPR(  -0.00,    0.00,    0.00), cRadius = 0.719298481941,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl',**a)


#Buildings/Scenery
def russianBuilding(**a):
    #Formerly russianBuilding. -Alexandra
    return modelHandle("russianBuilding/tetris-building.egg",name = "RussianBuilding",
                       localSize = 0.0783410083641, localPosition = P3(  -0.02,    0.04,    0.00),
                       localOrientation = HPR(  -0.00,    0.00,    0.00), cRadius = 0.491228342056,
                       cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)

def discoHall(**a):  # Seems broken - no local size?
    return modelHandle("discohall/disco_hall.egg", name = 'Disco Hall',
                        localSize = 0.0172880796686, localPosition = P3(  -0.25,   -0.02,    0.00),
                        localOrientation = HPR(  -3.14,    0.00,    0.00),cRadius = 0.710526585579,
                        cFloor = 0.0, cTop = 1.0, cType = 'cyl', **a)

def grassScene(**a):#Works as of 6-23-08 ~ Kendric
    return modelHandle("environment.egg.pz", name = 'Environment', **a)


def trainEngineScene(**a):#Works as of 6-23-08 ~ Kendric
   return modelHandle("trainengine/trainengine.egg",name = "Trainengine",
                        localSize = 0.1, localPosition = P3(   0.00,    0.80,    0.00),
                        localOrientation = HPR(  -3.14,    0.00,    0.00), cRadius = 0.780701935291,
                        cFloor = 0.0, cTop = 1.0, cType = 'cyl',**a)

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