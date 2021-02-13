from graph import Graph
from solver import ClosestNode

def main():
    graph = Graph(40, 50)
    graph.build_random()

    method1 = ClosestNode()
    method1.solve(graph)



if __name__ == "__main__":
    main()