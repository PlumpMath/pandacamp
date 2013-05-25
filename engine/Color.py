
# A non-reactive color type.
# This has the type field but doesn't check args
# r, g, b, and a values are in (0,1)

# Many predefined colors (stolen from Clastic)

from pandac.PandaModules import *   # Not sure about this!
from Types import *
from StaticNumerics import staticLerp
#from Signal import *

class Color:
    def __init__(self, r, g, b, a = 1):
# Not sure why this is commented out - probably for efficiency
#
#        if r != numType:
#            argTypeError(self.name, r, numType, 'r')
#        if g != numType:
#            argTypeError(self.name, g, numType, 'g')
#        if b != numType:
#            argTypeError(self.name, b, numType, 'b')
#        if a != numType:
#            argTypeError(self.name, a, numType, 'a')

        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.type = ColorType

    def show(self):
        return "[" + str(self.r) + ", " + str(self.g) + ", " + str(self.b) + "]"

# This is used to get color values into the representation used within
# the Panda library

    def toVBase4(self):
        return VBase4(self.r, self.g, self.b, self.a)

    

    def interp(self, t, c2):
        return Color(staticLerp(t, self.r, c2.r),
                     staticLerp(t, self.g, c2.g),
                     staticLerp(t, self.b, c2.b),
                     staticLerp(t, self.a, c2.a))

    def __str__(self):
      return "Color(r = %4.2f, g = %4.2f, b = %4.2f, a = %4.2f )" % (self.r, self.g, self.b, self.a)

# Avoid integer division!!!  Not sure why this worked with the .0
def color24(r, g, b, a = 1):
    return Color(r/255.0, g/255.0, b/255.0, a)

#Predefined Colors
black = color24(0,0,0)
blue = color24(0,0,255)
red = color24(255,0, 0)
green = color24(0,255,0)
darkBlue = color24(0,0,139)
gray = color24(128, 128, 128)
lightGray = color24(200, 200, 200)
darkGray = color24(60, 60, 60)
darkGreen = color24(0,100,0)
darkRed = color24(139,0,0)
white = color24(255,255,255)
yellow = color24(255, 255, 0)
gold = color24(255,215,0)
silver = color24(192,192,192)
navyBlue = color24(0,0,128)
purple = color24(128,0,128)
brown = color24(165,42,43)
orange = color24(255,122,0)

#Extra Colors (start)
teal = color24(0,188,188) #Good Color :)
tan = color24(210,180,140)
cyan = color24(0,255,255)
aquamarine = color24(112,219,147)
slateGray = color24(198,226,255)
purpleBlue = color24(71,60,139)

#Extra Colors (End)

def inverse(c):
        return (color24(255-(255*c.r), 255-(255*c.g), 255-(255*c.b)))

noColor = color24(0,0,0,0)  # Special: used to indicate no added texturing
