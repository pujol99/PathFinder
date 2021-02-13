import math

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def compute_distance(self, node):
        return math.sqrt(
            pow(node.x-self.x, 2)+pow(node.y-self.y, 2)
        )

    def __str__(self):
        return f"({self.x}, {self.y})"