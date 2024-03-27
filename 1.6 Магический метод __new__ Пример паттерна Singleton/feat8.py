# Создание разных классов в зависимости от внешней переменной
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
