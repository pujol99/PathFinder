from graph import Graph
from utils import *
from solver import ClosestNode

def main():
    graph = Graph(20, 5)
    graph.build_random()

    method1 = ClosestNode()
    method1.solve(graph)
    method1.show()



if __name__ == "__main__":
    main()