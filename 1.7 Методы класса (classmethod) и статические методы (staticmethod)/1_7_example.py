class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y) -> None:
        self.x = self.y = 0

        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(self.norm2(self.x, self.y))

    def get_coord(self):
        return self.x, self.y

    @staticmethod  # позводяет использовать эту функцию автономно
    def norm2(x, y):
        return x*x + y*y


a = Vector(1, 4)
a.get_coord()
print(Vector.get_coord(a))  # необходимо указывать экземпляр класса

print(Vector.validate(5))  # можно не указывать экземпляр класса
print(Vector.validate(500))  # можно не указывать экземпляр класса

a = Vector(1, 400)
print(a.get_coord())

print(Vector.norm2(2, 3))
