DEBUG = True

# service definitions

F, B, L, R, U, D = 0, 1, 2, 3, 4, 5

class sticker():
    def __init__(self, layers):
        self.layers = layers

class color():
    def __init__(self, stickers):
        self.stickers = stickers

class elem():
    def __init__(self, stickers):
        self.stickers = stickers

class cycle():  # cyclic shift to emulate rotation
    def __init__(self, elems):
        self.elems = elems

class layer():
    def __init__(self, name, cycles):
        self.name = name
        self.cycles = cycles

class cube():
    def __init__(self, colors, layers):
        self.colors = colors
        self.layers = layers
        
class lesscube():
    def __init__(self, adjacentLayers, kindStickers):
        self.adjacentLayers = adjacentLayers
        self.kindStickers = kindStickers

# less detailed description
lesscube2x2x2 = lesscube([
    adjacentToLayer(F, [U, R, D, L]), #each subsequent layer should be adjacent
    adjacentToLayer(B, [U, R, D, L]),
    adjacentToLayer(L, [U, F, D, B]),
    adjacentToLayer(R, [U, F, D, B]),
    adjacentToLayer(U, [F, R, B, L]),
    adjacentToLayer(D, [F, R, B, L]),
    ],[
    kindSticker("corner", 3)
    ])
    
def toDetailed(lesscube):
    pass


# maximum detailed description
# TODO automatic generation from minimal data

cube2x2x2 = cube([
    color([  # these stickers are replaceable when checking for solved
        sticker([F, U, L]),
        sticker([F, U, R]),
        sticker([F, D, R]),
        sticker([F, U, L]),
        ]),
    #TODO describe other colors
    ],[
    layer(F, [
        cycle([  # example with a 45-degree rotation
            elem([
                sticker([F, U, L])
                ]),
            elem([
                sticker([F, U, L]),
                sticker([F, U, R])
                ]),
            elem([
                sticker([F, U, R])
                ]),
            elem([
                sticker([F, U, R]),
                sticker([F, D, R])
                ]),
            elem([
                sticker([F, D, R])
                ]),
            elem([
                sticker([F, D, R]),
                sticker([F, D, L])
                ]),
            elem([
                sticker([F, D, L])
                ]),
            elem([
                sticker([F, D, L]),
                sticker([F, U, L])
                ]),
            ]),
        cycle([
            elem([
                sticker([U, L, F])
                ]),
            elem([
                sticker([U, R, F])
                ]),
            elem([
                sticker([D, R, F])
                ]),
            elem([
                sticker([D, L, F])
                ]),
            ]),
        cycle([
            elem([
                sticker([L, F, U])
                ]),
            elem([
                sticker([R, F, U])
                ]),
            elem([
                sticker([R, F, D])
                ]),
            elem([
                sticker([L, F, D])
                ]),
            ]),
        ]),
    layer(B, [
        cycle([
            elem([
                sticker([B, U, L])
                ]),
            elem([
                sticker([B, U, R])
                ]),
            elem([
                sticker([B, D, R])
                ]),
            elem([
                sticker([B, D, L])
                ]),
            ]),
        cycle([
            elem([
                sticker([U, L, B])
                ]),
            elem([
                sticker([U, R, B])
                ]),
            elem([
                sticker([D, R, B])
                ]),
            elem([
                sticker([D, L, B])
                ]),
            ]),
        cycle([
            elem([
                sticker([L, B, U])
                ]),
            elem([
                sticker([R, B, U])
                ]),
            elem([
                sticker([R, B, D])
                ]),
            elem([
                sticker([L, B, D])
                ]),
            ]),
        ]),
    #TODO describe layers: L, R, U, D
    ])



# definition actions

def getLayer(cube, nameLayer):
    for layer in cube.layers:
        if nameLayer == layer.name:
            return layer
if DEBUG: print("layer:", getLayer(cube2x2x2, F))
        
def shift(elems):
    temp = elems[0]
    for i in range(len(elems) - 1):
        elems[i] = elems[i + 1]
    elems[-1] = temp
    return elems
if DEBUG: print("[1, 2, 0]:", shift([0,1,2]))

def move(cube, nameLayer):
    layer = getLayer(cube, nameLayer)
    for cycle in layer.cycles:
        #TODO checking for the possibility
        cycle.elems = shift(cycle.elems)
    return cube
if DEBUG: print("cube:", move(cube2x2x2, F))

def runAlg(cube, alg):
    for nameLayer in alg:
        cube = move(cube, nameLayer)
    return cube
if DEBUG: print("cube:", runAlg(cube2x2x2, [F, B]))

def nextNameLayer(predNameLayer, namesLayers):
    isReturn = False
    for nameLayer in namesLayers:
        if isReturn:
            return nameLayer
        if nameLayer == predNameLayer:
            isReturn = True
    return namesLayers[0]
if DEBUG: print("1:", nextNameLayer(F, [F, B]))

def nextAlg(predAlg, namesLayers): #TODO constraint 4 rotates
    result = []
    transfer = True
    for i in range(len(predAlg)):
        head = predAlg[i]
        tail = predAlg[i+1:]
        if transfer:
            nextHead = nextNameLayer(head, namesLayers)
            if nextHead != namesLayers[0]:
                transfer = False
            result += [nextHead]
        else:
            result += [head]
    if transfer:
        result += [0]
    return result
if DEBUG:
    print("[0]:", nextAlg([], [F,B]))
    print("[1]:", nextAlg([F], [F,B]))
    print("[0, 0]:", nextAlg([B], [F,B]))
    print("[0, 1]:", nextAlg([B,F], [F,B]))
    print("[0, 0, 0]:", nextAlg([B,B], [F,B]))

def diff(cube1, cube2):
    pass
