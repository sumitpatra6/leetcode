from pprint import pprint
import json
class Project:
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.neighbours = []
    
    def __repr__(self):
        return json.dumps({
            'root' : self.val,
            'neighbours' : self.neighbours
        })        

class BuildProject(object):
    def __init__(self, nodes):
        super().__init__()
        self.node_dict = {}
        for node in nodes:
            self.node_dict[node] = Node(node)
    def build_graph(self, dependency_list):
        for dependency in dependency_list:
            f = dependency[0]
            t = dependency[1]
            self.node_dict[f].neighbours.append(t)
        pprint(self.node_dict)
    
    def build_project(self):
        visited = []
        for n in self.node_d


nodes = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
project = BuildProject(nodes)
project.build_graph(dependencies)