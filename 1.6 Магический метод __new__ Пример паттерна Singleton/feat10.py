# Здесь объявляется класс Factory

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:
    def build_secquence(self):
        return []

    def build_number(self, string):
        return float(string)


# эти строчки не менять!
ld = Loader()
s = "4, 5, -6.5"
res = ld.parse_format(s, Factory())
