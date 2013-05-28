from Numerics import *
from World import *
from FRP import *
from StaticNumerics import *
from DynamicGeometry import *


def launch(model, p0, v0):
    setType(model.velocity, P3Type)
    model.velocity = v0 + integral(P3(0,0,-5)) # g.world.gravity)
    model.position = p0 + integral(model.velocity)
