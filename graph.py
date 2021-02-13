from node import Node
from random import randrange
from matplotlib import pyplot as plt

class Graph:
    def __init__(self, space, size):
        self.nodes = set()
        self.start = None
        self.space = space
        self.size = size

    def build_random(self):
        self.start = self.random_node()
        for i in range(self.size):
            self.add_node(self.random_node())

    def add_node(self, node):
        self.nodes.add(node)

    def random_node(self):
        return Node(randrange(self.space), randrange(self.space))

    def show_graph(self):
        plt.plot(self.start.x, self.start.y, 'bo')
        for node in self.nodes:
            plt.plot(node.x, node.y, 'go')
        plt.show()

    def compute_min_cost(self, start, nodes):
        lowest = 999999
        
        for node in nodes:
            cost = self.compute_min_cost(node, nodes-{node}) + start.compute_distance(node)
            if cost < lowest:
                lowest = cost

        return lowest if nodes else 0


    def closest_node(self, node):
        closest = 99999, None
        for element in self.nodes:
            if element != node:
                distance = node.compute_distance(element)
                if distance < closest[0]:
                    closest = distance, element
        return closest
