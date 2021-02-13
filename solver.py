from utils import *

class Solver()


class ClosestNode:
    def __init__(self):
        self.x1, self.x2, self.y1, self.y2 = [], [], [], []

    def solve(self, graph):
        current_node = graph.start
        while graph.nodes:
            distance, node = graph.closest_node(current_node)

            line(current_node, node)

            graph.nodes.remove(node)
            current_node = node

    def line(self, start, end):
        self.x1.append(start.x)
        self.x2.append(end.x)
        self.y1.append(start.y)
        self.y2.append(end.y)
