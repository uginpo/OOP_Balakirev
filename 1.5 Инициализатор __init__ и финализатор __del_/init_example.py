class Point:
    color = 'red'
    circle = 2

    def __init__(self) -> None:
        self.x = 0
        self.y = 0

    def __del__(self):
        print(f'Deleting: {str(self)})')

    def set_coord(self, x=0, y=0):
        self.x = x
        self.y = y


print(Point.color)

a = Point()
print(a.x, a.y)  # id a and self are equal
print(a.color)
a.set_coord(2, 4)
print(a.x, a.y)  # id a and self are equal
