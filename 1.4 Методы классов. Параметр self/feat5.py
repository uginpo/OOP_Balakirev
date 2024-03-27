class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def drow(self):
        print(*[x for x in self.data if self.LIMIT_Y[0] <= x <= self.LIMIT_Y[1]])


graph1 = Graph()
graph1.set_data([10, 3, 5, 56, -2, 0, 4])
graph1.drow()
