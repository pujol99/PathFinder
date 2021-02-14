from graph import Graph
from solver import *
from utils import *

def main():
    graph = Graph(40, 8)
    graph.build_random()

    for method in [ClosestNode, TravelingSalesman]:
        method().solve(graph)

    show()

if __name__ == "__main__":
    main()