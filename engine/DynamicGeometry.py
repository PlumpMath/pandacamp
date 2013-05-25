import g

from Types import *
from Handle import *
from sys import exit
from Model import findTexture

class GeometryHandle(Handle):
    def __init__(self, object, position=None, hpr=None, size = 1, color = None, texture = None):
        Handle.__init__(self, name="dynamicGeometry")
        self.d.model = object
        g.nextModelId = g.nextModelId + 1
        self.d.model.setTag('rpandaid', str(g.nextModelId))
        self.d.onScreen = False
        ctl = newSignalRefd(self, "control", controlType, scEmptyControl)
        self.__dict__["control"] = ctl
        self.__dict__['position'] = newSignalRefd(self, 'position', P3Type, P3(0,0,0), ctl)
        self.__dict__['hpr']   = newSignalRefd(self, 'hpr', HPRType, HPR(0,0,0), ctl)
        self.__dict__['size'] = newSignalRefd(self, 'size', numType, 1, ctl)
        self.__dict__['color'] = newSignalRefd(self, 'color', ColorType, noColor, ctl)
        if size is not None:
             self.size.setBehavior(size)
        if position is not None:
             self.position.setBehavior(position)
        if hpr is not None:
             self.hpr.setBehavior(hpr)
        if color is not None:
             self.color.setBehavior(color)
        if texture is not None:
          tex = loader.loadTexture(findTexture(texture))
          self.d.model.setTexture(tex)
        g.newModels.append(self)
    def refresh(self):
        Handle.refresh(self)
        p = self.position.now()
        # print "Model position: " + str(p)
        self.d.model.setPos(p.x, p.y, p.z)
        d = self.hpr.now()
        self.d.model.setHpr(degrees(d.h), degrees(d.p), degrees(d.r))
        sz = self.size.now()
        self.d.model.setScale(sz)
        c = self.color.now()
        if c.a != 0:   # This signals that there is no color to paint on the model
           self.d.model.setColor(c.toVBase4())
    def kill():
        self.d.model.hide()
    def showModel(self):
        if not self.d.onScreen:
           # self.d.model.reparentTo(render)
           self.d.onScreen = True
    def show():
        self.d.model.show()
    def reparentTo(self, handle):
        self.d.model.reparentTo(handle.d.model)
    def setTexture(self, texture):
        tex = loader.loadTexture(findTexture(texture))
        self.d.model.setTexture(tex)
    def setTexture2(self, texture):
        if self.d.twoSided:
            self.d.sideTwo.setTexture(texture)

# This creates a model on the fly.  The array of spacePoints and texturePoints have to be the same length.
# The spacePoints contains P3 objects and texturePoints contains P2 objects.
# The triangles array contains triples of points, one for each triangle.
# The color is just a default - either color or texture override this.

def mesh(spacePoints, texturePoints, triangles, c):
#getV3c4t2() means 3-dimensional Vector, 4-dimensional Color and 2-dimensional Texture Coordinates.
    format = GeomVertexFormat.getV3c4t2()

#####I believe this provides a link of some sort to the Geom.UHStatic collection of vertices.
#####This seems to be a necessary step to making the shapes appear on the screen.
    vdata = GeomVertexData('name', format, Geom.UHStatic)

    vertex = GeomVertexWriter(vdata, 'vertex')
    normal = GeomVertexWriter(vdata, 'normal')
    color = GeomVertexWriter(vdata, 'color')
    texcoord = GeomVertexWriter(vdata, 'texcoord')
    for p in spacePoints:
        vertex.addData3f(p.x, p.y, p.z)
        color.addData4f(c.r, c.g, c.b, c.a)
    for p in texturePoints:
        texcoord.addData2f(p.x, p.y)
    geom = Geom(vdata)
    for triangle in triangles:

    #GeomTriangles contains a number of disconnected triangles, all apparently stored in a big pile.
        prim = GeomTriangles(Geom.UHStatic)

#####This seems to take the points we added in earlier and remove them.
#####Why this is all static, I don't understand.
        prim.addVertex(triangle[0])
        prim.addVertex(triangle[1])
        prim.addVertex(triangle[2])
        prim.closePrimitive()

    #Converting the vertices we just retrieved from the collection inside Geom.UHStatic into a node
#####
    
        geom.addPrimitive(prim)

    node = GeomNode('gnode')
    node.addGeom(geom)

    #Adds the node we've just made into the render path, therefore making it appear on screen.
#####I believe that if we want an actory-thing, this might be the place to do it.

    # nodePath = NodePath(node)
    # Not sure why this goes through render.  It makes the geometry visible too soon.
    # Can't reparent to render in showModel like a real model does.
    nodePath = render.attachNewNode(node)
    nodePath.setTwoSided(True)
    return nodePath

def emptyModel(color = None, position = None, hpr = None, size = None):
    nodePath = mesh([],[], [], white)
    result = GeometryHandle(nodePath, position, hpr, size, color, None)
    return result

