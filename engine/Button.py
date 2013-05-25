

# A reactive button

from Handle import *
from direct.gui.DirectGui import *
from Time import *
from World import postEvent
import g

# Arguments to the button constructor:
#   text            String        Normal text (required)
#   position        (x,y)         Placement of button (required)
#   size           Size          Defaults to 0.15
#   name            String        A name used in error message.  Defaults to Buttonx

# Methods / Attributes
#   click - an event that generates a

class Button(Handle):
    def __init__(self, text, position = None, size = 1, name = 'Button'):
        if position is None:
            position = P2(-.95, g.nextNW2dY)
            g.nextNW2dY = g.nextNW2dY -.1
        Handle.__init__(self, name = name)
        self.__dict__['click'] = EventMonitor(self.name)
        self.__dict__['button'] = DirectButton(text = text, pos = (position.x, 0, position.y), scale = size*0.1, command = lambda: postEvent(self.name))

    def refresh(self):
        pass

def button(*p, **k):
    return Button(*p, **k).click
