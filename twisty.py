# service definitions

F, B, L, R, U, D = 0, 1, 2, 3, 4, 5

class sticker():
    def __init__(self, layers):
        self.layers = layers

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

class axis():
    def __init__(self, name, layers):
        self.name = name  # is it necessary?
        self.layers = layers

class cube():
    def __init__(self, axises):
        self.axises = axises

class color():
    def __init__(self, stickers):
        self.stickers = stickers
        
class colorsheme():
    def __init__(self, colors):
        self.colors = colors


# maximum detailed description
# TODO automatic generation from minimal data

cube2x2x2 = (
    colorsheme([
        color([  # these stickers are replaceable when checking for solved
            sticker([F, U, L]),
            sticker([F, U, R]),
            sticker([F, D, R]),
            sticker([F, U, L]),
            ]),
        #TODO describe other colors
        ]),
    cube([
        axis([F, B], [
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
            ]),
        #TODO describe axis LR, UD
        ])
    )
