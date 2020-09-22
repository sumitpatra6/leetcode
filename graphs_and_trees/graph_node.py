class Node:
    def __init__(self,value):
        self.value = value
        self.vsited = None
        self.neighbours = []
    
    def add_neighbour(self, node):
        self.neighbours.append(node)