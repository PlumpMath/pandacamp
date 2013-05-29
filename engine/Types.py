
# This handles the typing of signal functions

# Every built-in type has a python-defined type
# User defined types have a type attribute.  This enables initialization time typechecking

class ptype:
    def __init__(self, tname, encoder = None, decoder = None):
        self.tname = tname
        self.encoder = encoder
        self.decoder = decoder

    def __str__(self):
        r = self.tname
        if self.innerTypes != []:
            r = r + " <"
            for ty in self.innerTypes:
                r = r + str(ty) + " "
            r = r + ">"
        return r
    def encode(self, x):
        if self.encoder is None:
            return x.encode(x)
        return self.encoder(x)
    def decode(self, x):
        if self.decoder is None:
            return x
        return self.decoder(x)




#  Predefined types used elsewhere

numType = ptype("Number", encoder = lambda x: show(x), decoder = lambda x: float(x))
fnType = ptype("Function")
boolType = ptype("Boolean")
stringType = ptype("String", encoder = lambda x:x, decoder = lambda x:x)
noneType = ptype("None")
P3Type = ptype("3-D Point")
HPRType = ptype("HPR")
P2Type = ptype("2-D Point")
controlType = ptype("A control signal")
anyType = ptype('Any type')
noneEType = ptype('Event')
noneType  = ptype('None')
numType1 = [numType]
numType2 = [numType, numType]
numType3 = [numType, numType, numType]
ColorType = ptype('Color')
NeverType = ptype("Never")
SoundType = ptype("Sound")
TupleType = ptype("Tuple")
SoundEventType = eventType(SoundType)
StaticType = ptype("Static")

# Check if the type can be interped?
def interpableType(t):
    return t is P2Type or t is P3Type or t is HPRType or t is ColorType or \
           t is numType or t is controlType


def checkInterpableType(t):
    if not interpType(t):
        print "Can't interpolate type " + str(t)
        exit()

# return the type of an object - either stored in a Panda object or using
# the primitive python type function.

def getPType(x):
    if hasattr(x,'type'):  # Panda types all have a pType slot
        return x.type
    if x is None:
        return noneType
    t = type(x)
    if t is type(1):
        return numType
    if t is type(1.0):
        return numType
    if t is type(True):
        return boolType
    if t is type('abc'):
        return stringType
    if t is type((1,2)):
        return TupleType

    return ptype("Unknown: " + str(t))
