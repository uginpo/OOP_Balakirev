# Создание клона класса


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)


pl = Point(1, 3)
