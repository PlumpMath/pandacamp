from pandac.PandaModules import *
from direct.particles.Particles import *
from direct.particles.ParticleEffect import *
from direct.task import Task
from direct.gui.DirectGui import *
from Panda import *
import direct.directbase.DirectStart
import math

#base.enableParticles()
#p = ParticleEffect()
#p.loadConfig(Filename('particles/fireCracker.ptf'))
#p.reparentTo(render)
#p.start()

#def button():
#    p.reset()

#b = DirectButton(size = .1, text = "stop", pos = (0, 0, -.95), command = button)
#base.camera.setPos(0, -10, 0)
begin()
sph = sphere(size = .1)
sph2 = sphere(size = .1)
alight1 = PLight(color = Color( .2, .2, .9, 1 ), position = P3(1, 0, 0), parent = sph)
plight = PLight(color = Color( 1, .2, .2, 1 ), position = P3(1, 0, 0), parent = sph2)
pandaBear(position = P3(0, 0, 0))
#discoHall(position = P3(0, 0, 0))

sph.position = P3(sin(time) * 7, 0, cos(time) *7)
sph2.position = P3(-sin(time) * 7, 0, cos(time) *7)
start()