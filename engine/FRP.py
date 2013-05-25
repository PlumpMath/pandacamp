import g
# Done?

# This is the basic implementation of signals and FRP
import g
from Signal import *
from Time import *

# Some things we still need:
#   Clocks
#   Event filtering
#   Switching
#   Dynamic collections
#   Type-specific initialization of integral

# Todos:

# Local time as a method on an object
# Time since last switch
# Extra signals in an object
# Switching on an event within an object:

# This prevents reinitialization (a "runningin" sort of thing.  Probably the same thing
# we need to keep object references up to date.

def keep(s):
    return Keep(s)

class Keep(CachedSignal):
    def __init__(self, s):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.active = None
    def refresh(self):
        return self.s.now()
    def typecheck(self, etype):
        st = self.s.typecheck(etype)
        return st
    # This resets the integrator when reinitialized.
    def siginit(self, context):
        if self.active is not None:
            self.active = self.s.siginit(context)
        return self.active

def integral(s):
    res = Integrator()
    res.s = maybeLift(s)
    return res

class Integrator(CachedSignal):
    def __init__(self):
        CachedSignal.__init__(self)
        self.lastTime = None
        self.context = None
 #        print "Created an integrator"
    def refresh(self):
        g.thunks.append(self)
        return self.val
    def force(self):
        v = self.s.now()
 #       print "Integrating", v
        t = g.currentTime
        if self.lastTime is not None:
            deltaT = t - self.lastTime
            self.val = self.val + v * deltaT
        self.lastTime = t
    def typecheck(self, etype):
#        print "Type checking integrator"
        st = self.s.typecheck(addableType)
#        print "Integrator argument type: " + st.tname + " Zero: " + str(st.zero)
        if not(addableType.implies(st)):
            argTypeError("integral",st, addableType, 1)
        self.zero = st.zero
        return st
    # This resets the integrator when reinitialized.
    def siginit(self, context):
        if needInit(self, context):
#            print "Initializing an integrator"
            newsig = self.s.siginit(context)
            newint = Integrator()
            newint.s = newsig
            newint.val = self.zero
            self.active = newint
        return self.active



# TODO: an initial value based on type, type checking, a proper initializer

def deriv(init, s):
    return DerivSignal(s, init)

class DerivSignal(CachedSignal):
    def __init__(self, s, init):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.init = init
        self.lastTime = None
        self.context = None
    def refresh(self):
        v = self.s.now()
        t = g.currentTime
        if self.lastTime is None:
            self.lastTime = t
            self.lastVal = v
            return self.init
        deltaT = t - self.lastTime
        deltaV = v - self.lastVal
        self.lastTime = t
        self.lastVal = v
        return deltaV * (1/deltaT)
    def typecheck(self, etype):
        sigType = self.s.typecheck(addableType)
        if not addableType.implies(sigType):
            argTypeError("deriv", sigType, addableType, 2)
        initType = getPType(self.init)
        if initType != sigType:
            typesMustMatch("deriv", sigType, initType)
        return sigType
    def siginit(self, context):
        if needInit(self, context):
            self.active = DerivSignal(self.s.siginit(context), self.init)
            self.context = context
        return self.active

def tracker(f, s0, s, resType):
    res = StateMachine(s0, f, resType)
    res.s = maybeLift(s)
    return res
# This should replace deriv someday
class StateMachine(CachedSignal):
    def __init__(self, initState, f, resType):
        CachedSignal.__init__(self)
        self.init = initState
        self.f = f
        self.resType = resType
        self.context = None
    def refresh(self):
        v = self.s.now()
        (newState, output) = self.f(self.state, v)
        self.state = newState
        return output
    def typecheck(self, etype):
        return self.resType
    def siginit(self, context):
        if needInit(self, context):
            self.active = StateMachine(self.init, self.f, self.resType)    # Shouldn't need type stuff
            self.active.s = self.s.siginit(context)
            self.active.state = self.init
            self.context = context
        return self.active

# Maybe reverse these arguments ...

def tag(v, s):
    return TagSignal([v], s)

def tags(v, s):
    return TagSignal(v, s)

#  Replace the value of each happening by a constant value

