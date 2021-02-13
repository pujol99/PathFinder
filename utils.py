from matplotlib import pyplot as plt

def plot_lines(x1, y1, x2, y2, title):
    plt.plot(x1, y1, x2, y2, marker = 'o')
    plt.title(title)
    plt.show()
