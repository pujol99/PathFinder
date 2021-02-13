import matplotlib.pyplot as plt
from copy import deepcopy

class Solver:
    def __init__(self):
        self.cost = 0
        _, self.ax = plt.subplots()
        self.bg = plt.imread("map.png")

    def solve(self, graph):
        graph.show_graph()
        plt.title(self.title)
        self.ax.imshow(self.bg, extent=[0, graph.space, 0, graph.space])

        self.solve_method(deepcopy(graph))
        
        plt.title(f"{self.title}, Cost: {int(self.cost)}", color="red")
        plt.show()
        
    def line(self, start, end):
        self.ax.plot([start.x, end.x], [start.y, end.y] ,'-k')
        plt.pause(0.02)


class ClosestNode(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Closest Node Method"

    def solve_method(self, graph):
        current_node = graph.start
        while graph.nodes:
            distance, node = graph.closest_node(current_node)
            self.cost += distance

            self.line(current_node, node)

            graph.nodes.remove(node)
            current_node = node


class TravelingSalesman(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Traveling Salesman Method"

    def solve_method(self, graph):
        raise NotImplementedError