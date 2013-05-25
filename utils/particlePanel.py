from Panda import *

birthRate = slider(min=0.001, max=0.0500, init=0.0200)
litterSize = slider(min=0, max=30, init=10)
lifeSpanBase = slider(min = 0, max = 10, init = 3)
amplitude = slider(min=0, max=3, init=1)
amplitudeSpread = slider(min=0, max=3, init = 0)

text(format("birthRate: %f", birthRate))
text(format("litterSize: %d", litterSize))
text(format("lifeSpanBase: %f", lifeSpanBase))
text(format("amplitude: %f", amplitude))
text(format("amplitudeSpread: %f", amplitudeSpread))

eff = likeFountainWater(position = P3(0,0,0), size = 1,
          birthRate = birthRate, litterSize = litterSize, lifeSpanBase = lifeSpanBase,
          amplitude = amplitude, amplitudeSpread = amplitudeSpread)

effs = {"likeFountainWater":likeFountainWater, "intervalRings":intervalRings, "shakenSparkles":shakenSparkles,
        "warpSpeed":warpSpeed, "heavySnow":heavySnow, "lightSnow":lightSnow, "explosion":explosion, "fireish":fireish}

def swap(p, v):
  global eff
  eff.stop()
  eff = effs[v](position = P3(0,0,0), size = 1,
                birthRate = birthRate, litterSize = litterSize, lifeSpanBase = lifeSpanBase,
                amplitude = amplitude, amplitudeSpread = amplitudeSpread)

#likeFountainWater(position = P3(0,0,0))
#intervalRings(position = P3(0,0,0))
#shakenSparkles(position = P3(0,0,0))
#warpSpeed(position = P3(0,0,0))
#heavySnow(position = P3(0,0,0))
#lightSnow(position = P3(0,0,0))
#explosion(position = P3(0,0,0))
#fireish(position = P3(0,0,0))

pm = menu(["likeFountainWater", "intervalRings", "shakenSparkles", "warpSpeed", "heavySnow", "lightSnow", "explosion", "fireish"],position=P2(-1.1,-.9), size = .5)
react(pm,swap)

start()