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
from FRP import wait
from FileUtils import *
from pandac.PandaModules import *
from direct.particles.Particles import *
from direct.particles.ParticleEffect import *
from World import react1
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
            self.react1(wait(duration), lambda m, v: m.exit())

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

#def blowUp(effect = explosions(), time = 2, size = 1, offset = P3(0,0,0)):
    #def r(model, value):
        #pos = model.position.now()
        #e = effect(position = pos + offset, size = size)
        #e.react1(wait(2), exitScene)
        #model.exit()
    #return r

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


def explosionsFn(self, dict):
    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(4000)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(1000)
    p0.setLitterSpread(10)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.25000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(1.00)
    p0.renderer.setStartColor(Vec4(1.00, 1.00, 0.30, 1.00))#Yellow
    p0.renderer.setEndColor(Vec4(0.50, 0.00, 0.00, 1.00))#dark red
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(5.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 9.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.025000)
    self.addParticles(p0)

def explosions(texture = "explosion.png", **a):
    a["texture"] = texture
    PEffect(explosionsFn, name = "explosions", **a)

def fireWorkFn(self, dict):
    self.reset()

    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(.0000, .0000, .0000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(10000)
    p0.setBirthRate(1.5)
    p0.setLitterSize(5000)
    p0.setLitterSpread(10)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(0.5000)
    p0.factory.setLifespanSpread(0.2000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(30.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(1.00)
    p0.renderer.setStartColor(Vec4(1.00, 1.00, 0.30, 1.00))#Yellow
    p0.renderer.setEndColor(Vec4(0.50, 0.00, 0.00, 1.00))#dark red
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 1.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(0.25000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, -2.0000), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def fireWorks(texture = None, **a):
    a["texture"] = texture
    PEffect(fireWorkFn, name = "fireWork", **a)

def fireWork(duration = 2,  **a):
   fireWorks(duration = duration, **a)

def intervalRingsFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("RingEmitter")
    p0.setPoolSize(30000)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(150)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(5.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(1.00)
    p0.renderer.setStartColor(Vec4(1.00, 0.00, 1.00, 1.00))
    p0.renderer.setEndColor(Vec4(1.00, 1.00, 0.00, 1.00))
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETCUSTOM)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 1.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Ring parameters
    p0.emitter.setRadius(3.0000)
    p0.emitter.setRadiusSpread(0.0000)
    p0.emitter.setAngle(31.6075)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Vortex')
    # Force parameters
    self.addForceGroup(f0)


def intervalRings(texture = None, **a):
    a["texture"] = texture
    PEffect(intervalRingsFn, name = "intervalRings", **a)

def likeFountainWaterFn(self,dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("LineParticleRenderer")
    p0.setEmitter("TangentRingEmitter")
    p0.setPoolSize(10000)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(100)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(3.0000)
    p0.factory.setLifespanSpread(0.0000)
    p0.factory.setMassBase(1.0000)
    p0.factory.setMassSpread(0.0000)
    p0.factory.setTerminalVelocityBase(400.0000)
    p0.factory.setTerminalVelocitySpread(0.0000)
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Line parameters
    p0.renderer.setHeadColor(Vec4(0.00, 0.00, 1.00, 1.00))
    p0.renderer.setTailColor(Vec4(0.00, 1.00, 0.00, 1.00))
    p0.renderer.setLineScaleFactor(2.00)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 2.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Tangent Ring parameters
    p0.emitter.setRadius(0.5000)
    p0.emitter.setRadiusSpread(0.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearVectorForce(Vec3(0.0000, 0.0000, -1.5000), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def likeFountainWater(texture = None, **a):
    a["texture"] = texture
    PEffect(likeFountainWaterFn, name = "likeFountainWater", **a)


def rainFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("LineParticleRenderer")
    p0.setEmitter("RingEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(0.0200)
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
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
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHAINOUT)
    p0.renderer.setUserAlpha(1.00)
    # Line parameters
    p0.renderer.setHeadColor(dict["headColor"].toVBase4())
    p0.renderer.setTailColor(dict["tailColor"].toVBase4())
    p0.renderer.setLineScaleFactor(dict["lineScaler"])
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(3.0000)
    p0.emitter.setAmplitudeSpread(1.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Ring parameters
    p0.emitter.setRadius(1.0000)
    p0.emitter.setRadiusSpread(0.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearSinkForce(Point3(getX(dict["force"]), getY(dict["force"]),getZ(dict["force"])), LinearDistanceForce.FTONEOVERR, 1.0000, 1.0000, 1)
    force0.setVectorMasks(1, 1, 1)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def rain(headColor = blue, tailColor = blue,lineScaler = 3, force = p3(0,0,-30), **a):
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    a["lineScaler"] = lineScaler
    a["force"] = force
    PEffect(rainFn, name = "rain", **a)

def shakenSparklesFn(self, dict ):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SparkleParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(10)
    p0.setLitterSpread(3)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Sparkle parameters
    p0.renderer.setCenterColor(dict["headColor"].toVBase4())
    p0.renderer.setEdgeColor(dict["tailColor"].toVBase4())
    p0.renderer.setBirthRadius(0.1000)
    p0.renderer.setDeathRadius(0.1000)
    p0.renderer.setLifeScale(SparkleParticleRenderer.SPNOSCALE)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(1.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    if dict.has_key("force"):
        # Force parameters
        f0 = ForceGroup.ForceGroup('Sink')
        force0 = LinearSinkForce(Point3(getX(dict["force"]), getY(dict["force"]),getZ(dict["force"])), LinearDistanceForce.FTONEOVERR, 1.0000, 1.0000, 1)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        f0.addForce(force0)
        self.addForceGroup(f0)

def shakenSparkles(headColor = white, tailColor = white ,lifeSpan = 0.05, lifeSpanSpread = 1, mass = 1,
     massSpread = 0, terminalVelocity = 400, terminalVelocitySpread = 1, birthRate = 0.02, **a):
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    a["lifeSpan"] = lifeSpan
    a["lifeSpanSpread"] = lifeSpanSpread
    a["mass"] = mass
    a["massSpread"] = massSpread
    a["terminalVelocity"] = terminalVelocity
    a["terminalVelocitySpread"] = terminalVelocitySpread
    a["birthRate"] = birthRate
    PEffect(shakenSparklesFn, name = "shakenSparkles", **a)

def warpSpeedFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("LineParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(1024)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Line parameters
    p0.renderer.setHeadColor(dict["headColor"].toVBase4())
    p0.renderer.setTailColor(dict["tailColor"].toVBase4())
    p0.renderer.setLineScaleFactor(dict["lineScaler"])
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(2.0000)
    p0.emitter.setAmplitudeSpread(2.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    if dict.has_key("force"):
        # Force parameters
        f0 = ForceGroup.ForceGroup('Sink')
        force0 = LinearSinkForce(Point3(getX(dict["force"]), getY(dict["force"]),getZ(dict["force"])), LinearDistanceForce.FTONEOVERR, 1.0000, 1.0000, 1)
        force0.setVectorMasks(1, 1, 1)
        force0.setActive(1)
        f0.addForce(force0)
        self.addForceGroup(f0)



def warpSpeed(headColor = white, tailColor = blue,lifeSpan = 1, lifeSpanSpread = 2, mass = 10,
     massSpread = 3, terminalVelocity = 10, terminalVelocitySpread = 3, lineScaler = 3,
     birthRate = 0.02,  **a):
    a["headColor"] = headColor
    a["tailColor"] = tailColor
    a["lifeSpan"] = lifeSpan
    a["lifeSpanSpread"] = lifeSpanSpread
    a["mass"] = mass
    a["massSpread"] = massSpread
    a["terminalVelocity"] = terminalVelocity
    a["terminalVelocitySpread"] = terminalVelocitySpread
    a["lineScaler"] = lineScaler
    a["birthRate"] = birthRate
    PEffect(warpSpeedFn, name = "warpSpeed", **a)

def fireishFn(self, dict):


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
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(10)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(1200.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
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

def fireish(texture = "fire.png",lifeSpan = 1, lifeSpanSpread = 2, mass = 10,
     massSpread = 3, terminalVelocity = 10, terminalVelocitySpread = 3, lineScaler = 3,
     birthRate = 0.02,  **a):
        a["texture"] = texture
        a["lifeSpan"] = lifeSpan
        a["lifeSpanSpread"] = lifeSpanSpread
        a["mass"] = mass
        a["massSpread"] = massSpread
        a["terminalVelocity"] = terminalVelocity
        a["terminalVelocitySpread"] = terminalVelocitySpread
        a["birthRate"] = birthRate
        PEffect(fireishFn, name = "fireish", **a)


def warpFaceFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("SpriteParticleRenderer")
    #p0.setEmitter("DiscEmitter")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(20000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(100)
    p0.setLitterSpread(10)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
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
    p0.emitter.setAmplitude(6.0000)
    p0.emitter.setAmplitudeSpread(5.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(50.0000)
    self.addParticles(p0)

def warpFace (texture = "face.png",lifeSpan = 2, lifeSpanSpread = 1, mass = 10,
     massSpread = 5, terminalVelocity = 400, terminalVelocitySpread = 0,
     birthRate = 0.02,  **a):
         a["texture"] = texture
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         PEffect(warpFaceFn, name = "warpFace", **a)


def heavySnowFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(100)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(dict["pointSize"])
    p0.renderer.setStartColor(dict["headColor"].toVBase4())
    p0.renderer.setEndColor(dict["tailColor"].toVBase4())
    p0.renderer.setBlendType(PointParticleRenderer.PPONECOLOR)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPNOBLEND)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 9.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(9.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forrce')
    # Force parameters
    force0 = LinearVectorForce(Vec3(getX(dict["force"]), getY(dict["force"]), getZ(dict["force"])))
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)



def heavySnow (lifeSpan = 6, lifeSpanSpread = 0, mass = 1,
     massSpread = 0, terminalVelocity = 400, terminalVelocitySpread = 0,
     birthRate = 0.02, pointSize = 1, headColor = white, tailColor = white,
     force = p3(0,0,-9),  **a):
         a["pointSize"] = pointSize
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         a["headColor"] = headColor
         a["tailColor"] = tailColor
         a["force"] = force
         PEffect(heavySnowFn, name = "heavySnow", **a)

def lightSnowFn(self, dict):

    self.reset()
    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(1.000, 1.000, 1.000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(60000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(3)
    p0.setLitterSpread(0)
    p0.setSystemLifespan(0.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict["massSpread"])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(dict["pointSize"])
    p0.renderer.setStartColor(dict["headColor"].toVBase4())
    p0.renderer.setEndColor(dict["tailColor"].toVBase4())
    p0.renderer.setBlendType(PointParticleRenderer.PPONECOLOR)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPNOBLEND)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(1.0000)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(1.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 9.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(9.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('forrce')
    # Force parameters
    force0 = LinearVectorForce(Vec3(getX(dict["force"]), getY(dict["force"]), getZ(dict["force"])))
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)

def lightSnow (lifeSpan = 6, lifeSpanSpread = 0, mass = 1,
     massSpread = 0, terminalVelocity = 400, terminalVelocitySpread = 0,
     birthRate = 0.02, pointSize = 1, headColor = white, tailColor = white,
     force = p3(0,0,-9),  **a):
         a["pointSize"] = pointSize
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         a["headColor"] = headColor
         a["tailColor"] = tailColor
         a["force"] = force
         PEffect(lightSnowFn, name = "lightSnow", **a)

def smokeTailFn(self, dict):


    self.reset()

    self.setPos(0.000, 0.000, 0.000)
    self.setHpr(0.000, 0.000, 0.000)
    self.setScale(.0000, .0000, .0000)
    p0 = Particles.Particles('particles-1')
    # Particles parameters
    p0.setFactory("PointParticleFactory")
    p0.setRenderer("PointParticleRenderer")
    p0.setEmitter("SphereVolumeEmitter")
    p0.setPoolSize(100000)
    p0.setBirthRate(dict["birthRate"])
    p0.setLitterSize(1)
    p0.setLitterSpread(1)
    p0.setSystemLifespan(1.0000)
    p0.setLocalVelocityFlag(1)
    p0.setSystemGrowsOlderFlag(0)
    # Factory parameters
    p0.factory.setLifespanBase(dict["lifeSpan"])
    p0.factory.setLifespanSpread(dict["lifeSpanSpread"])
    p0.factory.setMassBase(dict["mass"])
    p0.factory.setMassSpread(dict['massSpread'])
    p0.factory.setTerminalVelocityBase(dict["terminalVelocity"])
    p0.factory.setTerminalVelocitySpread(dict["terminalVelocitySpread"])
    # Point factory parameters
    # Renderer parameters
    p0.renderer.setAlphaMode(BaseParticleRenderer.PRALPHANONE)
    p0.renderer.setUserAlpha(1.00)
    # Point parameters
    p0.renderer.setPointSize(dict["pointSize"])
    p0.renderer.setBlendType(PointParticleRenderer.PPBLENDLIFE)
    p0.renderer.setBlendMethod(BaseParticleRenderer.PPBLENDLINEAR)
    # Emitter parameters
    p0.emitter.setEmissionType(BaseParticleEmitter.ETRADIATE)
    p0.emitter.setAmplitude(0.0500)
    p0.emitter.setAmplitudeSpread(0.0000)
    p0.emitter.setOffsetForce(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setExplicitLaunchVector(Vec3(0.0000, 0.0000, 0.0000))
    p0.emitter.setRadiateOrigin(Point3(0.0000, 0.0000, 0.0000))
    # Sphere Volume parameters
    p0.emitter.setRadius(1.0000)
    self.addParticles(p0)
    f0 = ForceGroup.ForceGroup('Sink')
    # Force parameters
    force0 = LinearVectorForce(Vec3(getX(dict["force"]), getY(dict["force"]), getZ(dict["force"])), 1.0000, 0)
    force0.setActive(1)
    f0.addForce(force0)
    self.addForceGroup(f0)


def smokeTail(lifeSpan = 5, lifeSpanSpread = 0, mass = 0.005,
     massSpread = 0, terminalVelocity = 10, terminalVelocitySpread = 0,
     birthRate = 0.05, pointSize = .2, force = p3(-1,0,0),  **a):
         a["pointSize"] = pointSize
         a["lifeSpan"] = lifeSpan
         a["lifeSpanSpread"] = lifeSpanSpread
         a["mass"] = mass
         a["massSpread"] = massSpread
         a["terminalVelocity"] = terminalVelocity
         a["terminalVelocitySpread"] = terminalVelocitySpread
         a["birthRate"] = birthRate
         a["force"] = force
         PEffect(smokeTailFn, name = "smokeTail", **a)