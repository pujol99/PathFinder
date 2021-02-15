import matplotlib.pyplot as plt

class Results:
    def __init__(self, data, range, names):
        self.data = data
        self.start, self.end = range
        self.names = names

    def show_results(self):
        plt.plot(self.data)
        plt.title(f"Time results (Cities range [{self.start}, {self.end-1}])")
        plt.legend(self.names)
        plt.show()
