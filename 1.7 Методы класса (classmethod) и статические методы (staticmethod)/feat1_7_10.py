class AppStore:
    def __init__(self) -> None:
        self.apps = {}

    def add_application(self, app):
        self.apps[id(app)] = app

    def remove_application(self, app):
        self.apps.pop(id(app))

    def block_application(self, app):
        obj = self.apps.get(id(app), False)
        if not obj:
            return False
        obj.bloced = True
        return obj.blocked

    def total_application(self):
        return len(self.apps)


class Application:
    def __init__(self, name) -> None:
        self.name = name
        self.blocked = False
