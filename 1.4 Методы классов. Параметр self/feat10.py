class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = dict()

        self.tr.setdefault(eng, [])
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        self.tr.pop(eng, False)

    def translate(self, eng):
        return self.tr[eng]
