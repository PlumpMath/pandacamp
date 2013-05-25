#This all works and is fairly well commented.
#This could probably be incorporated into DynamicGeometry logically, but we'll see.
#Something noteworthy: unlike the coaster.py in the physics directory, this builds the
# roller-coaster from scratch without using the triangle method in DynamicGeometry.
#~Kendric 5-29-08

# More Darek code ...

from pandac.PandaModules import *
from direct.particles.Particles import *
from direct.particles.ParticleEffect import *
import direct.directbase.DirectStart
import math
from DynamicGeometry import GeometryHandle

def vertices(x, y, size):
    return y*(size+1)+x
def default2D(x,y):
    return (math.sin(x*3)+math.sin(y*3))/2

#based on the makeTerrain2D below.
def makeTerrain1D(end=10, width=1, size=60, func=math.sin, texture="/c/panda/lib/models/forestSky/m0cm0.png", repeat=True):
    format = GeomVertexFormat.getV3c4t2() #Set the format of the Side
    square = GeomVertexData('square', format, Geom.UHStatic) #Make the square Data holder
    vertex = GeomVertexWriter(square, 'vertex') #Grab the Vertex data to be manipulated
    color = GeomVertexWriter(square, 'color') #Grab the Color data to be manipulated
    texcoord = GeomVertexWriter(square, 'texcoord') #Grab Texture Coordinates to be manipulated
    node = GeomNode('terrain')
    piece = Geom(square) #Basically says create a new Geom using the provided data.
    for i in range(size+1):
        texX = i/float(size)
        x = texX*(end)
        x2 = ((i+1)/float(size))*end
        z = func(x)
        z2 = func(x2)
        if repeat:
            vertex.addData3f(x, 0, z)
            texcoord.addData2f(0, 0)
            vertex.addData3f(x, width, z)
            texcoord.addData2f(0, 1)
            vertex.addData3f(x2, 0, z2)
            texcoord.addData2f(1, 0)
            vertex.addData3f(x2, width, z2)
            texcoord.addData2f(1, 1)
        else:
            vertex.addData3f(x, 0, z)
            texcoord.addData2f(texX, 0)
            vertex.addData3f(x, width, z)
            texcoord.addData2f(texX, 1)
    for i in range(size):
        prim = GeomTriangles(Geom.UHStatic) #Make a new primitive object that is a triangle
        offset = 2
        prim.addVertices(offset*i, offset*i+1, offset*i+2)
        prim.closePrimitive() #I think this says "These are all the points in your primitive shut it down"
        piece.addPrimitive(prim)
        prim.addVertices(offset*i+1, offset*i+2, offset*i+3)
        prim.closePrimitive()
        piece.addPrimitive(prim)

    node.addGeom(piece)
    nodePath = render.attachNewNode(node)
    tex = g.loadTexture(loader, texture)
    nodePath.setTexture(tex)
    nodePath.setTwoSided(True)

    #Swiped from DynamicGeometry to allow the terrain to be used like a model.
    result = GeometryHandle(nodePath)
    return result

#This creates terrain based on the two dimensional function "func", with the texture filename of "texture"
#All of the pieces are culled from this file and the DynamicGeometry.py.
def makeTerrain2D(xEnd=3, yEnd=3, xSize=10, ySize=10, func=default2D, texture="/c/panda/lib/models/forestSky/m0cm0.png"):
    format = GeomVertexFormat.getV3c4t2() #Set the format of the Side
    square = GeomVertexData('square', format, Geom.UHStatic) #Make the square Data holder
    vertex = GeomVertexWriter(square, 'vertex') #Grab the Vertex data to be manipulated
    color = GeomVertexWriter(square, 'color') #Grab the Color data to be manipulated
    texcoord = GeomVertexWriter(square, 'texcoord') #Grab Texture Coordinates to be manipulated
    node = GeomNode('terrain')
    piece = Geom(square) #Basically says create a new Geom using the provided data.
    for i in range(xSize+1):
        for j in range(ySize+1):
            texX = i/float(xSize)
            texY = j/float(ySize)

            x = texX*(xEnd)
            y = texY*(yEnd)

            vertex.addData3f(x, y, func(x,y))# addData3f says get ready to grab 3 floats
            texcoord.addData2f(texX, texY)

    for i in range(xSize):
        for j in range(ySize):
            prim = GeomTriangles(Geom.UHStatic) #Make a new primitive object that is a triangle
            prim.addVertices(vertices(i,j,ySize), vertices(i,j+1,ySize), vertices(i+1,j,ySize))
            prim.closePrimitive() #I think this says "These are all the points in your primitive shut it down"
            piece.addPrimitive(prim)
            prim.addVertices(vertices(i,j+1,ySize), vertices(i+1,j+1,ySize), vertices(i+1,j,ySize))
            prim.closePrimitive()
            piece.addPrimitive(prim)

    node.addGeom(piece)
    nodePath = render.attachNewNode(node)
    tex = loadTexture(loader, texture)
    if tex == None:
        print "Texture file " + texture + " not found."
        exit()
    nodePath.setTexture(tex)
    nodePath.setTwoSided(True)

    #Swiped from DynamicGeometry to allow the terrain to be used like a model.
    result = GeometryHandle(nodePath)
    return result

