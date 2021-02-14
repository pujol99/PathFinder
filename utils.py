from matplotlib import pyplot as plt

def line(ax, start, end):
    ax.plot([start.x, end.x], [start.y, end.y] ,'-k')
    plt.pause(0.02)

def show_graph(start, nodes):
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