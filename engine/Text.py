
# 2-D text overlay.
import g
from Handle import *
from direct.gui.OnscreenText import OnscreenText
from Types import *

class Text(Handle):
    def __init__(self, text = None, name = 'Text', position = None, size = 1, color = yellow):
        Handle.__init__(self, name)
        self.__dict__['text'] = newSignalRef(self, 'Text', anyType)
        # This allows the text in the initializer to be reactive.  Not sure why other
        # constructors don't do this.
        if text is not None:
            if not isinstance(text, Signal):
                text = Lift0(text)
            self.text.setBehavior(text)
        if position is None:
            position = P2(-.95, g.nextNW2dY)
            g.nextNW2dY = g.nextNW2dY -.1
        # This code looks OK - we should be able to make the position reactive
        #else:
            #t = getPtype(position)
            #if t != P2Type:
            #    argTypeError(self.name, t, P2Type, 'position')

        self.d.model = OnscreenText(pos = (position.x, position.y), scale = size*0.05, fg = color.toVBase4(), mayChange = True)

    def refresh(self):
        self.d.model.setText(str(self.text.now()))

def text(*p, **k):
    return Text(*p, **k)