def makeSide(xOne, yOne, zOne, xTwo, yTwo, zTwo, r = 0, g = 1, b = 0):
    format = GeomVertexFormat.getV3c4t2() #Set the format of the Side
    side = GeomVertexData('side', format, Geom.UHStatic) #Make the side Data holder

    vertex = GeomVertexWriter(side, 'vertex') #Grab the Vertex data to be manipulated
    color = GeomVertexWriter(side, 'color') #Grab the Color data to be manipulated
    texcoord = GeomVertexWriter(side, 'texcoord') #Grab Texture Coordinates to be manipulated

    #We will no initialize the points in space where the square will be.  The function takes in an x, y, z
    if xOne != xTwo:
        vertex.addData3f(xOne, yOne, zOne)# addData3f says get ready to grab 3 floats
        vertex.addData3f(xTwo, yOne, zTwo)
        vertex.addData3f(xTwo, yTwo, zTwo)
        vertex.addData3f(xOne, yTwo, zOne)

    else: #if the x values are the same then nothing will be drawn this fixes that
        vertex.addData3f(xOne, yOne, zOne)
        vertex.addData3f(xOne, yTwo, zOne)
        vertex.addData3f(xTwo, yTwo, zTwo)
        vertex.addData3f(xTwo, yOne, zTwo)

    #Now we will initalize the texture cordiants this will tell where the textures are supposed to go.
    #All of these are associated with the individual cornors and how the texture will be painted.
    #I am initializing the texcoords to be on the individual cornors of the square.
    texcoord.addData2f(1, 0) #addData2f says get ready for two floats
    texcoord.addData2f(1, 1)
    texcoord.addData2f(1, 0)
    texcoord.addData2f(0, 0)

    #Finally we will place in the color.  This is basically an optional thing.  Ia m doing it since we don't plan on using textures
    #In the case of this color scheme we will give an R,G,B,A.  However you can initalize a different format if you wish.
    color.addData4f(r, g, b, 1) #addData4f says I am taking four floats.
    color.addData4f(r, g, b, 1)
    color.addData4f(r, g, b, 1)
    color.addData4f(r, g, b, 1)
    #Now we will add the primitives.  These will actually be drawn onto the screen.
    #There are many different types of primities but for simplicity we will use triangles.
    #A triangle takes 3 points as they associate to the data in your GeomVertexData.  So be careful if you want to draw this properly
    primOne = GeomTriangles(Geom.UHStatic) #Make a new primitive object that is a triangle
    primOne.addVertex(0)
    primOne.addVertex(1)
    primOne.addVertex(2)
    primOne.closePrimitive() #I think this says "These are all the points in your primitve shut it down"

    primTwo = GeomTriangles(Geom.UHStatic)
    primTwo.addVertices(2, 3, 0) #Shorthand to add lots of vertexes in one fell swoop.
    primTwo.closePrimitive()

    #Now it is finally time to make the Geom.
    #I think a Geom is a special object in panda that draws the graphics
    square = Geom(side) #Basically says create a new Geom using the provided data.
    square.addPrimitive(primOne) #Add this primitive to the Geom
    square.addPrimitive(primTwo)

    #Finally return this Geom to be used by the program.
    return square

def makeCoasterSection(x = 0, y = .5, z = 0, ztwo = 0, delta = .1, re = 0, bl = 0, gr = 1):
    #sideOne = makeSide(x, y, z, x + delta, y, ztwo)
    #sideTwo = makeSide(x, -y, z, x + delta, -y, ztwo)
    sideThree = makeSide(x, y, z, x, -y, z, r = re, g = gr, b = bl)
    sideFour = makeSide(x + delta, y, ztwo, x + delta, -y, ztwo, r = re, g = gr, b = bl)
    sideFive = makeSide(x, y, z, x + delta, -y, ztwo, r = re, g = gr, b = bl)
    sideSix = makeSide(x, y, z, x + delta, -y, ztwo, r = re, g = gr, b = bl)

    node = GeomNode('coaster')
    #node.addGeom(sideOne)
    #node.addGeom(sideTwo)
    node.addGeom(sideThree)
    node.addGeom(sideFour)
    node.addGeom(sideFive)
    node.addGeom(sideSix)

    cube = render.attachNewNode(node)
    cube.setTwoSided(True)

def buildCoaster(funct, starter = 0, ender = 30, delta = .1):
    st = starter
    en = ender
    d = delta
    flip = False
    while st <= en:
        if flip:
            makeCoasterSection(x = st, z = funct(st), ztwo = funct(st + d), delta = d)
            flip = False
        else:
           makeCoasterSection(x = st, z = funct(st), ztwo = funct(st + d), delta = d, bl = 1, gr = 0)
           flip = True
        st = st + d
