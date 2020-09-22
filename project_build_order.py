from pprint import pprint
import json

projects_map = {}

class Project:
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.neighbours = []
        self.dependencies = 0
    
    def add_dependency(self, project):
        self.neighbours.append(project)
        project.increaseDependencies()

    def increaseDependencies(self):
        self.dependencies += 1

    def __repr__(self):
        return json.dumps({
            'root' : self.val,
            #'neighbours' : self.neighbours,
            'dependencies' : self.dependencies
        })        
    def __str__(self):
         return json.dumps({
            'root' : self.val,
            #'neighbours' : self.neighbours,
            'dependencies' : self.dependencies
        })  

def build_project(projects):
    # keep 2 pointers
    # 1 pointer to keep track of where to put the data and
    # another pointer to point to from where to start processing
    un_processed = 0
    build_order = []
    for 


def get_or_create_project(project_name):
    if project_name not in projects_map:
        projects_map[project_name] = Project(project_name)
    return projects_map[project_name] 

def main(projects, dependencies):
    for p in projects:
        get_or_create_project(p)
    for dependency in dependencies:
        from_node = get_or_create_project(dependency[0])
        to_node = get_or_create_project(dependency[1])
        from_node.add_dependency(to_node)
    pprint(projects_map)

nodes = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
# idea is to build the projects which do not have any incoming dependencies.
# After building the projects mark the incoming nodes as null on the dependent projects

if __name__ == '__main__':
    main(nodes, dependencies)
