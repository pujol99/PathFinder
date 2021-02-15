from graph import Graph
from solver import *
from utils import *
from results import *

def main():
    times = []
    methods = [ClosestNode(), DynamicSolution(), MLRose()]
    _range = 4, 14
    map_size = 80

    for i in range(_range[0], _range[1]):
        graph = Graph(map_size, i)
        graph.build_random()
        times_i = []

        for method in methods:
            if  i > 9 and type(method) == type(DynamicSolution()):
                times_i.append(None)
                continue
            method.solve(graph)
            times_i.append(method.time)

        times.append(times_i)

    results = Results(times, _range, tuple([method.title for method in methods]))
    results.show_results()

if __name__ == "__main__":
    main()