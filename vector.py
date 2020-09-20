def coords_to_index(x, y, w, h):
    i = (y * w) + x
    return i

def vector_to_index(v, w, h):
    i = (v.y * w) + v.x
    return i

def index_to_vector(i, w, h):
    x = w % i
    y = w / i
    return Vector2(x, y)

def index_to_coords(i, w, h):
    x = 0
    y = 0
    if i > 0:
        x = w % i
        y = w / i
    return x, y

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Binary Operators

    def __add__(self, i):
        return Vector2((self.x + i.x),(self.y + i.y))

    def __sub__(self, i):
        return Vector2((self.x - i.x),(self.y - i.y))

    def __mul__(self, i):
        return Vector2((self.x * i.x),(self.y * i.y))

    def __truediv__(self, i):
        return Vector2((self.x / i.x),(self.y / i.y))
    
    def __floordiv__(self, i):
        return Vector2((self.x // i.x),(self.y // i.y))

    def __mod__(self, i):
        return Vector2((self.x % i.x),(self.y % i.y))

    def __pow__(self, i):
        return Vector2((self.x ** i.x),(self.y ** i.y))

    def __lshit__(self, i):
        return Vector2((self.x << i.x),(self.y << i.y))

    def __rshift__(self, i):
        return Vector2((self.x >> i.x),(self.y >> i.y))

    def __and__(self, i):
        return Vector2((self.x & i.x),(self.y & i.y))

    def __xor__(self, i):
        return Vector2((self.x ^ i.x),(self.y ^ i.y))

    def __or__(self, i):
        return Vector2((self.x | i.x),(self.y | i.y))

    # Extended Assignments

    def __iadd__(self, i):
        self.x += i.x
        self.y += i.y
        return Vector2(self.x, self.y)

    def __isub__(self, i):
        self.x -= i.x
        self.y -= i.y
        return Vector2(self.x, self.y)

    def __imul__(self, i):
        self.x *= i.x
        self.y *= i.y
        return Vector2(self.x, self.y)

    def __itruediv__(self, i):
        self.x /= i.x
        self.y /= i.y
        return Vector2(self.x, self.y)

    def __ifloordiv__(self, i):
        self.x //= i.x
        self.y //= i.y
        return Vector2(self.x, self.y)

    def __imod__(self, i):
        self.x %= i.x
        self.y %= i.y
        return Vector2(self.x, self.y)

    def __ipow__(self, i):
        self.x **= i.x
        self.y **= i.y
        return Vector2(self.x, self.y)

    def __ilshit__(self, i):
        self.x <<= i.x
        self.y <<= i.y
        return Vector2(self.x, self.y)

    def __irshift__(self, i):
        self.x >>= i.x
        self.y >>= i.y
        return Vector2(self.x, self.y)

    def __iand__(self, i):
        self.x &= i.x
        self.y &= i.y
        return Vector2(self.x, self.y)

    def __ixor__(self, i):
        self.x ^= i.x
        self.y ^= i.y
        return Vector2(self.x, self.y)

    def __ior__(self, i):
        self.x |= i.x
        self.y |= i.y
        return Vector2(self.x, self.y)

    # Unary Operators

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __pos__(self):
        return Vector2(+self.x, +self.y)

    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __invert__(self):
        return Vector2(~self.x, ~self.y)

    def __complex__(self):
        return Vector2(complex(self.x), complex(self.y))

    def __int__(self):
        return Vector2(int(self.x), int(self.y))

    def __long__(self):
        return Vector2(long(self.x), long(self.y))

    def __float__(self):
        return Vector2(float(self.x), float(self.y))

    def __oct__(self):
        return Vector2(oct(self.x), oct(self.y))

    def __hex__(self):
        return Vector2(hex(self.x), hex(self.y))

    # Comparison Operators

    def __lt__(self, i):
        if (self.x < i.x and self.y <= i.y) or (self.x <= i.x and self.y < i.y):
            return Vector2(self.x, self.y)

    def __le__(self, i):
        if self.x <= i.x and self.y <= i.y:
            return Vector2(self.x, self.y)

    def __eq__(self, i):
        if self.x == i.x and self.y == i.y:
            return Vector2(self.x, self.y)

    def __ne__(self, i):
        if self.x != i.x or self.y != i.y:
            return Vector2(self.x, self.y)

    def __ge__(self, i):
        if self.x >= i.x and self.y >= i.y:
            return Vector2(self.x, self.y)

    def __gt__(self, i):
        if (self.x > i.x and self.y >= i.y) or (self.x >= i.x and self.y > i.y):
            return Vector2(self.x, self.y)

    # Misc.

    def coords(self):
        return Vector2(self.x, self.y)
