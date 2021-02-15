from copy import deepcopy
from utils import *
import time

#MLRose
import six, sys
sys.modules['sklearn.externals.six'] = six
import mlrose


class Solver:
    def initialize(self, graph):
        self.cost = 0
        self.start = graph.start
        self.path = []
        self.time = time.process_time()

        self.ax = initialize_plot(graph, self.title)

    def finalize(self):
        self.time = time.process_time() - self.time
        
        finalize_plot(self.title, self.cost, self.time)

    def solve(self, graph):
        self.initialize(graph)
        self.solve_method(deepcopy(graph), self.start)
        self.finalize()

class ClosestNode(Solver):
    def __init__(self):
        self.title = "Closest Node Method"

    def solve_method(self, graph, current_node):
        while graph.nodes:
            distance, node = graph.closest_node(current_node)
            self.cost += distance

            self.path.append(current_node)
            graph.nodes.remove(node)
            current_node = node
        
        self.cost += current_node.compute_distance(self.start)
        self.path.append(current_node)
        display_path(self.ax, self.path)


class DynamicSolution(Solver):
    def __init__(self):
        self.title = "Dynamic programming Method"

    def solve_method(self, graph, current_node):
        self.data = {}
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
            self.path.append(current_node)

            graph.nodes.remove(node)
            current_node = node
        self.path.append(current_node)
        display_path(self.ax, self.path)


class MLRose(Solver):
    def __init__(self):
        self.title = "MLRose Method"
    
    def solve_method(self, graph, current_node):
        nodes = list(graph.nodes) + [self.start]
        nodes.sort(key = lambda x: x.index)

        dist_list = [(node1.index, node2.index, node1.compute_distance(node2)) 
            for node1 in nodes for node2 in nodes 
            if node1.index < node2.index]

        fitness_coords = mlrose.TravellingSales(
            coords=[node.get() for node in nodes], 
            distances=dist_list)

        problem_fit = mlrose.TSPOpt(length=len(nodes), fitness_fn=fitness_coords, maximize=False)
        self.path, self.cost = mlrose.genetic_alg(problem_fit, mutation_prob = 0.2, 
					      max_attempts = 100, random_state = 2)

        self.path = [graph.get(node) for node in self.path]
        display_path(self.ax, self.path)