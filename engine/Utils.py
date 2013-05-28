
from Numerics import *
from World import *
from FRP import *
# Place a model under control of the mouse
# Note: no way to change pitch / roll.  Maybe add these controls from the keypad.

# Note: this differs from mouseControl in that the original position is
# not at the origin and that negation is needed to make the world move
# with the mouse instead of oppositely.  That is, raising the camera makes
# the objects in the scene go down.
def mouseControlCamera(m):
    m.position = P3(-getX(lbuttonPull), getY(rbuttonPull)-3,-getY(lbuttonPull)+.5)
    m.hpr = HPR(getX(rbuttonPull),0,0)

def mouseControl(m):
    m.position = P3(getX(lbuttonPull), getY(rbuttonPull),getY(lbuttonPull))
    m.hpr = HPR(getX(rbuttonPull),0,0)

def itime(i):
    return interpolate(time, i)

def itimef(i):
    return interpolate(time, forever(i + reverse(i)))

def lastFor(time,model):
    def end(m,v):
        m.exit()
    model.react1(localTimeIs(time), end)
    
def pointForward(m):
    m.hpr = P3toHPR(deriv(m.position))
    
def launch(b, p0, v0, g):
    setType(b.velocity, P3Type)
    b.velocity = v0 + integral(g)
    b.position = p0 + integral(b.velocity)