class TagSignal(Event):
    def __init__(self, vals, s):
        Event.__init__(self)
        self.s = maybeLift(s)
        self.vals = vals
        self.i = 0
        self.context = None
    def refresh(self):
        eventVal = self.s.now()
        if eventVal is None:
            return None
        res = self.vals[self.i % len(self.vals)]
        self.i = self.i + 1
        return res
    def typecheck(self, etype):
        # Should check type of incoming signal ...
        t = getPType(self.vals[0])
        return eventType(t)
    def siginit(self, context):
        if needInit(self, context):
            self.active = TagSignal(self.vals, self.s.siginit(context))
            self.context = context
        return self.active

def hold(i, s):
    return HoldSignal(i, s)

class HoldSignal(CachedSignal):
    def __init__(self, i, s):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.i = i
        self.context = None
    def refresh(self):
        v = self.s.now()
        if v != None:
#            print "Storing " + str(v) + " in hold at " + str(g.currentTime)
            self.i = v
        return self.i
    def typecheck(self, etype):
        initType = getPType(self.i)
        etype = self.s.typecheck(anyType)
        # Check the event type someday but not now ...
        return initType
    def siginit(self, context):
        if needInit(self, context):
            self.active = HoldSignal(self.i, self.s.siginit(context))
            self.context = context
        return self.active

def accum(v0, s):
    return AccumSignal(v0, s)

class AccumSignal(CachedSignal):
    def __init__(self, v0, s):
        CachedSignal.__init__(self)
        self.s = maybeLift(s)
        self.v0 = v0
        self.context = None
    def refresh(self):
        v = self.s.now()
        if v is None:
            return self.v0
        self.v0 = v(self.v0)
        return self.v0
    def typecheck(self, etype):
        initType = getPType(self.v0)
        # Check the event type someday but not now ...
        # Add a wrapper to check fn types maybe
        return initType
    def siginit(self, context):
        if needInit(self, context):
            self.active = AccumSignal(self.v0, self.s.siginit(context))
            self.context = context
        return self.active


mergeE = liftE(mergeE1, 2, "MergeE")

class Clock(CachedSignal):
    def __init__(self, start, step, end, useLocal):
        CachedSignal.__init__(self)
        self.start = start
        self.step = step
        self.end = end
        self.useLocal = useLocal
        self.context = None
    def refresh(self):
        if self.done:
            return False
        t = g.currentTime
        if self.useLocal:
            t = t - self.initialTime
        if t < self.nextEvent:
            return None
        if self.step is None:
            self.done = True
        else:
            if self.end is not None and t > self.end:
                self.done = True
            self.nextEvent = self.nextEvent + self.step
        return True
    def typecheck(self, etype):
        return EventBoolType
    def siginit(self, context):
        if needInit(self, context):
            self.active = Clock(self.start, self.step, self.end, self.useLocal)
            self.active.done = False
            self.context = context
            self.active.initialTime = context
            self.active.nextEvent = self.start
        return self.active

def timeIs(t):
    return Clock(t,None,t,False)

def alarm(start = 0, end = None, step = None):
    return Clock(start, step, end, True)

def localTimeIs(t):
    return Clock(t,None,t,True)

def localAlarm(start = 0, end = None, step = None):
    return Clock(start, step, end, True)

# This is to handle "reactive" variables

class RVar(CachedSignal):
    def __init__(self, initValue, type):
        CachedSignal.__init__(self)
        self.value = initValue
        self.type = type
    def refresh(self):
        return self.value
    def typecheck(self, etype):
        return self.type
    def siginit(self, context):
        return self   #  This should never happen!
    def get(self):    #  Used inside reaction code
        return self.value
    def set(self, val):
        self.value = val
    def add(self, val):
        self.value = self.value + val;
    def sub(self, val):
        self.value = self.value - val;
    def times(self, val):
        self.value = self.value * val;


def var(init):
    return RVar(init, getPType(init))

def typedVar(init, ty):
    return RVar(init, ty)

class RArr(CachedSignal):#I have no idea if this should work...
    def __init__(self, initValue, type):
        CachedSignal.__init__(self)
        self.value = initValue
        self.type = type
    def refresh(self):
        return self.value
    def typecheck(self, etype):
        return self.type
    def siginit(self, context):
        return self   #  This should never happen!
    def get(self):    #  Used inside reaction code
        return self.value
    def set(self, val):
        self.value = val
    def add(self, val):
        for i in self.value:
            i = i + val;
    def sub(self, val):
        for i in self.value:
            i = i - val;
    def times(self, val):
        for i in self.value:
            i = i * val;
def arr(init):
    return RArr(init, getPType(init))
def typedArr(init, ty):
    return RArr(init, ty)
