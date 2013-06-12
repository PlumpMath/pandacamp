# Done

# This handles all errors

import sys
import g
from Types import getPType

# Detected in checkSignal
def undefinedSignal(obj, sname):
    print "Signal " + sname + " is not defined for " + obj.name
    sys.exit()

def multipleDef(obj, sname):
    print sname + " is already defined for " + obj.name
    #exit()

def unKnownMethod(obj, sname):
    print 'Unknown method ' + sname + ' in object ' + str(obj) + ' is not defined'
    sys.exit()

def signalTypeError(slot, parent, reqType, badType):
    print "Type error for signal " + slot + " of " + parent
    print " Required type: " + str(reqType) + ", type given: " + str(badType)
    sys.exit()

def wrongNumberOfArguments(l):
    print "Wrong number of arguments to " + l
    showtccontext()
    sys.exit()

def argTypeError(fname, was, needed, n):
    print "Error: argument " + str(n) + " to function " + fname
    print "Needed type " + str(needed) + ", found " + str(was)
    showtccontext()
    sys.exit()

def typesMustMatch(fname, t1, t2):
    print "Error: in " + fname + " argument types " + str(t1) + " and " + str(t2) + " must match"
    showtccontext()
    sys.exit()

def showtccontext():
    c = g.tccontext
    if c != None:
        print "Error in definition of " + c.d.slot + " for object " + c.d.parent

def checkKeyType(parent, object, needed, name):
    was = getPType(object)
    if was != needed:
        argTypeError(parent, was, needed, name)

def mismatchedNumerics(msg, t1, t2):
    print "Numeric type mismatch in " + msg
    print "Types: " + str(t1) + " and " + str(t2)
    sys.exit()

def badArgToAbs(arg):
    print "Type " + str(arg) + " cannot be used with abs function"
    sys.exit()

def missingSignalRef(arg):
    print "Signal missing: " + arg
    sys.exit()

def slotInUse(obj, slot):
    print "Slot  " + slot + " of " + obj + " cannot be used as a local signal - use a different name"
    sys.exit()

def interpTypeError(ty):
    print "Can't interpolate values in type " + str(ty)
    sys.exit()

def badKeyName(n):
    print str(n) + " is not a valid key name"
    sys.exit()
