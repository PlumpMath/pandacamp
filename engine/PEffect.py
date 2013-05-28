import PEffect
#!/usr/bin/env python
#HappyDoc:# These variables should be discovered.
#HappyDoc:TestInt=1
#HappyDoc:TestString="String"
#HappyDoc:TestStringModule=string.strip(' this has spaces in front and back ')
#HappyDoc:url=urlencode({'a':'A', 'b':'B'})
#HappyDoc:docStringFormat='StructuredText'
#
import g
from Handle import *
from FRP import localTimeIs
from pandac.PandaModules import *
from direct.particles.Particles import *
from direct.particles.ParticleEffect import *
#import direct.directbase.DirectStart
#from direct.directbase.TestStart import *

from Numerics import *
from Handle import *
from Model import findTexture
#from Time import uniqueName
from pandac.PandaModules import *
from Color import *

##In future, we should add a duration parameter to these particle effects to
##make it easier to set more useful particle effects.
##Kendric June09

def stopIt(m, v):
    m.stop()
    m.exit()
def startIt(m,v):
    m.start()

def explosion(**a):
    e = explosions(**a)
    e.react1(localTimeIs(2), stopIt)
    return e

def explosions(color = yellow, endColor = red, size = 1,poolSize = 1000,
              birthRate = 2.500, litterSize = 250, lifeSpanBase = 2.00,
              terminalVelocityBase = 1.000, emissionType = "ETCUSTOM",
              amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = None, duration = None, **args):
  return PEffect(colorType = "startEnd", particleFile = 'Explosion.py', color=color,
                 endColor = endColor,size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread,
                 lineScaleFactor = lineScaleFactor, duration = duration, **args)

def fireWork(**a):
    f = fireWorks(**a)
    f.react1(localTimeIs(2), stopIt)
    return f

def fireWorks(color = yellow, endColor = red, size = 1,poolSize = 4000,
              birthRate = 2.000, litterSize = 1000, lifeSpanBase = 1.50,
              terminalVelocityBase = 200.000, emissionType = "ETCUSTOM",
              amplitude = 1.0, amplitudeSpread = 1.00, lineScaleFactor = 7, **args):
  return PEffect(colorType = "startEnd", particleFile = 'FireWork.py', color=color,
                 endColor = endColor,size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)


