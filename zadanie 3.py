class Vector2D:
    def __init__(self, x, y):
        self.x = x if isinstance(x, (int, float)) else 0
        self.y = y if isinstance(y, (int, float)) else 0

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vector2D(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector2D' and '{}'".format(type(other)))

    def __radd__(self, other):
        # Obsługa dodawania krotki (x, y) do wektora (krotka jako lewy operand)
        if isinstance(other, tuple) and len(other) == 2:
            return Vector2D(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and 'Vector2D'".format(type(other)))





v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)

result1 = v1 + v2
print(result1)

result2 = v1 + (5, 3)
print(result2)

result3 = (5, 3) + v1
print(result3)
