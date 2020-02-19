class BitManager:

    def __init__(self, name, w=8, h=8):
        self.name = name
        self.width = w
        self.height = h
        self.bit_map = {}

    def load_bits(self, keys):
        self.bit_map = keys

    def bit_on(self, b, i):
        self.bit_map[b][i] = 1

    def bit_off(self, b, i):
        self.bit_map[b][i] = 0

    def bit_flip(self, b, i):
        self.bit_map[b][i] = not self.bit_map[b][i]

    def fill_bits(self, b, f=0):
        for i in range(len(self.bit_map[b])):
            self.bit_map[b][i] = f

    def add_map(self, name, f=0):
        self.bit_map[name] = []
        for i in range(self.width*self.height):
            self.bit_map[name].append(bool(f))
        print(self.bit_map[name])

    def save_map(self, bmap_dir):
        from os import path
        with open(path.join(bmap_dir, "{}.bmd".format(self.name)), 'w') as f:
            # Iterates through Characters
            for b in self.bit_map:
                line = "{}\n".format(b)
                # Saves BitMap Matrix
                for y in range(self.height):
                    for x in range(self.width):
                        if self.bit_map[b][(y*self.width)+x]:
                            data = "1"
                        else:
                            data = "0"
                        line += "{}{}".format(data, ",")
                    line += "\n"
                f.write(line)

    def load_map(self, bmap_dir):
        from os import path
        bit_map = {}
        with open(path.join(bmap_dir, "{}.bmd".format(self.name)), 'r') as f:
            txt = f.readlines()

            for line in txt:
                if line == "\n":
                    pass
                else:
                    if len(line) != (self.width*2)+1:
                        bit = line.strip()
                        bit_map[bit] = []
                    else:
                        for i in line:
                            if i.isdigit():
                                bit_map[bit].append(bool(int(i)))
            self.load_bits(bit_map)
            f.close()

class BitMask:

    def __init__(self, x, y, i, c):
        self.x = x
        self.y = y
        self.index = i
        self.char = c
        self.matrix = []

    def update(self, matrix):
        self.matrix = matrix

    def draw(self, manager, display, r, g, b, a):
        from vector import coords_to_index
        for y in range(manager.height):
            for x in range(manager.width):
                i = coords_to_index(x, y, manager.width, manager.height)
                if self.matrix[i] == True:
                    display.draw(x+self.x, y+self.y, r, g, b, a, self.char)
