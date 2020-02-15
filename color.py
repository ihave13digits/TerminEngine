class Color:

    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def color(self):
        return (self.r, self.g, self.b, self.a)

    def __add__(self, c):
        return Color(self.clamp(self.r + c.r, 0, 255), self.clamp(self.g + c.g, 0, 255), self.clamp(self.b + c.b, 0, 255), self.clamp(self.a + c.a))

    def __sub__(self, c):
        return Color(self.clamp(self.r - c.r, 0, 255), self.clamp(self.g - c.g, 0, 255), self.clamp(self.b - c.b, 0, 255), self.clamp(self.a - c.a))

    @staticmethod
    def clamp(n, minv, maxv):
        return max(min(maxv, n), minv)

    @staticmethod
    def overflow(c):
        R, G, B, A = c.r, c.g, c.b, c.a
        if c.r > 255:
            val = round((c.r-255+.1)/2)
            R, G, B = c.r, G+val, B+val
        elif c.r < 0:
            val = int((c.r + c.r*2)/2)
            R, G, B = c.r, G+val, B+val
        if c.g > 255:
            val = round((c.g-255+.1)/2)
            R, G, B = R+val, c.g, B+val
        elif c.g < 0:
            val = int((c.g + c.g*2)/2)
            R, G, B = R+val, c.g, B+val
        if c.b > 255:
            val = round((c.b-255+.1)/2)
            R, G, B = R+val, G+val, c.b
        elif c.b < 0:
            val = int((c.b + c.b*2)/2)
            R, G, B = R+val, G+val, c.b
        return Color(Color.clamp(R, 0, 255), Color.clamp(G, 0, 255), Color.clamp(B, 0, 255), Color.clamp(A, 0, 255))

    def add(self, r=0, g=0, b=0, a=0):
        self.r += r
        self.g += g
        self.b += b
        self.a += a

    def sub(self, r=0, g=0, b=0, a=0):
        self.r -= r
        self.g -= g
        self.b -= b
        self.a -= a