def intervalRings(color = yellow, endColor = red, size = 1,poolSize = 30000,
                  birthRate = 0.0200, litterSize = 500, lifeSpanBase = 6.000,
                  terminalVelocityBase = 400.000, emissionType = "ETCUSTOM",
                  amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00,**args):
  return PEffect(colorType = "startEnd", particleFile = 'IntervalRings.py', color=color,
                 endColor = endColor,size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def likeFountainWater(color = blue, endColor = green, size = 1, poolSize = 100000,
                      birthRate = 0.0200, litterSize = 10, lifeSpanBase = 3.00,
                      terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
                      amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 7.00, radius = 0.5, **args):
  return PEffect(colorType = "headTail", particleFile = 'LikeFountainWater.py', color=color,
                      endColor = endColor,size = size, poolSize = poolSize,
                      birthRate = birthRate, litterSize = litterSize,
                      lifeSpanBase = lifeSpanBase, terminalVelocityBase = terminalVelocityBase,
                      emissionType = emissionType, amplitude = amplitude,
                      amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, radius = radius, **args)

def shakenSparkles(size = 1, poolSize = 20000, birthRate = 0.0200, litterSize = 10, 
                   lifeSpanBase = 3.00, terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
                   amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 7.00, **args):
  return PEffect(particleFile = 'ShakenSparkles.py',size = size, poolSize = poolSize,
                 colorType = "image", birthRate = birthRate, litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def warpSpeed(color = white, endColor = blue, size = 1, poolSize = 2000,
              birthRate = 0.0500, litterSize = 15, lifeSpanBase = 5.00,
              terminalVelocityBase = 4000.000, emissionType = "ETRADIATE",
              amplitude = 5.00, amplitudeSpread = 0.00, lineScaleFactor = 3.25,**args):
  return PEffect(colorType = "headTail", particleFile = 'Warpspeed.py', color=color,
              endColor = endColor,size = size, poolSize = poolSize, birthRate = birthRate,
              litterSize = litterSize, lifeSpanBase = lifeSpanBase,
              terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
              amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def fireish(size = 1,poolSize = 1024, birthRate = 0.0200, litterSize = 10, 
            lifeSpanBase = 0.50, terminalVelocityBase = 4000.000, emissionType = "ETRADIATE",
            amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00, texture = "fire.png",**args):
  return PEffect(colorType = "image", particleFile = 'fireish.py', size = size,
                 poolSize = poolSize, birthRate = birthRate, litterSize = litterSize,
                 lifeSpanBase = lifeSpanBase, terminalVelocityBase = terminalVelocityBase,
                 emissionType = emissionType, amplitude = amplitude, amplitudeSpread = amplitudeSpread,
                 lineScaleFactor = lineScaleFactor,
                 texture = texture, **args)

def warpFace(size = 1,poolSize = 1024, birthRate = 0.0200, litterSize = 10,
            lifeSpanBase = 0.50, terminalVelocityBase = 4000.000, emissionType = "ETRADIATE",
            amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00, texture = "fire.png",**args):
  return PEffect(colorType = "image", particleFile = 'WarpFace.py', size = size,
                 poolSize = poolSize, birthRate = birthRate, litterSize = litterSize,
                 lifeSpanBase = lifeSpanBase, terminalVelocityBase = terminalVelocityBase,
                 emissionType = emissionType, amplitude = amplitude, amplitudeSpread = amplitudeSpread,
                 lineScaleFactor = lineScaleFactor,
                 texture = texture, **args)

def heavySnow(color = white, endColor = white, size = 1, poolSize = 60000,
              birthRate = 0.0200, litterSize = 100, lifeSpanBase = 6.00,
              terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
              amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00,**args):
  return PEffect(colorType = "startEnd", particleFile = 'heavySnow.py', color=color,
                 endColor = endColor, size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def lightSnow(color = white, endColor = white, size = 1, poolSize = 60000,
              birthRate = 0.0200, litterSize = 3, lifeSpanBase = 6.00,
              terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
              amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 1.00,**args):
  return PEffect(colorType = "startEnd", particleFile = 'lightSnow.py',
                 color=color, endColor = endColor, size = size, poolSize = poolSize,
                 birthRate = birthRate, litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

def smokeTail(color = white, endColor = white, size = 1, poolSize = 60000,
              birthRate = 0.0200, litterSize = 100, lifeSpanBase = 6.00,
              terminalVelocityBase = 0, emissionType = "ETRADIATE",
              amplitude = 0, amplitudeSpread = 0.00, lineScaleFactor = 0,**args):
  return PEffect(colorType = "startEnd", particleFile = 'Frict.py', color=color,
                 endColor = endColor, size = size, poolSize = poolSize, birthRate = birthRate,
                 litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

class PEffect(Handle):
    """
    PEffect(Handle):
    """
    pid = 1
    def __init__(self, name = None, particleFile = "LikeFountainWater.py",
                defaultPath = True, parent = render, hpr = None, position = None,
                colorType = None, color = gray, endColor = None,
                size = None, birthRate = None, poolSize = None, litterSize = None,
                lineScaleFactor = None, lifeSpanBase = None, terminalVelocityBase = None,
                texture = None, amplitude = None, amplitudeSpread = None,
                emissionType = "ETRADIATE", radius = None, radiusSpread = None ,
                duration = 0):

        """Initalizes the PEffect.

        PEffect __init__(self,
                        name = 'PEffect',
                        particleFile = "LikeFountainWater.py",
                        defaultPath = True,
                        parent = render,
                        hpr = None,
                        position = None,
                        color = gray,
                        startColor = None ,
                        endColor = None,
                        headColor = None,
                        tailColor = None,
                        birthRate = None,
                        poolSize = None,
                        litterSize = None,
                        lineScaleFactor = None,
                        lifeSpanBase = None,
                        terminalVelocityBase = None,
                        amplitude = None,
                        amplitudeSpread = None,
                        particlePic = None
                        ):
        """
        if texture is not None:
            g.texture = loader.loadTexture(findTexture(texture))
        if name is None:
            name = 'PEffect-%d' % PEffect.pid
            PEffect.pid += 1

        Handle.__init__(self, name = name)
        self.d.colorType = colorType

        #pathname = "/lib/panda/lib/lib-original/particles/"
        base.enableParticles()
        p = ParticleEffect()

        self.__dict__[name] = p
        self.particleName = name
        self.d.model = p  # ???
        
        if defaultPath:
            # print particleFile
            p.loadConfig(Filename(g.pandaPath+"/particles/"+ particleFile))
        else:
            p.loadConfig(Filename(particleFile))

        pd = p.particlesDict["particles-1"]

        if emissionType is not None:
            if emissionType is "ETRADIATE":
                pd.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)  #emitter type ETEXPICIT ETCUSTOM, ETRADIATE
            elif emissionType is "ETCUSTOM":
                pd.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
        if radius is not None:
                    self.__dict__['radius'] = newSignalRef(self, 'radius', numType, radius)
        checkKeyType('PEffect', name, stringType, 'name')

        self.__dict__['position'] = newSignalRef(self, 'position', P3Type)
#        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType,color)
        
        self.__dict__['hpr'] = newSignalRefd(self, 'hpr', HPRType, HPR(0,0,0))
        self.__dict__['size'] = newSignalRefd(self, 'size', numType, 1)
        if size is not None:
             self.size.setBehavior(size)
        self.__dict__['color'] = newSignalRefd(self,'color',ColorType,color)# color at which the effect will start
        if endColor is None:
            endColor = color
        self.__dict__['endColor'] = newSignalRefd(self,'endColor',ColorType,endColor)# color at which the effect will end at
        self.color.setBehavior(color)
        if lineScaleFactor is not None:
            self.__dict__['LineScaleFactor'] = newSignalRefd(self,'LineScaleFactor',numType,lineScaleFactor) #how long a particle is
        if poolSize is not None:
            self.__dict__['PoolSize'] = newSignalRefd(self,'PoolSize',numType,poolSize) #Number of particles avaiable for the entire effect
        if birthRate is not None:
            self.__dict__['BirthRate'] = newSignalRefd(self,'BirthRate',numType,birthRate) #The rate in which the particle effect occurs
        if litterSize is not None:
            self.__dict__['LitterSize'] = newSignalRefd(self,'LitterSize',numType,litterSize) #Number of particles per effect occcurance
        if lifeSpanBase is not None:
            self.__dict__['LifeSpanBase']  = newSignalRefd(self,'LIfeSpanBase',numType,lifeSpanBase) #How long the particle effect stays on screen
        if terminalVelocityBase is not None:
            self.__dict__['TerminalVelocityBase'] = newSignalRefd(self,'TerminalVelocityBase',numType,terminalVelocityBase) #how fast the particles move
        if amplitude is not None:
            self.__dict__['Amplitude'] = newSignalRefd(self,'Amplitude', numType, amplitude)#amplitude is the spreading out of particles
        if amplitudeSpread is not None:
            self.__dict__['AmplitudeSpread'] = newSignalRefd(self,'AmplitudeSpread',numType,amplitudeSpread)#amplitude multiplier spreadings of particles.

        if position is not None:
            self.position.setBehavior(position)
        if hpr is not None:
            self.hpr.setBehavior(hpr)
        if color is not None:
            self.color.setBehavior(color)
        if endColor is not None:
            self.endColor.setBehavior(endColor)
        if parent is not render:
            self.__dict__['parent'] = parent.d.model

        p.reparentTo(render)
        p.start()
        #Had to use this hack because the refresh function kept restarting the particle effects.
        self.__dict__["started"] = True
        if duration != 0:
            self.react1(localTimeIs(duration), lambda m, v: m.exit())

    def refresh(self):
        """
        refresh(self):
            refreshes the variables in the effect
        """
        name = self.name
        p = self.__dict__[name]#particle effect on our level
        Handle.refresh(self)
        if self.__dict__["started"]:
            p0 = p.particlesDict["particles-1"] #particle effect on panda 3d level
            pr = p0.renderer# renderer settings use this prefix
            pf = p0.factory# factory settings use this prefix
            pe = p0.emitter# emitter settings use this prefix
            #renderer based settings
            if self.d.colorType == "startEnd":
              pr.setStartColor(self.__dict__['color'].now().toVBase4())
              pr.setEndColor(self.__dict__['endColor'].now().toVBase4())
            elif self.d.colorType == "headTail":
              
              pr.setHeadColor(self.__dict__['color'].now().toVBase4())
              pr.setTailColor(self.__dict__['endColor'].now().toVBase4())
    #        if self.lineScaleFactor is not None:
    #            pr.setLineScaleFactor(self.__dict__['LineScaleFactor'].now())
    #        if self.headColor is not None:
    #            pr.setHeadColor(self.__dict__['HeadColor'].now().toVBase4())
    #        if self.tailColor is not None:
    #            pr.setTailColor(self.__dict__['TailColor'].now().toVBase4())
            #basic particle settings
            #had to comment this one out because it would randomly cause incredible slowdown
            #p0.setPoolSize(self.__dict__['PoolSize'].now())
            p0.setBirthRate(self.__dict__['BirthRate'].now())
            p0.setLitterSize(int(self.__dict__['LitterSize'] .now()))
            #factory based settings
            pf.setLifespanBase(self.__dict__['LifeSpanBase'] .now())
            pf.setTerminalVelocityBase(self.__dict__['TerminalVelocityBase'].now())
            #emitter based settings
            pe.setAmplitude(self.__dict__['Amplitude'].now())
            pe.setAmplitudeSpread(self.__dict__['AmplitudeSpread'].now())

        position = self.__dict__['position'].now()
        x = getX(position)
        y = getY(position)
        z = getZ(position)
        p.setPos(x,y,z)
        hpr = self.__dict__['hpr'].now()
        h = getH(hpr)
        pit = getP(hpr)
        r = getR(hpr)
        p.setHpr(degrees(h), degrees(pit), degrees(r))
        s = self.size.now()
        p.setScale(s)
#        p.particlesDict["particles-1"].emitter.setRadiateOrgin(Point3(x,y,z))
    def exit(self):
        self.__dict__["started"]= False
        name = self.particleName.now()
        p = self.__dict__[name]
        p.disable()
    def stop(self):
        """
        stop(self):
            stops the emitter from emitting new particles and lets it finish
            the effect on the particles left on screen.
        """
        self.__dict__["started"]= False
        name = self.particleName.now()
        p = self.__dict__[name]
        p.softStop()

    def start(self):
        """
        start(self):
            starts the Particle effect.
        """
        self.__dict__["started"] = True
        name = self.pid
        p = self.__dict__[self.particleName.now()]
        p.softStart()

    def reparentTo(self, handle):
        name = self.name
        p = self.__dict__[name]
        p.reparentTo(handle.d.model)

# Reaction Functions

def exitScene(model, value):
    model.exit()
    
def blowUp(effect = explosions, time = 2, size = 1, offset = P3(0,0,0)):
    def r(model, value):
        pos = model.position.now()
        e = effect(position = pos + offset, size = size)
        e.react1(localTimeIs(2), exitScene)
        model.exit()
    return r