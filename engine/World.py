# Done

# This creates top level GUI signals and the world and cam objects.

import g  # Global names
from direct.actor import Actor
import direct.directbase.DirectStart          # start panda
from direct.showbase import DirectObject      # for event handling
from direct.actor import Actor                # allow use of actor
from direct.gui.DirectGui import *
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from copy import copy
from Handle import *
from FRP import tag, hold, typedVar
from direct.showbase.DirectObject import DirectObject

class Camera(Handle):
  def __init__(self):
     g.cam = self
     Handle.__init__(self, name = "camera")
     self.__dict__['position'] = newSignalRefd(self, 'position', P3Type, P3(0, -10, 0))
     self.__dict__['hpr'] = newSignalRefd(self, 'hpr', HPRType, HPR(0, 0, 0))

  def refresh(self):
    # Sample signals for position / HPR and give them to the Panda3D camera
    Handle.refresh(self)
    p = self.position.now()
    g.panda3dCamera.setPos(p.x, p.y, p.z)
    p = self.hpr.now()
    g.panda3dCamera.setHpr(degrees(p.h), degrees(p.p), degrees(p.r))

class World(Handle):
# This initialization code sets up global variables in g as well as the
# world object internals
  def __init__(self):
     g.world = self
     Handle.__init__(self, isWorld = True, name = "World")
     # Signals native to the world object - note that all have defaults
     self.__dict__['color']   = newSignalRefd(self, 'color', ColorType, gray)

  def refresh(self):
    Handle.refresh(self)
    # Check all world-level events
    for w in g.reactEvents:
        w.check()
    c = self.color.now()
    base.setBackgroundColor(c.r, c.g, c.b)

  def kill(self):
       print "World object received a kill signal"
       exit()

def initializeGlobals():
     base.disableMouse()  # this takes the mouse away from Panda3D
     g.panda3dCamera = camera
     g.directObj = DirectObject()
     g.eventSignals = {}
     g.newEvents = {}
     g.events = {}
     g.reactEvents = []
     g.newModels = []
     g.tracking = False
     g.nextNE2dY = .95         # Positioning for 2-D controls
     g.nextNW2dY = .95
     g.tccontext = None
     # Set up the events / behaviors that deal with the mouse
     g.lbp = getEventSignal("mouse1", True)
     g.rbp = getEventSignal("mouse3", True)
     g.lbr = getEventSignal("mouse1-up", True)
     g.rbr = getEventSignal("mouse3-up", True)
     g.mouse = typedVar(SP2(0,0), P2Type)
     g.lbutton = hold(False, tag(True, g.lbp) + tag(False, g.lbr))
     g.rbutton = hold(False, tag(True, g.rbp) + tag(False, g.rbr))
     g.initMousePos = True
     g.mousePos = SP2(0,0)
     g.lbuttonPull = typedVar(SP2(0,0), P2Type)
     g.rbuttonPull = typedVar(SP2(0,0), P2Type)



  # These methods handle signals from the GUI
  # Cache keypress events so there's no duplication of key events - not
  # sure this is useful but it can't hurt.  Probably not a good idea to
  # have multiple accepts for the same event.
  
def getEventSignal(ename, val):
        if g.eventSignals.has_key(ename):
            return tag(val, g.eventSignals[ename])
        e = EventMonitor(ename)
        g.eventSignals[ename] = e
        g.directObj.accept(ename, lambda: postEvent(ename))
        return tag(val, e)

# This saves event occurances in g.newEvents
def postEvent(ename, val = True):
        g.newEvents[ename] = val

# Initialize the environment
initTime()     #  Sets current time to 0
base.enableParticles()

# Exported vocabulary
world = World()
initializeGlobals()
# The underlying Panda3D system uses the name "camera" so we'll use "cam" instead
camera = Camera()
# Bring the GUI behaviors / events to the user namespace
mouse = g.mouse
lbp = g.lbp
lbr = g.lbr
rbp = g.rbp
rbr = g.rbr
lbutton = g.lbutton
rbutton = g.rbutton
rbuttonPull = g.rbuttonPull
lbuttonPull = g.lbuttonPull

def react(event, handler):
    world.react(event, handler)

def react1(event, handler):
    world.react1(event, handler)

def when(event, handler):
    world.when(event, handler)

def when1(event, handler):
    world.when1(event, handler)

def key(kname, val = True):
    return getEventSignal(kname, val)

def leftClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-leftclick", val)

def rightClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-rightclick", val)