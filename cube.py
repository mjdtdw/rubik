#Color
White = 0
Yellow = 1
Orange = 2
Red = 3
Green = 4 
Blue = 5

#Piece
Up = 0
Down = 1
Left = 2
Right = 3
Front = 4
Back = 5
UpFL = 0
UpFR = 1
UpBL = 2
UpBR = 3
DownFL = 4
DownFR = 5
DownBL = 6
DownBR = 7
LeftFU = 8
LeftFD = 9
LeftBU = 10
LeftBD = 11
RightFU = 12
RightFD = 13
RightBU = 14
RightBD = 15
FrontUL = 16
FrontUR = 17
FrontDL = 18
FrontDR = 19
BackUL = 20
BackUR = 21
BackDL = 22
BackDR = 23

class Cube:
    def __init__(self, stickers, pieces, groups, blocks):
        self.stickers = stickers
        self.pieces = pieces #только для наглядности
        self.groups = groups
        self.blocks = blocks
    
cube1x1x1 = Cube([White, Yellow, Orange, Red, Green, Blue],
                 [Up, Down, Left, Right, Front, Back],
                 [ [ [Up, Back, Down, Front] ],
                     [ [Up, Right, Down, Left] ],
                     [ [Front, Right, Back, Left] ] ],
                 [])
                 
cube2x2x2 = Cube([White, White, White, White, Yellow, Yellow, Yellow, Yellow,
                    Orange, Orange, Orange, Orange, Red, Red, Red, Red,
                    Green, Green, Green, Green, Blue, Blue, Blue, Blue],
                 [UpFL, UpFR, UpBL, UpBR, DownFL, DownFR, DownBL, DownBR,
                    LeftFU, LeftFD, LeftBU, LeftBD, RightFU, RightFD, RightBU, RightBD,
                    FrontUL, FrontUR, FrontDL, FrontDR, BackUL, BackUR, BackDL, BackDR],
                 [ [ [UpFL, BackUL, DownBL, FrontDL],
                       [UpFR, BackUR, DownBR, FrontDR],
                       [UpBL, BackDL, DownFL, FrontUL],
                       [UpBR, BackDR, DownFR, FrontUR],
                       [LeftFU, LeftBU, LeftBD, LeftFD],
                       [RightFU, RightBU, RightBD, RightFD] ],
                     [ [UpFL, RightFU, DownFR, LeftFD],
                       [UpFR, RightFD, DownFL, LeftFU],
                       [UpBL, RightBU, DownBR, LeftBD],
                       [UpBR, RightBD, DownBL, LeftBU],
                       [FrontUL, FrontUR, FrontDR, FrontDL],
                       [BackUL, BackUR, BackDR, BackDL] ],
                     [ [UpFL, BackUL, DownBL, FrontDL],
                       [UpBL, BackDL, DownFL, FrontUL],
                       [LeftFU, LeftBU, LeftBD, LeftFD] ] ],
                     [])

def show(cube):
    res = cube.stickers
    src = ["White", "Yellow", "Orange", "Red", "Green", "Blue"]
    for i in range(len(res)):
        res[i] = src[res[i]]
    return res
                 
def flat(xxs):
    res = []
    for xs in xxs:
        for x in xs: 
            res += [x]
    return res

def alienElem(checked, checker):
    for c in checked:
        if c not in checker:
            return False
    return True

def checkBlocked(group, blocks):
    alienElem(flat(group), flat(blocks))
    
def shift(group):
    return group[1:] + [group[0]]

def glue(xs, ys):
    res = []
    for i in range(len(xs)):
        res += [(xs[i], ys[i])]
    return res

def get(glues, stickers):
    res = []
    for i in range(len(stickers)):
        for (iFrom, iDest) in glues:
            if iFrom == i:
                res += [(iDest, stickers[i])]
    return res

def new(saved, stickers):
    res = []
    for i in range(len(stickers)):
        isWrite = False
        for (iDest, sticker) in saved:
            if i == iDest:
                res += [sticker]
                isWrite = True
        if isWrite == False:
            res += [stickers[i]]
    return res
    
def perm(group, stickers):
    glues = glue(group, shift(group))
    saved = get(glues, stickers)
    res = new(saved, stickers)
    return res
    
def multiperm(group, stickers):
    for g in group:
        stickers = perm(g, stickers)
    return stickers
                 
def rotate(n, cube):
    group = cube.groups[n]
    if checkBlocked(group, cube.blocks):
        False
    else:
        cube.stickers = multiperm(group, cube.stickers)
    return cube
        
print(show(rotate(1, cube2x2x2)))
