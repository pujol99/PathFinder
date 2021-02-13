from utils import *

class Solver:
    def __init__(self):
        self.x1, self.x2, self.y1, self.y2 = [], [], [], []

    def line(self, start, end):
        self.x1.append(start.x)
        self.x2.append(end.x)
        self.y1.append(start.y)
        self.y2.append(end.y)
    
    def show(self):
        plot_lines(self.x1, self.y1, self.x2, self.y2, self.title)

class ClosestNode(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Closest Node Method"

    def solve(self, graph):
        current_node = graph.start
        while graph.nodes:
            distance, node = graph.closest_node(current_node)

            self.line(current_node, node)

            graph.nodes.remove(node)
            current_node = node

class Dijkstra(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Dijkstra"

    def solve(self, graph):
        raise NotImplementedError