from matplotlib import pyplot as plt

def line(ax, start, end):
    ax.plot([start.x, end.x], [start.y, end.y] ,'-k')
    plt.pause(0.02)

def show_graph(graph):
    start, nodes = graph.start, graph.nodes
    plt.plot(start.x, start.y, 'bo')
    for node in nodes:
        plt.plot(node.x, node.y, 'ro')

def index_str(node, neighbors):
        string = str(node.index)
        for neighbor in sorted([neighbor.index for neighbor in neighbors]):
            string += "|"+str(neighbor)
        return string

def show():
    plt.show()

def initialize_plot(graph, title):
    _, ax = plt.subplots()
    show_graph(graph)
    plt.title(title)
    ax.imshow(
        plt.imread("map.png"), 
        extent=[-10, graph.space+10, -10, graph.space+10])
    return ax

def finalize_plot(title, cost, time):
    plt.title(f"{title}, Cost: {int(cost)}, Time: {format(time, '.2f')}")
    plt.close()


def display_path(ax, path):
    for i in range(len(path)-1):
        line(ax, path[i], path[i+1])
    line(ax, path[i+1], path[0])