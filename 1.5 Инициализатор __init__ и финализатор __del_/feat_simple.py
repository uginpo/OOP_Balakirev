class Money:
    def __init__(self, money) -> None:
        self.money = money


class Point:
    def __init__(self, x, y, color='black') -> None:
        self.x = x
        self.y = y
        self.color = color
        pass


points = []
for i in range(1000):
    if i == 1:
        p = Point(2*i+1, 2*i+1, 'yellow')
    p = Point(2*i+1, 2*i+1)
    points.append(p)
