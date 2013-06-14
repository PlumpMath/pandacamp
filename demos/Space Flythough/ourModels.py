import g
from pandac.PandaModules import Filename
import os, sys
from Model import *

def space4(**a):
    return modelHandle(fileName = "space4/space4.egg", **a)

def space5(**a):
    return modelHandle(fileName = "space5/space5.egg", **a)

#def dropOff(**a):
    #return modelHandle(fileName = "dropOff/dropOff.egg", name = "dropOff",
                        #localSize = 0.00320221339435, localPosition = P3(   0.00,    0.12,    0.07),
                        #localOrientation = HPR(  -0.00,   -0.06,    0.00), cRadius = 1.0, cFloor = 0.0,
                        #cTop = 1.0, cType = 'cyl', **a)

def tardis(**a):
    return modelHandle(fileName = "tardis/Tardis.egg", **a)

def alien(**a):
    return modelHandle(fileName = "Alien1/Alien1.egg", **a)

def spaceship(**a):
    return modelHandle(fileName = "spaceship/spaceship.egg", **a)

