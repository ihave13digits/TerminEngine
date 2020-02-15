import os, sys

from draw import *
from palette import *

class Display:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = []
        self.clear_cmd = ""
        self.bg_char = "██"

        if sys.platform.startswith('win32'):
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'

        self.new_display()

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        size = (self.width, self.height)
        return size

    def clear(self):
        os.system(self.clear_cmd)

    def new_display(self):
        if len(self.matrix) > 0:
            self.matrix.clear()

        for y in range(self.height):
            for x in range(self.width):
                P = Pixel(x, y, 0, 0, 0, 0, self.bg_char)
                self.matrix.append(P)

    def get_matrix(self):
        for p in self.matrix:
            yield p

    def draw(self, x, y, r, g, b, a, char):
        mr = self.matrix[y*self.width+x].color.r
        mg = self.matrix[y*self.width+x].color.g
        mb = self.matrix[y*self.width+x].color.b
        ma = self.matrix[y*self.width+x].color.a
        if ma > 0 and a <= 0:
            R = mr
            G = mg
            B = mb
            A = ma
        elif (ma <= a and a > 0):
            R = r
            G = g
            B = b
            A = a
        else:
            A = int(( ma + a) /2)
            R = int((mr * ma) + (r * a)) / (ma + a)
            G = int((mg * ma) + (g * a)) / (ma + a)
            B = int((mb * ma) + (b * a)) / (ma + a)
            #R = int(( ((mr*ma)/255) + ((r*a)/255) ) /2)
            #G = int(( ((mg*ma)/255) + ((g*a)/255) ) /2)
            #B = int(( ((mb*ma)/255) + ((b*a)/255) ) /2)
        P = Pixel(x, y, R, G, B, A, char)
        try:
            self.matrix[(y * self.width) + x] = P
        except IndexError:
            pass

    def draw_sprite(self, sprite):
        for pxl in sprite.matrix:
            self.draw(pxl.position.x+sprite.position.x, pxl.position.y+sprite.position.y, pxl.color.r, pxl.color.g, pxl.color.b, pxl.color.a, pxl.char)

    def render(self):
        self.clear()
        for i, pxl in enumerate(self.get_matrix()):
                if i % self.width == 0:
                    print("")
                sys.stdout.write("\x1b[{};2;{};{};{}m".format(38, pxl.color.r, pxl.color.g, pxl.color.b) + pxl.char + '\x1b[0m')
        print("")
