from array import array
import math

class Vector2d:

    def __init__(self,x , y) -> None:
        self.x = float(x)
        self.y = float(y)


    def __iter__(self):
        return (i for i in (self.x, self.y))


    def __repr__(self) -> str:
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    
    def __str__(self) -> str:
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other) -> bool:
        if (self.x == other.x) and (self.y == other.y):
            return True
        else:
            return False

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    