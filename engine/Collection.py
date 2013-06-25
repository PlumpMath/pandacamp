

import g
from Time import *
from Signal import *
from Numerics import *
from Types import *
from Switchers import *

class Collection:
    def __init__(self, name = "unknows"):
        self.name = name
        self.members = []
    def allModels(self):
        return self.members
    def add(self, model):
        self.members = [model] + self.members
        model.d.collections = [self] + model.d.collections
    def remove(self, model):
        newMembers = []
        for m in self.members:
            if not (m is model):
                newMembers = newMembers + [m]
        self.members = newMembers

collection = Collection

def getCollection(s):
    if isinstance(s, basestring):
        if s not in g.collections:
            g.collections[s] = collection(s)
        return g.collections[s]
    return s  # Should already be a collection

def showCollection(c):
    r = str(c.name) + ": "
    for o in c.allModels():
        r = r + str(o.name) + " "
    return r
