from Numerics import *
from World import *
from FRP import *
from StaticNumerics import *
from DynamicGeometry import *

# For whatever reason, the world object imported above is always None.  Thus we
# have to use g.world instead

def launch(model, p0, v0, grav = None):
    if grav is None:
        grav = g.world.gravity
    model.velocity = v0 + integral(grav) 
    model.position = p0 + integral(model.velocity)
