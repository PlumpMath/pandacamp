
# This defines an object that appears on the screen whose representation is obtained from a
# 3-D model in an egg file.  These have the following reactive parameters:
#   position  P3      location in 3-space
#   hpr       HPR     orientation in 3-space
#   scale     scalar  relative size (1 = unit cube)
#   color     Color   dynamic texture (None = model skin, otherwise = color of object)
import g
from direct.actor import Actor
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from Handle import *
from FileUtils import *
from FRP import wait
from Collection import getCollection

# This fills in all of the defaults
parameterCache = {}
defaultModelParameters = {"localPosition" : P3(0,0,0),
                          "localSize" : 1,
                          "localOrientation" : HPR(0,0,0),
                          "joints" : [],
                          "animations" : None,
                          "defaultAnimation" : None,
                          "frame" : None,
                          "cRadius" : 1,
                          "cFloor" : 0,
                          "cTop" : 1,
                          "cType" : "cyl"}

modelParameters = {"localPosition" : P3Type,
                   "localSize" : numType,
                   "localOrientation" : HPRType,
                   "joints" : StringListType,
                   "animations" : StringListType,
                   "defaultAnimation" : stringType,
                   "frame" : numType,
                   "cRadius" : numType,
                   "cFloor" : numType,
                   "cTop" : numType,
                   "cType" : stringType}

pandaParameters = { "localSize" : 0.00178,
                    "localPosition" : P3( 0, 0.21, 0),
                    "localOrientation" : HPR(0, 0, 0)}

def model(fileName, name = None, size = None, hpr = None, position = None, color = None,
                 control = None, texture = None, duration = 0, joints = [], animations = None, defaultAnimation = None, frame = None, kind = None):
   res = Model(fileName, name, size, hpr, position, color,
                control, texture, duration, kind)
   return res

class Model(Handle):
    def __init__(self, fileName, name, size, hpr, position, color,
                 control, texture, duration, kind):
        if name is None:
            name = fileName  #  Should parse off the directories
        Handle.__init__(self, name = name, duration = duration)
        mFile = fileSearch(fileName, "models")
        if mFile is None:
            print "Can't find model" + str(fileName)
            mFile = Filename("panda-model.egg.pz")
            mParams = pandaParameters
        elif fileName in parameterCache:
            mParams = parameterCache[fileName]
        else:
            mParamFile = Filename(mFile)
            mParamFile.setExtension("model")
            if mParamFile.exists():
                mParams = loadDict(mParamFile, modelParameters, defaultModelParameters)
            else:
                print "No .model for " + str(fileName)
                mParams = defaultModelParameters
            parameterCache[fileName] = mParams
        localPosition = mParams["localPosition"]
        localSize = mParams["localSize"]
        localOrientation = mParams["localOrientation"]
        joints = mParams["joints"] # Needs conversion to array of pairs  # Should remove this from the .model
        animations = mParams["animations"]  # Should remove this from the .model
        defaultAnimation = mParams["defaultAnimation"]  # Should remove this from the .model
        frame = mParams["frame"]   # Should remove this from the .model
        cRadius = mParams["cRadius"]
        cTop = mParams["cTop"]
        cFloor = mParams["cFloor"]
        cType = mParams["cType"]

        self.d.fileName = mFile
        self.d.hasJoints = len(joints) != 0
        self.d.joints = joints
        self.d.jointNodes = {}
        self.cRadius = static(cRadius)
        self.cFloor = static(cFloor)
        self.cTop = static(cTop)
        self.cType = static(cType)
        self.d.noHPR = False
        self.d.defaultAnimation = defaultAnimation
        ctl = newSignalRefd(self, "control", controlType, scEmptyControl)
        self.__dict__["control"] = ctl
        for j,pj in joints:
            self.__dict__[j] = newSignalRefd(self, j, HPRType, HPR(0,0,0), ctl)

        if self.d.hasJoints:
            if animations != None:
                self.d.model = Actor.Actor(self.d.fileName, animations)
                #self.d.model.reparentTo(render)
                if frame != None:
                    self.d.frame = frame
                else:
                    undefinedSignal(self, 'frame') # ????  Bad error message ...
            else:
                self.d.model = Actor.Actor(self.d.fileName)
            for x in joints:
                if isinstance(x, basestring):
                    j = x
                    pj = x
                else:
                    j, pj = x
                self.d.jointNodes[j] = self.d.model.controlJoint(None, "modelRoot", pj)
                if self.d.jointNodes[j] == None:
                    print 'joint not found: ' + j
                    exit()
        else:   #  Not jointed
            self.d.model = loader.loadModel(self.d.fileName)
            if self.d.model == None:
                print 'Model not found: ' + fileName  # Shouldn't happen - file was found
                exit()
        g.nextModelId = g.nextModelId + 1
        self.d.model.setTag('rpandaid', str(g.nextModelId))
        self.d.localSize = localSize
        self.d.localPosition = localPosition
        self.d.localOrientation = localOrientation
        self.d.onScreen = False
        self.d.currentTexture = ""
        self.__dict__['position'] = newSignalRefd(self, 'position', P3Type, P3(0,0,0), ctl)
        self.__dict__['hpr']   = newSignalRefd(self, 'hpr', HPRType, HPR(0,0,0), ctl)
        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType, noColor, ctl)
        self.__dict__['size'] = newSignalRefd(self, 'size', numType, 1, ctl)
        self.__dict__['texture'] = newSignalRefd(self, 'texture', stringType, "", ctl)
        if size is not None:
             self.size.setBehavior(size)
        if position is not None:
             self.position.setBehavior(position)
        if control is not None:
             # print "Setting control", control
             self.control.setBehavior(control)
