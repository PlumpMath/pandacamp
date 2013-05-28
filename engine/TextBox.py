from Handle import *
from direct.gui.DirectGui import *
from Time import *
from World import postEvent
from FRP import var


class TextBox(Handle):
    def __init__(self, position = None, size = 1, name = 'TextBox', width = 15):
        Handle.__init__(self, name = name)
        if position is None:
            position = SP2(.95, g.nextNE2dY)
            g.nextNE2dY = g.nextNE2dY - .1
        self.d.model =  DirectEntry(pos = (position.x,0,position.y),scale=size*0.05, command=lambda v:textBoxChange(v,self), width = width)
        self.__dict__['text'] = var("")
        self.__dict__['enter'] = EventMonitor(self.name)
    
    def refresh(self):
        pass
    
def textBoxChange(v, self):
    postEvent(self.name, v)
    self.__dict__['text'].set(v)

def textBox(*p, **k):
    return TextBox(*p, **k).enter