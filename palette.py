from draw import *

class Palette:

    def __init__(self):
        self.char = "██"
        self.colors = []
        self.brushes = []

    def add_color(self, r, g, b, a):
        c = Color(r, g, b, a)
        self.colors.append(c)

    def insert_color(self, r, g, b, a, index):
        self.colors.insert(index, Color(r, g, b, a))

    def set_colors(self):
        for c in self.colors:
            brush = Draw(c.r, c.g, c.b, c.a, self.char)
            self.brushes.append(brush)
