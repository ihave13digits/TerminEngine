class SevenSegmentDisplay:

    def __init__(self, x, y, r, g, b, a, c="██"):
        self.width = 4
        self.height = 7
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.char = c
        self.matrix = []

    def refresh(self):
        self.matrix.clear()
        #for y in range(self.width):
        #    for x in range(self.height):
        #        self.matrix.append(Pixel(x, y, 0, 0, 0, self.a, self.char))

    def update(self, i):

        self.refresh()

        A = [[1+self.x, 0+self.y, self.r, self.g, self.b, self.a, self.char], [2+self.x, 0+self.y, self.r, self.g, self.b, self.a, self.char]]
        B = [[0+self.x, 1+self.y, self.r, self.g, self.b, self.a, self.char], [0+self.x, 2+self.y, self.r, self.g, self.b, self.a, self.char]]
        C = [[3+self.x, 1+self.y, self.r, self.g, self.b, self.a, self.char], [3+self.x, 2+self.y, self.r, self.g, self.b, self.a, self.char]]
        D = [[1+self.x, 3+self.y, self.r, self.g, self.b, self.a, self.char], [2+self.x, 3+self.y, self.r, self.g, self.b, self.a, self.char]]
        E = [[0+self.x, 4+self.y, self.r, self.g, self.b, self.a, self.char], [0+self.x, 5+self.y, self.r, self.g, self.b, self.a, self.char]]
        F = [[3+self.x, 4+self.y, self.r, self.g, self.b, self.a, self.char], [3+self.x, 5+self.y, self.r, self.g, self.b, self.a, self.char]]
        G = [[1+self.x, 6+self.y, self.r, self.g, self.b, self.a, self.char], [2+self.x, 6+self.y, self.r, self.g, self.b, self.a, self.char]]


        numbers = [
                [A, B, C, E, F, G],
                [C, F],
                [A, C, D, E, G],
                [A, C, D, F, G],
                [B, C, D, F],
                [A, B, D, F, G],
                [A, B, D, E, F, G],
                [A, C, F],
                [A, B, C, D, E, F, G],
                [A, B, C, D, F, G]
                ]

        for seg in numbers[i]:
            self.matrix.append(seg)
