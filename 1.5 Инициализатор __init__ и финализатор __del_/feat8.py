class Cart():
    def __init__(self) -> None:
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{x.name}: {x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price


gd_table1 = Table('Ольха', 200)
gd_table2 = Table('Дуб', 500)

gd_tv = TV('Sony', 2000)

gd_tv = Notebook('MacPro', 35000)

gd_cup1 = Cup('Чайная', 150)
gd_cup2 = Cup('Кофейная', 320)

a = Cart()
a.add(gd_table1)
a.add(gd_table2)
print(a.get_list())
