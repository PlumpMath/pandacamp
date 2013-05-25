# Basic reactive switching
import g

from Signal import *
from Time import *
from FRP import *

def react(signal, switchEvent):
    r = React()
    r.switcher = maybeLift(switchEvent)
    r.s = maybeLift(signal)
    return r

class React(CachedSignal):
    def __init__(self):
        CachedSignal.__init__(self)
        self.switched = False
        self.context = None
    # This prevents a buildup of indirections
    def reduce(self):
        if self.switched:
            return self.newSignal
        return self
    def refresh(self):
        if self.switched:
            self.newSignal = self.newSignal.reduce()
            return self.newSignal.now()
        val = self.s.now()
 #       print val
        e = self.switcher.now()
        if e is None:
            return val
        self.switched = True
        # This is the time of the switch
        # The result of the switch should be a signal factory
        newSignal = maybeLift(e(val))  # Evaluate the new signal
        newSignal.typecheck(self.sigType)
        ctxt = g.currentTime
        newSignal = newSignal.siginit(ctxt)
        newSignal.now()  # result isn't needed but need to update state
        self.newSignal = newSignal
        return val

    def typecheck(self, etype):
        st = self.s.typecheck(anyType)
        self.sigType = st
        return st
    # This resets the integrator when reinitialized.
    def siginit(self, context):
        if needInit(self, context):
            self.active = React()
            self.context = context
            self.active.s = self.s.siginit(context)
            self.active.switcher = self.switcher.siginit(context)
            self.active.sigType = self.sigType
        return self.active


# Event watcher takes an event of some value, an arbitrary number of
# signals, and a function.  This function is applied to the
# instantanous values of the signals.

def when(ev, fn, *args):
    return when1(ev, False, fn, args, True)

def whenv(ev, fn, *args):
    return when1(ev, True, fn, args, True)

def whenEvent(ev, fn, *args):
    return when1(ev, False, fn, args, False)

def whenEventv(ev, fn, *args):
    return when1(ev, True, fn, args, False)

def when1(ev, recur, fn, args, evType):
    res = When(fn, recur, evType)
    res.ev = maybeLift(ev)
    res.args = args
    return res

def evarg(a):
    if hasattr(a,'eval'):
        return a.now()
    return a

class When(CachedSignal):
    def __init__(self, fn, recur, evType):
        CachedSignal.__init__(self)
        # print "When: ", recur, evType
        self.fn = fn
        self.recur = recur
        self.evType = evType
        self.context = None
    def refresh(self):
        e = self.ev.now()
        args = map(evarg, self.args)
        if self.evType:
            # True: event of bool
            if not e:
                return None
        else:
            if e == None:
                return None
        thunk = lambda v:self.addRecur(v, args)
        return thunk
    def addRecur(self, v,args):
        if self.recur:
            return self.fn(v, *args)
        return self.fn(*args)
# Can't really typecheck this
    def typecheck(self, etype):
        return EventAnyType
    # This resets the integrator when reinitialized.
    def siginit(self, context):
        if needInit(self, context):
            self.active = When(self.fn, self.recur, self.evType)
            self.context = context
            self.active.ev = self.ev.siginit(context)
            self.active.args = map(lambda a: a.siginit(context), self.args)
        return self.active
