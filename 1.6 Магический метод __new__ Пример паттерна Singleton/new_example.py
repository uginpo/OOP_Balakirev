class Point:
    def __new__(cls, *args, **kwargs):
        print(f"I'm working -> {str(cls)}")
        # запускает процесс создания экземпляра класса
        return super().__new__(cls)

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


a = Point(1, 4)

print(a.x)

# Паттерн Singleton


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        DataBase.__instance = None

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")
