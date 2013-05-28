
# A reactive menu

from Handle import *
from direct.gui.DirectGui import *
from Time import *
from World import postEvent

# Arguments to the button constructor:
#   text            String        Normal text (required)
#   position        (x,y)         Placement of button (required)
#   size            Size          Defaults to 1
#   name            String        A name used in error message.  Defaults to Buttonx

# Methods / Attributes
#   select - an event that generates a string

class Menu(Handle):
    def __init__(self, items, position = None, size = 1, name = 'Menu'):
        Handle.__init__(self, name = name)
        self.__dict__['select'] = EventMonitor(self.name)
        if position is None:
            pos = (.95, 0, g.nextNE2dY)
            g.nextNE2dY = g.nextNE2dY - .1
        self.d.model =  DirectOptionMenu(pos = (position.x,0,position.y),scale=size*0.15,items=items, command=lambda v: postEvent(self.name, v))

    def refresh(self):
        pass
    def addItem(self, string):
        x = self.d.model
        tmp_menu = x['items']
        new_item = string
        tmp_menu.insert(-1,new_item) #add the element before add
        x['items'] = tmp_menu

def menu(*p, **d):
    return Menu(*p, **d).select
