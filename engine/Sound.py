# This can play sound in an event handler

import direct.directbase.DirectStart
import g
from direct.actor import Actor
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *
from Handle import *
from FileUtils import *


class Sound:
    def __init__(self, file, loopCount = 1, volume = 0.5):

        self.filePath = findSound(file)
        self.foundSound = self.filePath is not None
        if self.foundSound:
            self.type = SoundType
            self.volume = volume
            self.loopCount = loopCount
            self.sound = loader.loadSfx(self.filePath)
            self.sound.setVolume(self.volume)
        else:
            print "Sound " + file + " not found"
    def __str__(self):
        "Sound: " + self.filePath
    def play(self):
        if self.foundSound:
            if self.loopCount != 1:
                self.sound.setLoop(True)
                self.sound.setLoopCount(self.loopCount)
            self.sound.play()
            return self.sound
    def setRate(self, n):
        if self.foundSound:
            self.sound.setPlayRate(n)

def sound(*p, **k):
    return Sound(*p, **k)


# Add a loop parameter
def play(s):
    sound(s).play()