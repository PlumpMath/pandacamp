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
from FileUtils import *
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
    e.react1(wait(2), stopIt)
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
    f.react1(wait(2), stopIt)
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

#  Currently crashes ppython
def shakenSparkles(size = 1, poolSize = 20000, birthRate = 0.0200, litterSize = 10,
                   lifeSpanBase = 3.00, terminalVelocityBase = 400.000, emissionType = "ETRADIATE",
                   amplitude = 1.00, amplitudeSpread = 0.00, lineScaleFactor = 7.00, **args):
  return PEffect(particleFile = 'ShakenSparkles.py',size = size, poolSize = poolSize,
                 colorType = "image", birthRate = birthRate, litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                 terminalVelocityBase = terminalVelocityBase, emissionType = emissionType,
                 amplitude = amplitude, amplitudeSpread = amplitudeSpread, lineScaleFactor = lineScaleFactor, **args)

#shakenSparkles = likeFountainWater

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

    pid = 1
    def __init__(self, particleFn, name = None,
               hpr = None, position = None,
              
                size = None,
                duration = 0, ** a):

        if name is None:
            name = 'PEffect-%d' % PEffect.pid
            PEffect.pid += 1

        Handle.__init__(self, name = name)

        #pathname = "/lib/panda/lib/lib-original/particles/"
        base.enableParticles()
        p = ParticleEffect()
        particleFn(p, a)
        self.d.model = p  # ???



        self.__dict__['position'] = newSignalRef(self, 'position', P3Type)
#        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType,color)

        self.__dict__['hpr'] = newSignalRefd(self, 'hpr', HPRType, HPR(0,0,0))
        self.__dict__['size'] = newSignalRefd(self, 'size', numType, 1)
        if size is not None:
             self.size.setBehavior(size)
  
        if position is not None:
            self.position.setBehavior(position)
        if hpr is not None:
            self.hpr.setBehavior(hpr)


        p.reparentTo(render)
        p.start()
        #Had to use this hack because the refresh function kept restarting the particle effects.
        if duration != 0:
            self.react1(localTimeIs(duration), lambda m, v: m.exit())

    def refresh(self):

        p = self.d.model
        Handle.refresh(self)
        

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
        e.react1(wait(2), exitScene)
        model.exit()
    return r

def fireFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    p0.setEmitter("DiscEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(1200.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAOUT)
    p0.renderer.setUserAlpha(0.22)
    # Sprite parameters
    #print __import__("g").texture
    p0.renderer.setTexture(findTexture(dict["texture"]))
    p0.renderer.setColor(Vec4(1.00, 1.00, 1.00, 1.00))
    p0.renderer.setXScaleFlag(1)
    p0.renderer.setYScaleFlag(1)
    p0.renderer.setAnimAngleFlag(0)
    p0.renderer.setInitialXScale(0.0050)
    p0.renderer.setFinalXScale(0.0200)
    p0.renderer.setInitialYScale(0.0100)
    p0.renderer.setFinalYScale(0.0200)
    p0.renderer.setNonanimatedTheta(0.0000)
    p0.renderer.setAlphaBlendMethod(BaseParticleRenderer.PPNOBLEND)
    p0.renderer.setAlphaDisable(0)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 3.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Disc parameters
    p0.emitter.setRadius(0.5000)
    self.addParticles(p0)

def fire1(texture = "fire.png", **a):
    a["texture"] = texture
    PEffect(fireFn, name = "fire", **a)
