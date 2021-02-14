from random import randrange
from matplotlib import pyplot as plt
import math

class Graph:
    def __init__(self, space, size):
        self.nodes = set()
        self.start = None
        self.space = space
        self.size = size

    def build_random(self):
        self.start = self.random_node(0)
        for i in range(self.size):
            self.nodes.add(self.random_node(i+1))

    def random_node(self, index):
        return Node(randrange(self.space), randrange(self.space), index)

    def show_graph(self):
        plt.plot(self.start.x, self.start.y, 'bo')
        for node in self.nodes:
            plt.plot(node.x, node.y, 'ro')

    def closest_node(self, node):
        closest = 99999, None
        for element in self.nodes-{node}:
            distance = node.compute_distance(element)
            if distance < closest[0]:
                closest = distance, element
        return closest

    def get(self, index):
        for node in self.nodes:
            if node.index == index:
                return node


class Node:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
    
    def compute_distance(self, node):
        return math.sqrt(
            pow(node.x-self.x, 2)+pow(node.y-self.y, 2)
        )

    def __str__(self):
        return f"({self.x}, {self.y})"
