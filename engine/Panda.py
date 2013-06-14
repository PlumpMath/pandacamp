
#  This is a wrapper for all user-visible functions

#  It also contains "start" which initializes the FRP system and
#  starts Panda

import direct.directbase.DirectStart          # start panda
from direct.showbase import DirectObject      # for event handling
from direct.actor import Actor                # allow use of actor
from direct.gui.DirectGui import *            # 2D GUI elements
from Maze import *
from Racetrack import *
from World import *
from Time import *
from Color import *
from Models import *
from Handle import *
from Numerics import *
from StaticNumerics import randomChoice, random01, random11, randomInt, shuffle
from Slider import *
from Text import *
from Signal import time, static
from FRP import *
# from Switch import *
from Light import *
from Sound import *
from Button import *
from Menu import *
from PEffect import *
from DynamicGeometry import *
from Interp import *
from TextBox import *
from PoseAndScriptFiles import *
from Utils import *
from Collection import collection
from Roll import *
from Bezier import *
from Physics import *
from g import *

# This allows user initialization to override system initialization
g.models.append(world)  # This doesn't happen during initialization
g.models.append(camera)
icontext = 0

for m in g.models:
    m.checkSignals(icontext)
    m.d.switches = m.d.newswitches # Add in switchers generated at initialization
    
stepEngine(0)


# Call this at the end to fire up Panda
def start():
    print "Starting..."
    # Initialize the system.  This is called from "begin" and needs to traverse
    # every active signal in the system.
    for m in g.models:
        m.checkSignals(icontext)
        m.d.switches = m.d.newswitches # Add in switchers generated at initialization
    taskMgr.add(stepTask, 'PandaClock')
    run()

# I don't have the slightest idea why this code won't work if placed in time.py (where it belongs).
# It can't find CollisionNode if placed there.  So it's here - called indirectly through g

def findClickedModels():
           pickerNode = CollisionNode('mouseRay')
           pickerNP = g.panda3dCamera.attachNewNode(pickerNode)
           pickerNode.setFromCollideMask(GeomNode.getDefaultCollideMask())
           pickerRay = CollisionRay()
           pickerNode.addSolid(pickerRay)
           mpos = base.mouseWatcherNode.getMouse()
           pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())
           myHandler = CollisionHandlerQueue()
           myTraverser = CollisionTraverser('traverser name')
           myTraverser.addCollider(pickerNP, myHandler)
           myTraverser.traverse(render)
           # Assume for simplicity's sake that myHandler is a CollisionHandlerQueue.
           # print "Found " + str(myHandler.getNumEntries()) + " Collisions"
           if myHandler.getNumEntries() > 0:
              # This is so we get the closest object.
              myHandler.sortEntries()
              pickedObj = myHandler.getEntry(0).getIntoNodePath()
              # print "Closest = " + str(pickedObj)
              pickedObj = pickedObj.findNetTag('rpandaid')
              # print "tag: " + str(pickedObj)
              if not pickedObj.isEmpty():
                 t = pickedObj.getTag('rpandaid')
                 # print "Clicked on " + str(t)
                 return t
           return None

g.findClickedModels = findClickedModels

#p = hangGlider(position = P3(0,0,0))
#p = volleyBall(position = P3(-1,0,1))
#p = tails(position = P3(1,0,-1))
#start()