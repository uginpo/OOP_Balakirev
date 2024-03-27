class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Mistake! You can't create objects of this class"


a = AbstractClass()
# print(a)


class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):
        # Создается только 5 экземпляров класса. Остальные ссылаются на пятый.
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
        return cls.__instance

    def __init__(self, name) -> None:
        self.name = name


objs = [SingletonFive(str(i)) for i in range(6)]

# for elem in objs:
#    print(id(elem))
TYPE_OS = 1  # 1 - Windows, 2 - Linux


class DialogWindows:
    name_class = 'DialogWindows'


class DialogLinux:
    name_class = 'DialogLinux'


class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = None
        if TYPE_OS == 1:
            obj = super().__new__(DialogWindows)  # type: ignore
        else:
            obj = super().__new__(DialogLinux)  # type: ignore

        obj.name = args[0]  # так тоже можно, хоть и криво

        return obj


dl = Dialog('main')
print(dl.name)
