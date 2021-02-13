import matplotlib.pyplot as plt

class Solver:
    def __init__(self):
        self.cost = 0

    def line(self, start, end):
        plt.plot([start.x, end.x], [start.y, end.y] ,'-k')
        plt.pause(0.02)

class ClosestNode(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Closest Node Method"

    def solve(self, graph):
        graph.show_graph()
        plt.title(self.title)

        current_node = graph.start
        while graph.nodes:
            distance, node = graph.closest_node(current_node)
            self.cost += distance

            self.line(current_node, node)

            graph.nodes.remove(node)
            current_node = node
        
        plt.title(f"{self.title}, Cost: {int(self.cost)}")
        plt.show()

class Dijkstra(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Dijkstra"

    def solve(self, graph):
        raise NotImplementedError