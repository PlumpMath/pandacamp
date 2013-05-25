import g
from Color import *
from Handle import *
from Time import uniqueName
from pandac.PandaModules import *

class PLight(Handle):
    def __init__(self, name = 'pointlight',  position = None, color = None):
        Handle.__init__(self, name = name)
        checkKeyType('pointlight', name, stringType, 'name')
        self.__dict__['position'] = newSignalRef(self, 'position', P3Type)
        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType, white)
        if position is not None:
            self.position.setBehavior(position)
        if color is not None:
            self.color.setBehavior(color)
        self.__dict__['pLight'] = PointLight('plight')
        self.__dict__['plnp'] = render.attachNewNode(self.pLight)
        render.setLight(self.plnp)
        g.models.append(self)

    def refresh(self):
        Handle.refresh(self)
        c = self.__dict__['color'].now()
        self.__dict__['pLight'].setColor(c.toVBase4())
        p = self.__dict__['position'].now()
        self.__dict__['plnp'].setPos(p.x, p.y, p.z)

class ALight(Handle):
    def __init__(self, name = 'ambientlight',  color = None):
        Handle.__init__(self, name = name)
        checkKeyType(name, name, stringType, 'name')
        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType, white)
        if color is not None:
            self.color.setBehavior(color)
        self.__dict__['parent'] = render
        self.__dict__['ambientLight'] = AmbientLight( 'ambientLight' )
        self.__dict__['ambientLightNP'] = self.parent.attachNewNode( self.ambientLight )
        render.setLight(self.ambientLightNP)
        g.models.append(self)

    def refresh(self):
        c = self.color.now()
        self.ambientLight.setColor( c.toVBase4() )

# Directional light has a heading but no origin

class DLight(Handle):
    def __init__(self, name = 'DLight', parent = render, hpr = None, color = None):
        Handle.__init__(self, name = name)
        checkKeyType('DLight', name, stringType, 'name')
        self.__dict__['hpr'] = newSignalRef(self, 'hpr', HPRType)
        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType, white)
        self.__dict__['parent'] = parent
        if hpr is not None:
            self.hpr.setBehavior(hpr)
        if color is not None:
            self.color.setBehavior(color)
        self.__dict__['directionalLight'] = DirectionalLight( "directionalLight" )
        self.__dict__['directionalLightNP'] = self.parent.attachNewNode( self.directionalLight )
        render.setLight(self.directionalLightNP)
        g.models.append(self)

    def refresh(self):
        c = self.__dict__['color'].now()
        self.directionalLight.setColor( c.toVBase4())
        h = self.__dict__['hpr'].now()
        self.directionalLightNP.setHpr(degrees(h.h), degrees(h.p), degrees(h.r))

# Probably should remove some of this - keep position, color, and fov only
# I don't see how to directly set the direction - this only seems to be able
# to focus on a specific object
class SLight(Handle):
    def __init__(self, name = 'spotight', parent = render, focus = None, position = None, exponent = None, color = None, fov = None, attenuation = None, hpr = None):
        Handle.__init__(self, name = name)
        checkKeyType('SLight', name, stringType, 'name')
        self.__dict__['position'] = newSignalRef(self, 'position', P3Type)
        self.__dict__['exponent'] = newSignalRefd(self, 'exponent', numType, 60)
        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType, white)
        self.__dict__['fov'] = newSignalRefd(self, 'fov', numType, 8)
        self.__dict__['parent'] = parent
        self.__dict__['attenuation'] = newSignalRefd(self, 'attenuation', P3Type, P3(.1, .04, 0))
        if focus is not None:
            self.__dict__['focus'] = focus
        if position is not None:
            self.position.setBehavior(position)
        if exponent is not None:
            self.exponent.setBehavior(exponent)
        if color is not None:
            self.color.setBehavior(color)
        if exponent is not None:
            self.exponent.setBehavior(exponent)
        if fov is not None:
            self.fov.setBehavior(fov)
        if attenuation is not None:
            self.attenuation.setBehavior(attenuation)
        if parent is not render and parent is not camera:
            self.__dict__['parent'] = parent.d.model

        self.__dict__['slight'] = Spotlight('slight')
        self.__dict__['slight'].setColor(VBase4(1, 1, 1, 1))
        self.__dict__['lens'] = PerspectiveLens()

        self.__dict__['slight'].setLens(self.__dict__['lens'])
        self.__dict__['slnp'] = self.parent.attachNewNode(self.slight)

        if focus is not None:
            self.slnp.lookAt(focus.d.model)
        render.setLight(self.slnp)
        g.models.append(self)

    def refresh(self):
        c = self.color.now()
        self.slight.setColor( c.toVBase4())
        p = self.position.now()
        self.slnp.setPos(p.x, p.y, p.z)
        e = self.exponent.now()
        self.slight.setExponent(e)
        f = self.fov.now()
        self.lens.setFov(f, f)
        a = self.attenuation.now()
        self.slight.setAttenuation(Vec3(a.x, a.y, a.z))

    # Friendly user names

def pointLight(*p, **a):
        res = PLight(*p, **a)
        return res

def directionalLight(*p, **a):
        res = DLight(*p, **a)
        return res

def ambientLight(*p, **a):
        res = ALight(*p, **a)
        return res

def spotLight(*p, **a):
        res = SLight(*p, **a)
        return res