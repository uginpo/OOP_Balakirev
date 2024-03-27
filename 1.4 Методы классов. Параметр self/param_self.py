class Point:
    color = 'red'
    circle = 2

    def set_coord(self):  # self   ссылается на экземпляр класса (в данном случае a)
        print('your coordinate is')
        print(f'self= {id(self)}')


print(Point.color)

a = Point()
Point.set_coord(a)
print(a.color)
a.set_coord()
print(id(a))  # id a and self are equal
