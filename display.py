from os import system
from sys import platform, stdout

from palette import *

class Display:

    def __init__(self, width, height, fr=0, fg=0, fb=0):
        self.width = width
        self.height = height
        self.matrix = []
        self.clear_cmd = ""
        self.bg_char = "██"
        self.fr = fr
        self.fg = fg
        self.fb = fb

        if platform.startswith('win32'):
            self.clear_cmd = 'cls'
        else:
            self.clear_cmd = 'clear'

        self.refresh()

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def get_size(self):
        size = (self.width, self.height)
        return size

    def set_console_size(self, x, y):
        pass
        #import os
        #os.environ['COLUMNS'] = x
        #os.environ['LINES'] = y

    def get_console_size(self):
        from os import get_terminal_size
        line = str(get_terminal_size())
        x = ""
        y = ""
        z = 0
        for c in line:
            if c == " ":
                z += 1
            if c.isdigit() == True:
                if z == 0:
                    x += c
                if z == 1:
                    y += c
        return Vector2(int(x), int(y))
        #return Vector2(int(environ['COLUMNS']), int(environ['LINES']))
        
    def get_console_info(self):
        self.clear()
        import os
        for key in os.environ:
            print(":{}   :\n{}\n\n".format(key, os.environ[key]))
        input("\n: Press 'Enter' to continue.")

    def clear(self):
        system(self.clear_cmd)

    def refresh(self):
        self.clear()
        if len(self.matrix) > 0:
            self.matrix.clear()

        for y in range(self.height):
            for x in range(self.width):
                P = Pixel(x, y, self.fr, self.fg, self.fb, 0, self.bg_char)
                self.matrix.append(P)

    def get_matrix(self):
        for p in self.matrix:
            yield p

    def color_draw(self, x, y, c, char):
        mr = self.matrix[y*self.width+x].color.r
        mg = self.matrix[y*self.width+x].color.g
        mb = self.matrix[y*self.width+x].color.b
        ma = self.matrix[y*self.width+x].color.a
        if c.a == 255:
            R = c.r
            G = c.g
            B = c.b
            A = c.a
        else:
            A = int(( ma + c.a) /2)
            R = int(( ((mr*ma)/255) + ((c.r*c.a)/255) ) /2)
            G = int(( ((mg*ma)/255) + ((c.g*c.a)/255) ) /2)
            B = int(( ((mb*ma)/255) + ((c.b*c.a)/255) ) /2)
        P = Pixel(x, y, int(R), int(G), int(B), int(A), char)
        try:
            self.matrix[(y * self.width) + x] = P
        except IndexError:
            pass

    def draw(self, x, y, r, g, b, a, char):
        mr = self.matrix[y*self.width+x].color.r
        mg = self.matrix[y*self.width+x].color.g
        mb = self.matrix[y*self.width+x].color.b
        ma = self.matrix[y*self.width+x].color.a
        #if ma > 0 and a <= 0:
        #    R = mr
        #    G = mg
        #    B = mb
        #    A = ma
        if a == 255:
            R = r
            G = g
            B = b
            A = a
        else:
            A = int(( ma + a) /2)
            #R = int((mr * ma) + (r * a)) / (ma + a)
            #G = int((mg * ma) + (g * a)) / (ma + a)
            #B = int((mb * ma) + (b * a)) / (ma + a)
            R = int(( ((mr*ma)/255) + ((r*a)/255) ) /2)
            G = int(( ((mg*ma)/255) + ((g*a)/255) ) /2)
            B = int(( ((mb*ma)/255) + ((b*a)/255) ) /2)
        P = Pixel(x, y, int(R), int(G), int(B), int(A), char)
        try:
            self.matrix[(y * self.width) + x] = P
        except IndexError:
            pass

    def draw_sprite(self, sprite):
        for pxl in sprite.matrix:
            self.draw(pxl.position.x+sprite.position.x, pxl.position.y+sprite.position.y, pxl.color.r, pxl.color.g, pxl.color.b, pxl.color.a, pxl.char)

    def render(self):
        for i, pxl in enumerate(self.get_matrix()):
                if i % self.width == 0:
                    print("")
                stdout.write("\x1b[{};2;{};{};{}m".format(38, pxl.color.r, pxl.color.g, pxl.color.b) + pxl.char + '\x1b[0m')
        print("")
