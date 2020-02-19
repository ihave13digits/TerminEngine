from os import path

from vector import coords_to_index

class Font:

    def __init__(self, name, w=5, h=7):
        self.name = name
        self.width = w
        self.height = h
        self.key_map = {}
        self.new()

    def load_keys(self, keys):
        self.key_map = keys

    def bit_on(self, letter, i):
        self.key_map[letter][i] = 1

    def bit_off(self, letter, i):
        self.key_map[letter][i] = 0

    def bit_flip(self, letter, i):
        self.key_map[letter][i] = not self.key_map[letter][i]

    def fill_bits(self, letter, f=0):
        for i in range(len(self.key_map[letter])):
            self.key_map[letter][i] = f

    def new(self):
        numbers = "0123456789"
        symbols = "@#$%^&*(){}[]<>:;|\/\"'`~_-+=?!., "
        lletters = "abcdefghijklmnopqrstuvwxyz"
        cletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for n in numbers:
            self.key_map[n] = []
            for i in range(self.width * self.height):
                self.key_map[n].append(True)
        for s in symbols:
            self.key_map[s] = []
            for i in range(self.width * self.height):
                self.key_map[s].append(True)
        for ll in lletters:
            self.key_map[ll] = []
            for i in range(self.width * self.height):
                self.key_map[ll].append(True)
        for cl in cletters:
            self.key_map[cl] = []
            for i in range(self.width * self.height):
                self.key_map[cl].append(True)

    def save_font(self, font_dir):
        with open(path.join(font_dir, "{}.bmd".format(self.name)), 'w') as f:
            # Iterates through Characters
            for letter in self.key_map:
                line = "{}\n".format(letter)
                # Saves Character Matrix
                for y in range(self.height):
                    for x in range(self.width):
                        if self.key_map[letter][(y*self.width)+x]:
                            data = "1"
                        else:
                            data = "0"
                        line += "{}{}".format(data, ",")
                    line += "\n"
                f.write(line)

    def load_font(self, font_dir):
        key_map = {}
        with open(path.join(font_dir, "{}.bmd".format(self.name)), 'r') as f:
            txt = f.readlines()

            for line in txt:
                if line == "\n":
                    pass
                else:
                    if len(line) == 2:
                        key = line.strip()
                        key_map[key] = []
                    elif len(line) > 2:
                        for i in line:
                            if i.isdigit():
                                key_map[key].append(bool(int(i)))
            self.load_keys(key_map)
            f.close()

class Character:

    def __init__(self, x, y, i, c):
        self.x = x
        self.y = y
        self.index = i
        self.char = c
        self.matrix = []

    def update(self, matrix):
        self.matrix = matrix

    def draw(self, font, display, r, g, b, a):
        for y in range(font.height):
            for x in range(font.width):
                i = coords_to_index(x, y, font.width, font.height)
                if self.matrix[i] == True:
                    display.draw(x+self.x, y+self.y, r, g, b, a, self.char)