def triangle(p1, p2, p3, color = None, position = None, hpr = None, size = None, texture = None, texP1 = P2(0,0), texP2 = P2(1, 0), texP3 = P2(0, 1), side2 = None):
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkKeyType("triangle", p1, P3Type, "p1")
    checkKeyType("triangle", p2, P3Type, "p2")
    checkKeyType("triangle", p3, P3Type, "p3")
    nodePath = mesh([p1, p2, p3], [texP1, texP2, texP3], [[0,1,2]], white)
    if (side2 is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position, hpr, size, color, texture)
        if side2 is not False:
            otherSide = triangle(p2, p1, p3, texture = side2, side2 = False, texP1 = texP1, texP2 = texP2, texP3 = texP3)
            otherSide.reparentTo(result)
            result.d.twoSided = True
            result.d.sideTwo = otherSide
        return result
    result = GeometryHandle(nodePath, position, hpr, size, color, texture)
    result.d.twoSided = False
    result.d.model.setScale(0)
    return result

def rectangle(p1, p2, p3, color = None, position=None, hpr=None, size=None, texture = None, side2 = None,
              texP1 = P2(0,0), texP2 = P2(1,0), texP3 = P2(0,1), texP4 = P2(1,1)):
    # If side2 is a string, it is interpreted as a file name in the pictures area
    # If side2 is False, the texture is one sided (invisible from the back)
    #checking to ensure that the second argument is an instance of the third argument
    #The first and fourth are for error handling.
    checkKeyType("rectangle", p1, P3Type, "p1")
    checkKeyType("rectangle", p2, P3Type, "p2")
    checkKeyType("rectangle", p3, P3Type, "p3")
    p4 = p3 + p2 - p1
    nodePath = mesh([p1, p2, p3, p4], [texP1, texP2, texP3, texP4], [[0,1,2], [2, 1, 3]], white)
    if (side2 is not None):
        nodePath.setTwoSided(False)
        result = GeometryHandle(nodePath, position, hpr, size, color, texture)
        if side2 is not False:  
            otherSide = rectangle(p2, p1, p4, texture = side2, side2 = False, texP1 = texP1, texP2 = texP2, texP3 = texP3, texP4 = texP4)
            otherSide.reparentTo(result)
            result.d.twoSided = True
            result.d.sideTwo = otherSide
        return result
    result = GeometryHandle(nodePath, position, hpr, size, color, texture)
    result.d.twoSided = False
    result.d.model.setScale(0)  # Hack - this is rendered too soon and we get 1 frame before update.  This keeps the model invisible
                                # until the first refresh
    return result

def unitSquare(**a):
    return rectangle(P3(-1, 0, -1), P3(1, 0, -1), P3(-1, 0, 1), **a)

def photoWheel(p, radius = 1.2, height = 1.2, **a):
    total = len(p)
    center = emptyModel(**a)
    for i in range(total):
      r = (2*pi/total)*i
      r2 = (2*pi/total)*(i+1)
      p1 = P3C(radius, r, height)
      p2 = P3C(radius, r, 0)
      p3 = P3C(radius, r2, 0)
      ph = rectangle(p2,p3,p1, texture = p[i])
      ph.reparentTo(center)
    return center

def cube(t1, t2, t3, t4, t5, t6, **a):
    center = emptyModel(**a)
    v1 = P3(1,1,1)
    v2 = P3(1,1,-1)
    v3 = P3(1, -1, 1)
    v4 = P3(1, -1, -1)
    v5 = P3(-1,1,1)
    v6 = P3(-1,1,-1)
    v7 = P3(-1, -1, 1)
    v8 = P3(-1, -1, -1)
    f1 = rectangle(v8, v4, v7, texture = t1)
    f2 = rectangle(v4, v2, v3, texture = t2)
    f3 = rectangle(v2, v6, v1, texture = t3)
    f4 = rectangle(v6, v8, v5, texture = t4)
    f5 = rectangle(v7, v3, v5, texture = t5)
    f6 = rectangle(v2, v6, v4, texture = t6)
    f1.reparentTo(center)
    f2.reparentTo(center)
    f3.reparentTo(center)
    f4.reparentTo(center)
    f5.reparentTo(center)
    f6.reparentTo(center)
    return center


def tetra(t1, t2, t3, t4, v1 = P3(-1, -1, -1), v2 = P3(1,-1,-1),v3 = P3(0, 1, -1), v4 = P3(0, 0, 1),  **a):
    center = emptyModel(**a)
    f1 = triangle(v1, v2, v4, texture = t1, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f2 = triangle(v2, v3, v4, texture = t2, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f3 = triangle(v3, v1, v4, texture = t3, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f4 = triangle(v1, v2, v3, texture = t4, texP1 = P2(0,0), texP2 = P2(0,1), texP3 = P2(.5, 1))
    f1.reparentTo(center)
    f2.reparentTo(center)
    f3.reparentTo(center)
    f4.reparentTo(center)
    return center

def slicePicture(p, w, h, **a):
    center = emptyModel(**a)
    res = []
    xsz = 1.0/w
    ysz = 1.0/h
    for x in range(w):
        for y in range(h):
            ll = P2(x*xsz, y*ysz)
            lr = P2((x+1)*xsz, y*ysz)
            ul = P2(x*xsz, (y+1)*ysz)
            ur = P2((x+1)*xsz, (y+1)*ysz)
            r = rectangle(P3(2*x*xsz-1, 0, 2*y*ysz-1), (P3(2*(x+1)*xsz-1, 0, 2*y*ysz-1)),
                          P3(2*x*xsz-1, 0, 2*(y+1)*ysz-1), texP1 = ll, texP2 = lr, texP3 = ul, texP4 = ur, texture = p)
            r.reparentTo(center)
            r.location = static(P3(2*(x+.5)*xsz-1, 0, 2*(y+.5)*ysz-1))
            res.append(r)
    return (center, res)


