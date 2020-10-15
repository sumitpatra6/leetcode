from collections import deque
class Person(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None


class ThroneInheritance(object):
    def __init__(self, name):
        self.root = Person(name)
    
    def search(self, name, root):
        # returns the subtree rootes at the provided key
        if not root or root.name == name:
            return root
        for child in root.children:
            res = self.search(name, child)
            if res:
                return res 

    def birth(self, parentName, childName):
        parent_root = self.search(parentName, self.root)
        if parent_root:
            child_sub_tree = Person(childName)
            child_sub_tree.parent = parent_root
            parent_root.children.append(child_sub_tree)
    
    def delete_node(self, node):
        if node is None:
            return None
        elif len(node.children) == 0:
            del node
            return None
        elif len(node.children):
            to_be_promoted = node.children[0]
            node.name = to_be_promoted.name
            node.children[0] = self.delete_node(to_be_promoted)
            # readjust the childrens
            # for the last level, the first element of the children array may become None. The array needs to be re ordered
            i = 0
            while i < len(node.children):
                if node.children[i] != None:
                    break
                i += 1
            if i >= len(node.children):
                 node.children = []
            else:
                node.children = node.children[i:]
        

    def death(self, name):
        node_to_delete = self.search(name, self.root)
        if len(node_to_delete.children) > 0:
            node_to_delete.name = node_to_delete.children[0].name
            for i in range(len(node_to_delete.children) - 1):
                node_to_delete.children[i] = node_to_delete.children[i+1]
            if len(node_to_delete.children) > 0:
                node_to_delete.children.pop()
        else:
            parent = node_to_delete.parent
            for i in range(len(parent.children)):
                if parent.children[i] == node_to_delete:
                    del parent.children[i]
                    break
            # for i in range(len(parent.children) - 1):
            #     parent.children[i] = parent.children[i+1]
            # if len(node_to_delete.children) > 0:
            #     node_to_delete.children.pop()

    def print_level(self):
        print("*****")
        "Prints the hierarchy of the tree."
        if self.root is None:
            return
        q = deque()
        q.append(self.root)
        while q:
            tmp =[]
            for i in range(len(q)):
                current = q.popleft()
                tmp.append(current.name)
                for child in current.children:
                    q.append(child)
            print(tmp)
        print("****")

    def get_inheritance(self):
        stack = []
        stack.append(self.root)
        inheritance = []
        while stack:
            current = stack.pop()
            inheritance.append(current.name)
            for i in range(len(current.children) - 1, -1, -1):
                stack.append(current.children[i])
        print(inheritance)
        return inheritance

# ["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
# [["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
inherit = ThroneInheritance('king')
inherit.birth('king', 'andy')
inherit.birth('king', 'bob')
inherit.birth('king', 'catherine')
inherit.birth('andy', 'mathew')
inherit.birth('bob', 'alex')
inherit.birth('bob', 'asha')
inherit.print_level()
inherit.get_inheritance()
inherit.death('bob')
inherit.print_level()
inherit.death('alex')
inherit.print_level()
inherit.death('asha')
inherit.print_level()
inherit.get_inheritance()