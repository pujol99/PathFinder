import matplotlib.pyplot as plt
from copy import deepcopy
from utils import *

class Solver:
    def __init__(self):
        self.cost = 0
        _, self.ax = plt.subplots()
        self.start = None

    def solve(self, graph):
        self.start = graph.start
        show_graph(self.start, graph.nodes)

        plt.title(self.title)
        self.ax.imshow(
            plt.imread("map.png"), 
            extent=[-10, graph.space+10, -10, graph.space+10])

        self.solve_method(deepcopy(graph), self.start)
        
        plt.title(f"{self.title}, Cost: {int(self.cost)}")


class ClosestNode(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Closest Node Method"

    def solve_method(self, graph, current_node):
        while graph.nodes:
            distance, node = graph.closest_node(current_node)
            self.cost += distance
            line(self.ax, current_node, node)

            graph.nodes.remove(node)
            current_node = node
        
        self.cost += current_node.compute_distance(self.start)
        line(self.ax, current_node, self.start)


class TravelingSalesman(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Traveling Salesman Method"
        self.data = {}

    def solve_method(self, graph, current_node):
        self.cost = self.min_path(self.start, graph.nodes)

        self.backtrack(graph, current_node)
        
    def min_path(self, node, neighbors):
        if not neighbors:
            return node.compute_distance(self.start)
        
        min_distance = 999999, None
        for neighbor in neighbors:
            distance = node.compute_distance(neighbor) + self.min_path(neighbor, neighbors-{neighbor})

            if distance < min_distance[0]:
                min_distance = distance, neighbor

        self.data[index_str(node, neighbors)] = min_distance
        return min_distance[0]

    def backtrack(self, graph, current_node):
        while graph.nodes:
            distance, node = self.data[index_str(current_node, graph.nodes)]
            line(self.ax, current_node, node)

            graph.nodes.remove(node)
            current_node = node
        
        line(self.ax, current_node, self.start)