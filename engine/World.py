# World.py

# Done

# This creates top level GUI signals and the world and cam objects.


import direct.directbase.DirectStart          # start panda
from direct.showbase import DirectObject      # for event handling
from direct.actor import Actor                # allow use of actor
from direct.gui.DirectGui import *
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from Handle import *
from FRP import tag, hold, typedVar, timeIs, localTimeIs
from direct.showbase.DirectObject import DirectObject
import sys,os
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import OnscreenText
from random import *
from g import* # Global names



# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)


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

  # Puts camera on fixed rod behind target
  # Will be revised later
  def rod(self, target, distance = 3, height = 0.5, constant = 0.5):
      self.position = target.position - distance * HPRtoP3(target.hpr) + P3(0,0,height)
      self.hpr = HPR(getH(target.hpr)+pi,getP(target.hpr),getR(target.hpr))
  def flatrod(self, target, distance = 3, height = 0.5, constant = 0.5):
      self.position = target.position + P3C(distance,  getH(target.hpr)+pi/2, height)
      self.hpr = HPR(getH(target.hpr)+pi,0,0)

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

def lbp(e = True):
    return getEventSignal("mouse1", e)

def rbp(e = True):
    return getEventSignal("mouse3", e)

def lbr(e = True):
    return getEventSignal("mouse1-up", e)

def rbr(e = True):
    return getEventSignal("mouse3-up", e)

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
     g.mouse = typedVar(SP2(0,0), P2Type)
     g.lbutton = hold(False, lbp(True) + lbr(False))
     g.rbutton = hold(False, rbp(True) + rbr(False))
     g.initMousePos = True
     g.mousePos = SP2(0,0)
     g.lbuttonPull = typedVar(SP2(0,0), P2Type)
     g.rbuttonPull = typedVar(SP2(0,0), P2Type)
     g.world = world



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

lbutton = g.lbutton
rbutton = g.rbutton
rbuttonPull = g.rbuttonPull
lbuttonPull = g.lbuttonPull

def applyAll(handler):
    def react(m, e):
        for (m1, m2) in e:
            handler(m1, m2)
    return  react
        
def react(event, handler, extra = None):
    if extra is None:
        world.react(event, handler)
    else:
        event.react(handler, extra)

def react1(event, handler, extra = None):
    if extra is None:
        world.react1(event, handler)
    else:
        event.react1(handler, extra)

def reactAll(event, handler, extra = None):
    if extra is None:
        world.react(event, applyAll(handler))
    else:
        event.react(handler, applyAll(extra))

def reactAll1(event, handler, extra = None):
    if extra is None:
        world.react1(event, applyAll(handler))
    else:
        event.react1(handler, applyAll(extra))

def when(event, handler, extra = None):
    if extra is None:
        world.when(event, handler)
    else:
        event.when(handler, extra)

def when1(event, handler, extra = None):
    if extra is None:
        world.when1(event, handler)
    else:
        event.when1(handler, extra)

def key(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname, val)

def keyUp(kname, val = True):
    kname = checkValidKey(kname)
    return getEventSignal(kname + "-up", val)

def leftClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-leftclick", val)

def rightClick(model, val = True):
    return getEventSignal(model.d.model.getTag('rpandaid') + "-rightclick", val)

allKeyNames = ["escape", "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12",
               "backspace", "insert", "home", 
               "tab",  "delete", "end", "enter", "space"]

keyRenamings = {"upArrow": "arrow_up", "downArrow": "arrow_down",
                "leftArrow": "arrow_left", "rightArrow": "arrow_right",
                "pageUp": "page_up", "pageDown": "page_down"}
                
def checkValidKey(s):
    if s in keyRenamings:
        return keyRenamings[s]
    if type(s) is type("s"):
        if len(s) == 1 or s in allKeyNames:
            return s
    badKeyName(s)

# Clear out the world.  This doesn't reset the global time or camera position.
def resetWorld():
    for m in g.models:
        if m is not world and m is not camera:
            m.exit()
    world.d.switches = []
    world.d.newswitches = []
    g.nextNE2dY = .95         # Positioning for 2-D controls - old controls should be gone
    g.nextNW2dY = .95

# This is used in the launch function in the Physics module.  You can change this if you want another
# gravitational constant / direction.  The 5 assumes that a unit is approx 2 meters - that is, the effects of
# gravity will look natural for objects that would be 2 meters high in the real world (this is a good approx for the panda!)

def atTime(n, r):
    react(timeIs(n), lambda m,v: r())

def atLocalTime(n, r):
    react(localTimeIs(n), lambda m, v: r())

world.gravity = P3(0, 0, -1)


# This is the air resistance used by launch

world.airRes = 0

g.world = world

