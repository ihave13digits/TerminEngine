from sprite import *

class Draw:

    def __init__(self, r, g, b, a=255, c="██"):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.char = c
        self.sprites = []

    def line(self, X, Y, w, h):
        to_draw = Sprite(X, Y, w, h)
        for y in range(h):
            for x in range(h//w):
                pxl = Pixel(x+X, y+Y, self.r, self.g, self.b, self.a, self.char)
                to_draw.matrix.append(pxl)
        self.sprites.append(to_draw)

    def rect(self, x, y, w, h):
        to_draw = Sprite(x, y, w, h)
        to_draw.fill(self.r, self.g, self.b, self.a, self.char)
        self.sprites.append(to_draw)

