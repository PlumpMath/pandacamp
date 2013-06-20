import math
from DynamicGeometry import *
from Color import *
from Sound import *
from FRP import *



# txt is the file name, modname is the name of the Python module contain functions which elaborate maze objects


class RaceTile:
    def __init__(self, pushBackFriction, turnFriction, solid, letter):
        self.pushBackFriction = pushBackFriction
        self.turnFriction =turnFriction
        self.solid = solid
        self.letter = letter


class Racetrack:
    def __init__(self, txt, checkered = True, model = None, defaultTile = "x"):
        # for now the track will only have one object interacting with it
        meshpts = [] # Points in the mesh
        meshtri = [] # Triangles in the mesh
        meshcol = [] # Colors in the mesh
        meshtxt = [] # Texture coords in the mesh
        def rect(x, y, z, right, up, tile):
            color = grayShade(randomRange(.7, 1)) if checkered else white
            p1 = P3(x-.5, y-.5, z)
            p2 = p1 + right
            p3 = p1 + up
            p4 = p3 + p2 - p1
            n = len(meshpts)
            meshpts.extend([p1, p2, p3, p4])
            texp1 = P2(tile.texXMin, 0)
            texp2 = P2(tile.texXMax, 0)
            texp3 = P2(tile.texXMin, 1)
            texp4 = texp3 + texp2 - texp1
            meshtxt.extend([texp1, texp2, texp3, texp4])
            meshtri.extend([[n,n+1,n+2], [n+2, n+1, n+3]])
            meshcol.extend([color, color, color, color])
        def block(x, y, tile):
            rect(x, y, 0, P3(1, 0, 0), P3(0,0,1), tile)
            rect(x+1, y, 0, P3(0, 1, 0), P3(0,0,1), tile)
            rect(x+1, y+1, 0, P3(-1, 0, 0), P3(0,0,1), tile)
            rect(x, y+1, 0, P3(0, -1, 0), P3(0,0,1), tile)
            rect(x, y, 1, P3(1, 0, 0), P3(0, 1, 0), tile)
