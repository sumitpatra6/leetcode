from collections import deque
class Node(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.neighbours = []
    def __repr__(self):
        return "Val {}".format(self.val)


def bfs(root):
    if root is None:
        return None
    q = deque()
    visited = []
    q.append(root)
    visited.append(root)
    while len(q) > 0:
        current_node = q.popleft()
        print("{} - {}".format(current_node.val, hex(id(current_node))))
        for node in current_node.neighbours:
            if node not in visited:
                visited.append(node)
                q.append(node)

def deep_copy(root):
    if root is None:
        return None
    registry = {}
    q = deque()
    visited = []
    new_root = Node(root.val)
    visited.append(root)
    registry[root] = new_root
    q.append(root)
    while len(q) > 0:
        current_node = q.popleft()
        current_node_copy = registry[current_node] if registry.get(current_node) is not None else Node(current_node.val)
        for node in current_node.neighbours:
            if node in registry:
                tmp = registry[node]
            else:
                tmp = Node(node.val)
                registry[node] = tmp
            current_node_copy.neighbours.append(tmp)
            if node not in visited:
                visited.append(node)
                q.append(node)
    return new_root


    

"""
Graph to create
1 - 2
|   |
4 - 3
"""

# first build the graph 
node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_1.neighbours.extend([node_2, node_4])
node_2.neighbours.extend([node_1, node_3])
node_3.neighbours.extend([node_2, node_4])
node_4.neighbours.extend([node_1, node_3])
# print(node_1.__repr__())
deep_copy = deep_copy(node_1)
print("*********")
print(deep_copy)
print("**********")
bfs(node_1)
print("***********")
bfs(deep_copy)