#        print hpr
#        print self.hpr.signal
        if hpr is not None:
             self.hpr.setBehavior(hpr)
#        print "HPR: "
#        print self.hpr.signal
        if color is not None:
             self.color.setBehavior(color)
        self.d.animPlaying = False # This initializes it so there is no animation playing.
        if texture is not None:
            print "Texture for model " + name
            tex = findTexture(texture)
            self.d.currentTexture = texture
            self.d.model.setTexture(tex, 1)
        if kind is not None:
            getCollection(kind).add(self)

    def showModel(self):
        if not self.d.onScreen:
           self.d.model.reparentTo(render)
           self.d.onScreen = True
    def refresh(self):
#       print "Refreshing " + self.name
       Handle.refresh(self)
       p = self.position.now()
       s = self.size.now()
       self.d.model.setScale(s*self.d.localSize)
#            print "Model position: " + str(p)
       self.d.model.setPos(p.x + self.d.localPosition.x*s,
                           p.y + self.d.localPosition.y*s,
                           p.z + self.d.localPosition.z*s)
       if not self.d.noHPR:
           d = self.hpr.now()
           self.d.model.setHpr(degrees(d.h + self.d.localOrientation.h),
                               degrees(d.p + self.d.localOrientation.p),
                               degrees(d.r + self.d.localOrientation.r))

       c = self.color.now()
       if c.a != 0:   # This signals that there is no color to paint on the model
           self.d.model.setColor(c.toVBase4())
       texture = self.texture.now()
       if texture != "" and texture != self.d.currentTexture:
            texf = findTexture(texture)
            self.d.currentTexture = texture
            self.d.model.setTexture(texf, 1)
       if not self.d.animPlaying:#this just lets the animation continue instead of overriding it.
           if self.d.hasJoints:
               for j,pj in self.d.joints:
                    sig = getattr(self, j)
                    hpr = sig.now()
                    #print "Setting joint", j, hpr
                    #print self.d.jointNodes[j]
                    #self.d.jointNodes[j].setHpr(degrees(hpr.x),degrees(hpr.y), degrees(hpr.z))
                    self.d.jointNodes[j].setH(degrees(hpr.h))
                    self.d.jointNodes[j].setP(degrees(hpr.p))
                    self.d.jointNodes[j].setR(degrees(hpr.r))
                    #print self.d.jointNodes[j].getH()
                    # Set panda joint pj to hpr (convert from radians)
               if self.d.defaultAnimation is not None:
                self.d.model.loop(self.d.defaultAnimation, fromFrame = self.d.frame, toFrame = self.d.frame)
    def play(self, anim):
        if anim == "stop":
            self.d.animPlaying = False
        else:
            self.d.model.loop(anim)
            self.d.animPlaying = True
    #def setTexture(self, texture):
    #    tex = loader.loadTexture(findTexture(texture))
    #    self.d.model.setTexture(tex, 1)
    def reparentTo(self, handle):
        self.d.model.reparentTo(handle.d.model)
        # This doesn't allow the HPR to modify the cylinder so it's pretty crude.
    def touches(self, handle, trace):
        if trace:
           print "Touch: " + repr(self) + " (" + self.cType + ") " + repr(handle) + " (" + handle.cType + ")"
        mr = self.cRadius*self.size.now()
        mp = self.position.now()
        yr = handle.cRadius*handle.size.now()
        yp = handle.position.now()
        if trace:
            print repr(mp) + " [" + repr(mr) + "]  " + repr(yp) + " [" + repr(yr) + "]"
        if self.cType == "sphere":
            if handle.cType == "sphere":
                return absP3(subP3(mp, yp)) < mr + yr
            elif handle.cType == "cyl":   # Test if the x,y points are close enough.  This treats the sphere as a cylinder
                d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
                if d > mr + yr:
                    return False
                else:
                    cb = yp.z + handle.size.now()*handle.cFloor
                    ct = yp.z + handle.size.now()*handle.cTop
                    sb = mp.z-mr
                    st = mp.z+mr
 #                   print str(cb) + " " + str(ct) + " " + str(sb) + " " + str(st)
                    return ct > sb and cb < st
        elif self.cType == "cyl":
            if handle.cType == "sphere":
                d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
 #               print "c to s (dist = " + str(d) + ")"
                if  d > mr + yr:
                    return False
                else:
                    cb = mp.z + self.size.now()*self.cFloor
                    ct = mp.z + self.size.now()*self.cTop
                    sb = yp.z-yr
                    st = yp.z+yr
#                    print str(cb) + " " + str(ct) + " " + str(sb) + " " + str(st)
                    return ct > sb and cb < st
            elif handle.cType == "cyl":
#                print str(mp.x) + " , " + str(mp.y)
                d = absP2(subP2(P2(mp.x, mp.y), P2(yp.x, yp.y)))
                if trace:
                    print "c to c (dist = " + str(d) + ") " + str(mr+yr)
                if  d > mr + yr:
                    return False
                else:
                    res = self.cTop + mp.z > handle.cFloor + yp.z and self.cFloor + mp.z < handle.cTop + yp.z
                    if trace:
                        print "Result: " + str(res) + " " + str((self.cTop, mp.z, handle.cFloor, yp.z, self.cFloor, handle.cTop))
                    return res
        return False
    def allModels(self):  # A collection will return more than one model
        return [self]
