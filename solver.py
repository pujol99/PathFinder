import matplotlib.pyplot as plt
from copy import deepcopy
from utils import Tree

class Solver:
    def __init__(self):
        self.cost = 0
        _, self.ax = plt.subplots()
        self.bg = plt.imread("map.png")

    def solve(self, graph):
        graph.show_graph()
        plt.title(self.title)
        self.ax.imshow(self.bg, extent=[-10, graph.space+10, -10, graph.space+10])

        self.solve_method(deepcopy(graph))
        
        print(self.cost)
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
        
        self.cost += current_node.compute_distance(graph.start)
        self.line(current_node, graph.start)


class TravelingSalesman(Solver):
    def __init__(self):
        super().__init__()
        self.title = "Traveling Salesman Method"

    def solve_method(self, graph):
        self.start = graph.start

        self.cost, tree = self.min_path(self.start, graph.nodes)
        
        current_node = graph.start
        while tree.children:
            min_distance = 999999, None, None
            for _tree in tree.children:
                node, _, distance = _tree.data
                if distance < min_distance[0]:
                    min_distance = distance, node, _tree
            self.line(current_node, min_distance[1])

            current_node = min_distance[1]
            tree = min_distance[2]
        self.line(current_node, self.start)


    def min_path(self, node, neighbors):
        if not neighbors:
            distance = node.compute_distance(self.start)
            return distance, Tree((node, neighbors, distance))
        
        min_distance = 999999
        children = []
        for neighbor in neighbors:
            best_child = self.min_path(neighbor, neighbors-{neighbor})
            distance = node.compute_distance(neighbor) + best_child[0]
            children.append(best_child[1])

            if distance < min_distance:
                min_distance = distance

        return min_distance, Tree((node, neighbors, min_distance), children=children)