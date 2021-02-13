from graph import Graph
from utils import *

def main():
    graph = Graph(100)

    graph.start = graph.random_node()
    for i in range(50):
        graph.add_node(graph.random_node())

    
    



if __name__ == "__main__":
    main()