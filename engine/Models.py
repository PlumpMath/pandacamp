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

# Characters/Creatures

def panda(**a):
    return modelHandle("panda-model.egg.pz", **a)

def girl(**a):
    return modelHandle("eve/eve.egg",**a)

def gorilla(**a):
    return modelHandle("gorilla/gorilla.egg", **a)

def bunny(**a):
    return modelHandle("bunny/bunny.egg", **a)

def balloonBoy(**a):
    return modelHandle("boyballoon/boymodel.egg", **a)

def r2d2(**a):
    return modelHandle("r2d2/r2d2.egg", **a)

def tails(**a):
    return modelHandle("tails/tails.egg", **a)

def penguin(**a):
    return modelHandle("Penguin/Penguin.egg", **a)

def ralph(**a):
    return modelHandle("Ralph/ralph.egg",**a )

def bee (**a):
    return modelHandle("Bee/Bee.egg", **a)

def chicken (**a):
    return modelHandle("Chicken2/Chicken2.egg", **a)

def dragon (**a):
    return modelHandle("dragon3/dragon3.egg", **a)

# Objects and Shapes

def sphere(**a):
    return modelHandle("sphere/sphere.egg", **a)

def soccerBall(**a):#This one needs some atttention
    return modelHandle("soccerball/soccerball.egg", **a)

def chair(**a):
    return modelHandle("deskChair/deskchair.egg",**a)

def stretcher(**a):
    return modelHandle("stretcher/strecher.egg",**a)

def russianBuilding(**a):
    return modelHandle("russianBuilding/tetris-building.egg", **a)

def volleyBall(**a):
    return modelHandle("volleyBall/volleyball.egg", **a)

def stoplightSign(**a):
    return modelHandle("stoplight_sign/stoplight_sign.egg", **a)

def slipperyRoadSign(**a):
    return modelHandle("slipperySign/slipperySign.egg", **a)

def bowlingPins(**a):
    return modelHandle ("bowlingpins/bowlingpins.egg", **a)



# Jointed Models


#vehicals
def truck(**a):
    return modelHandle("truck/cartruck.egg", **a)

def ford(**a):
    return modelHandle("fordCar/ford.egg", **a)

def jeep(**a):
    return modelHandle("jeep/jeep.egg", **a)

def boeing707(**a):
    return modelHandle("boeing707/boeing707.egg", **a)


def hangGlider(**a):
    return modelHandle("hangglider/hang-glider-1.egg", **a)


#Scenary
def discoHall(**a):  # Seems broken - no local size?
    return modelHandle("discohall/disco_hall.egg", **a)

def grassScene(**a):
    return modelHandle("environment.egg.pz", **a)

def trainEngineScene(**a):
   return modelHandle("trainengine/trainengine.egg",**a)

def forestSky(**a):
    return modelHandle("forestSky/forestsky.egg", **a)

def farmSky(**a):
    return modelHandle("farmSky/farmsky.egg", **a)
'''
#jointed models


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



 #Vehicles
#def crudeplane(**a):#Have not tested - Matt
#    return modelHandle("crude_plane.egg", name = "Crudeplane",
#                    localSize = 2, **a)




def spaceship(**a):
    return modelHandle("alice-scifi--fighter/fighter.egg", name="Spaceship",
    localSize = 0.0477077047052, localPosition = P3(   0.00,    0.11,    0.00),
    localOrientation = HPR(   3.14,    0.00,    0.00), cRadius = 0.807017505169,
    cFloor = -0.157894611359, cTop = 0.228070497513, cType = 'cyl',
    **a)


def sunset(**a):
    return modelHandle("sunset/sunset.egg", name = "Sunset",
                        **a)

#def celestial(**a):   # Seems broken?
#    return modelHandle("celestial/celestial.egg", name = "Celestial",
#                        localSize = .016, **a)'''


