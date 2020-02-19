class BitMap:

    def __init__(self, name, w=8, h=8):
        self.name = name
        self.width = w
        self.height = h
        self.bit_map = {}
        self.next_index = 0
        self.current_index = 0

    def bit_on(self, b, i, clear_layers=True):
        if clear_layers:
            for layer in self.bit_map:
                self.bit_map[layer]['matrix'][i] = False
        self.bit_map[b]['matrix'][i] = True

    def bit_off(self, b, i, clear_layers=True):
        if clear_layers:
            for layer in self.bit_map:
                self.bit_map[layer]['matrix'][i] = False
        self.bit_map[b]['matrix'][i] = False

    def bit_flip(self, b, i, clear_layers=True):
        if clear_layers:
            for layer in self.bit_map:
                self.bit_map[layer]['matrix'][i] = False
        self.bit_map[b]['matrix'][i] = not self.bit_map[b]['matrix'][i]

    def fill_bits(self, b, f=0, clear_layers=True):
        for i in range(len(self.bit_map[b])):
            if clear_layers:
                for layer in self.bit_map:
                    self.bit_map[layer]['matrix'][i] = False
            self.bit_map[b]['matrix'][i] = bool(f)

    def add_layer(self, r, g, b, a, f=0):
        from color import Color
        self.bit_map[str(self.next_index)] = {
                'color' : Color(r, g, b, a),
                'matrix' : []
                }
        for i in range(self.width*self.height):
            self.bit_map[str(self.next_index)]['matrix'].append(bool(f))
        self.next_index += 1

    def save_map(self, bmap_dir):
        from os import path
        import pickle
        with open(path.join(bmap_dir, "{}.bmd".format(self.name)), 'wb') as f:
            pickle.dump(self.bit_map, f)
            f.close()

    def load_map(self, bmap_dir):
        from os import path
        import pickle
        bit_map = {}
        with open(path.join(bmap_dir, "{}.bmd".format(self.name)), 'rb') as f:
            self.bit_map = pickle.load(f)
            f.close()

    def draw(self, display):
        from vector import coords_to_index
        for layer in self.bit_map:
            for y in range(self.height):
                for x in range(self.width):
                    i = coords_to_index(x, y, self.width, self.height)

                    if self.bit_map[layer]['matrix'][i] == True:
                        display.color_draw(x, y, self.bit_map[layer]['color'], display.bg_char)