# This creates a colored floor rectangle. If no color is given then gray is used.
        def floorRect(x, y, tile):
            rect(x, y, 0, P3(1, 0, 0), P3(0,1,0), tile)


        self.model = model
        # reactive score
        self.score = var(0)
        # for ease of checkering
        # the key is the letter, the value is a list of attributes (for now the default texture image, surface friction, and centripetal force friction)
        self.tiles = {}
        t = [
             RaceTile(0.85,0.85, False, "d"),   # dirt
             RaceTile(0.95,0.75, False, "g"),   # grass
             RaceTile(0,0, False, "w"),         # Water
             RaceTile(0.95,0.95, True, "x"),    # Wall
             RaceTile(0.45,0.35, False, "r")]   # road

        nt = len(t)
        i = 0.0
        for tile in t:
            tile.texXMin = i/nt + .01
            tile.texXMax = (i+1)/nt - .01
            self.tiles[tile.letter] = tile
            i = i + 1
        self.tiles[" "] = self.tiles[defaultTile]
        #read the txt and store it's size>>
        self.filename = txt
        self.type = "maze"
        fileLoader = open(txt,  "r")
        contents = fileLoader.read().split("\n")
        self.ymax = len(contents)  # Height is the number of lines
        self.xmax = 0  # Take a running max over line lenths
        for r in contents:
            self.xmax = max(self.xmax,len(r))
        self.chars = []
        self.objects = []

        #expand arrays.  These are all 2-D arrays stored as [x][y]
        for x in range(self.xmax):
            self.chars.append([]) # The character at each location
            self.objects.append([])  # The Panda object at each location
            for y in range(self.ymax):
                   self.chars[x].append(" ")
                   self.objects[x].append(None)

        #populate  char array

        s = set()
        for y in range(self.ymax):
            line = contents[y]
            for x in range(self.xmax):
                #if cn >= len(l):
                if x < len(line):
                    #c = "r"
                #else:
                    c = line[x]
                    if c in self.tiles:
                        feature = self.tiles[c]
                    else:
                        print "Unknown feature in racetrack: " + c
                        feature = self.tiles["d"]
                    self.objects[x][y] = feature
                    if feature.solid:
                        block(x, y, feature)
                    else:
                        floorRect(x, y, feature)
        trackMesh = mesh(meshpts, meshtxt, meshtri, meshcol)
        self.trackModel = GeometryHandle(trackMesh, position = P3(0,0,0), hpr = HPR(0,0,0), size = 1, texture = "track.jpg")



    # Returns the friction of the current surface
    def sFriction(self, p):
        try:
            tile = self.objects[int(p.x+.5)][int(p.y+.5)]
        except:
            return 0
        if tile is None:
            return 0
        return tile.pushBackFriction

    # Lift friction!
    def friction(self, s):
        return (lift(lambda p:self.sFriction(p), "friction", [P3Type], numType))(s)

    # Returns the centripetal force of the current surface
    def sCent(self, p):
        try:
            tile = self.objects[int(p.x+.5)][int(p.y+.5)]
        except:
            return 0
        if tile is None:
            return 0
        return tile.turnFriction


    # Lift centripetal!
    def cent(self, s):
        return (lift(lambda p:self.sCent(p), "cent", [P3Type], numType))(s)

    # This is used for cube collision
    # Should check for z
    def sinWall(self, cr, size, p):
        r = cr*size
        x = int(p.x+.5)
        y = int(p.y+.5)
        lx = p.x - x + .5
        ly = p.y - y + .5
        if x < 1 or x > self.xmax-1 or y < 1 or y > self.ymax-1:
            return True
        if p.z > 1:
            return False

        c = self.objects[x][y]
        if c.solid:
            return True
        n = self.objects[x][y-1]
        if n.solid and ly - r < 0:
            return True
        s = self.objects[x][y+1]
        if s.solid and ly + r > 1:
            return True
        e = self.objects[x+1][y]
        if e.solid and lx + r > 1:
            return True
        w = self.objects[x-1][y]
        if w.solid and lx - r < 0:
            return True
        return False


    def inWall(self, m):
        return (lift(lambda cr,size,pos:self.sinWall(cr,size,pos), "inwall", [numType,numType,P3Type], boolType))(m.cRadius,m.size,m.position)

    def getRandomLoc(self):
        while(True):
            x = randomInt(self.xmax-1)
            y = randomInt(self.ymax-1)
            o = self.objects[x][y]
            if o is not None and not o.solid:
                break
        return P3(x,y,0)

    def placeObj(self, texture, position = None, size = 0.2, duration = 10000, score = 0, reaction = None, sound = None):
        if position == None:
            position = self.getRandomLoc()
        obj = rectangle(P3(-size/2,0,0), P3(size/2,0,0), P3(-size/2,0,size), position = position, texture = texture, hpr = integral(HPR(pi/4,0,0)), duration = duration)

        def reactToHit(m,v):
            if sound != None:
                play(sound)
            self.score.add(score)
            obj.exit()
            #print "HIT!"
            if reaction != None:
                reaction(self.model,self)

        obj.when(dist(self.model.position,obj.position) < (self.model.cRadius*self.model.size)+size, reactToHit)


    def item(self, name, pos, hpr0 = HPR(0,0,0), size = 0.2, action = None):
        if action == "bounce":
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0),hpr=hpr0)
        elif action == "spin":
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0))
        elif action == "both":
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0))
        else:
            item = rectangle(pos,pos+P3(0,size,0),pos+P3(0,0,size),texture = name, color = Color(0,0,0,0))
        items.append(item)
        return items[-1]


def ground(x, y, image, rotation):
    #return rectangle(P3(x,y+rotation,0), P3(x+rotation,y+1,0), P3(x+1,y,0), color = Color(240,240,240,rotation))
    col = 100+(100*rotation)
    #print col
    # the checkerboard coloring doesn't work. is there a bug in the color interpolation code?
    return rectangle(P3(x,y+rotation,0), P3(x+rotation,y+1,0), P3(x+(1+rotation)%2,y,0), texture = image, color = Color(col,col,col))



# racetrack item list
items = []
questionBlock = "questionBlock.JPG"
boost = "boost.png"
charge = "charge.png"
defense = "defense.png"
glide = "glide.png"
hp = "hp.png"
offense = "offense.png"
speed = "speed.png"
turn = "turn.png"
weight = "weight.png"
coin = "coinTnsp.png"

# item actions
bounce = "bounce"
spin = "spin"
both = "both"