from vector import *
from color import *

class Pixel:

    def __init__(self, x, y, r, g, b, a, c):
        self.position = Vector2(x, y)
        self.color = Color(r, g, b, a)
        self.char = c

    def get_pos(self):
        return Vector2(self.position.x, self.position.y)

    def get_col(self):
        return Color(self.color.r, self.color.g, self.color.b, self.color.a)

    def get_char(self):
        return self.char
