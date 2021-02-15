from graph import Graph
from solver import *
from results import *

def main():
    _range, show_plots = handle_args(sys.argv[1:])
    times, map_size = [], 80
    methods = [ClosestNode(), DynamicSolution(), MLRose()]


    for i in range(_range[0], _range[1]):
        graph = Graph(map_size, i)
        graph.build_random()
        times.append([None if i > 9 and type(method) == type(DynamicSolution())
            else method.solve(graph, show_plots) 
            for method in methods])

    Results(times, _range, tuple([method.title for method in methods])).show_results()

def handle_args(args):
    #:return: range, show_plots
    # 2 5 ...   -> (2, 5) False
    # 2 5       -> (2, 5) True
    # 10 ...    -> (1, 10) False
    # 10        -> (1, 10) True
    #           -> (4, 12) True
    nargs = len(args)
    if nargs == 1:
        if args[0].isdigit() and int(args[0]) > 1:
            return (1, int(args[0])), True
    if nargs == 2:
        if args[0].isdigit() and int(args[0]) > 0:
            arg = int(args[0])
            if args[1].isdigit() and int(args[1]) > int(args[0]):
                return (arg, int(args[1])), True
            elif not args[1].isdigit():
                return (1, arg), False
    if nargs == 3:
        if args[0].isdigit() and int(args[0]) > 0:
            arg1 = int(args[0])
            if args[1].isdigit() and int(args[1]) > int(args[0]):
                arg2 = int(args[1])
                return (arg1, arg2), False
    return (7, 12), True

if __name__ == "__main__":
    main()