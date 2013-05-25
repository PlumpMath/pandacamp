# Done

# This implements the main event loop using a panda task.  This is where
# reactive values are sustained.

import g
from direct.task import Task
import direct.directbase.DirectStart          # start panda
from direct.gui.DirectGui import *
from copy import copy
from StaticNumerics import *
    
def pollGUI():
       # Take the events that have happened since the previous pollGUI and make them available
       g.events = g.newEvents
       # Start collecting new event values
       g.newEvents = {}
       if base.mouseWatcherNode.hasMouse():
           mpos = base.mouseWatcherNode.getMouse() #get the mouse position in Panda3D form
           lastMousePos = g.mousePos
           g.mousePos = SP2(mpos.getX(), mpos.getY())
           g.mouse.set(g.mousePos)
           if (g.lbutton.now() and not g.initMousePos):
                   g.lbuttonPull.set(g.lbuttonPull.get() + g.mousePos - lastMousePos)
           if (g.rbutton.now() and not g.initMousePos):
                   g.rbuttonPull.set(g.rbuttonPull.get() + g.mousePos - lastMousePos)
           g.initMousePos = False
       # If a left / right mouse click has happened, ask Panda which model was clicked on.  Post an event
       # if there is a model where the mouse clicked
       if g.events.has_key("mouse1") or g.events.has_key("mouse3"):
           m = g.findClickedModels()
           if m is not None:
               if g.events.has_key("mouse1"):
                    g.events[m + "-leftclick"] = True
               else:
                    g.events[m + "-rightclick"] = True

# We use a Panda task that reschedules itself as the main loop

def stepTask(task):
    g.currentTime = task.time  # The task contains the elapsed time
    # Look for models that were introduced during the previous step
    for newModel in g.newModels:
        newModel.checkSignals(g.currentTime)
        newModel.d.switches = newModel.d.newswitches
        g.models.append(newModel)
    g.newModels = []
    g.thunks = []
    # print "Stepping at " + str(g.currentTime)
    pollGUI()   # Read signals from the external GUI
    # Then refresh everything
    g.switched = False
    for m in g.models:
        m.refresh()
        m.d.newswitches = []  # For the next loop
        m.d.undefined = []    # For the next loop
    # Look for switching
    oldModels = copy(g.models)  # In case new models are added
    for m in oldModels:
        m.switch()
    # If any models have switched, reinitialize these new signals
    if g.switched:
       ctxt = g.currentTime
       for m in g.models:
           m.checkSignals(ctxt)
           m.d.switches = m.d.switches + m.d.newswitches # Add in new switchers
    # Force all unevaluated thunks (avoids time leaks)
    for t in g.thunks:
        t.force()
    return Task.cont

# Start initialize the world object

def initTime():
    g.currentTime = 0
    g.models = []
    g.thunks = []
    g.objectNames = {}


# This is used to give unique names to each handle

def uniqueName(baseName):
    if g.objectNames.has_key(baseName):
        n = g.objectNames[baseName]
        n = n + 1
        g.objectNames[baseName] = n
        return baseName + str(n)
    g.objectNames[baseName] = 0
    return baseName

