from graph import Graph
from solver import *

def main():
    graph = Graph(40, 4)
    graph.build_random()

    for method in [ClosestNode, TravelingSalesman]:
        method().solve(graph)



if __name__ == "__main__":
    main()