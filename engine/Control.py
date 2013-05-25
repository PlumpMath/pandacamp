# done

# A Control is a group of signals (dictionary) - this allows you to
# bundle signals together into a single object.  Models use both named
# signals and a single control signal.  The named signals override the
# ones in the control input.

from Types import *
from StaticNumerics import *

# A control is just a front end for a dictionary of values
# The "+" operator combines controlls, favoring the rhs on duplicated
# signal names.
# The addVal method returns a new control with an extra signal
# The hasVal method determines whether a control has a signal name in it
#
class Control:
      def __init__(self, d):
          self.dict = d
          self.type = controlType
      def str(self):
          return "Control " + str(self.dict.keys())
      def __add__(self, c2):
          res = c2.dict.copy()
          for k, v in self.dict.iteritems():
              res[k] = v
          return Control(res)
      def addVal(self, key, val):
          res = self.dict.copy()
          res[key] = val;
          return Control(res)
      def hasVal(self, key):
          return self.dict.has_key(key)
      def getVal(self, key):
          return self.dict[key]
      def eraseVal(self, key):
          res = self.dict.copy()
          del res[key]
          return Control(res)
      def interp(self, t, c2):
          #print "pose interp",t,c2
          res = {}
          for k, v in self.dict.iteritems():
              if c2.dict.has_key(k):
                  #print "interpolating", k, v, c2.dict[k]
                  v2 = c2.dict[k]
                  ty = getPType(v)
                  # No way to distinguish between angles / scalars in numbers
                  if ty is numType:
                      res[k] = staticLerp(t, v, v2)  # Might not be needed ...
                  else:
                      res[k] = v.interp(t, v2)

          return Control(res)

      def interpA(self, t, c2):
          return self.interp(t, c2)  # Always do angle interpolation
# Static control functions to be lifted

scEmptyControl = Control({})

def scControl(k, v):
    d = {}
    d[k] = v
    return Control(d)

def scAddVal(k, v, c):
    return c.addVal(k, v)

def scHasVal(k, c):
    return c.hasVal(k)

def scGetVal(k, c):
    return c.getVal(k)

def scEraseVal(k, c):
    return c.eraseVal(k)