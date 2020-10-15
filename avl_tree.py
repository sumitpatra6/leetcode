from collections import deque
from binary_tree import BinaryTree
class Node(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.height = 1
        self.right = None
        self.left = None

class AvlTree(object):
    def __init__(self, array):
        self.root = None
        self.build_from_array(array)
    

    def build_from_array(self,array):
        for a in array:
            if a is None:
                continue
            self.root = self.insert(self.root, a)
            self.level_order_traversal(self.root)
            print("----")
        
    def insert(self,root, val):
        if root is None:
            return Node(val)
        if val <= root.val:
            root.left = self.insert(root.left, val)
        if val > root.val:
            root.right = self.insert(root.right, val)
        root.height = self.get_max_depth(root)
        balance = self.get_balance(root)
        if balance > 1 and root.left and  val <= root.left.val:
            # left left, right rotate parent
            root = self.rotate_right(root)
        if balance > 1 and root.left and val > root.left.val:
            # left right, left rotate child
            root.left = self.rotate_left(root.left)
        if balance > 1 and root.right and val > root.right.val:
            #  right right, left rotate parent
            root = self.rotate_left(root)
        if balance > 1 and root.right and val < root.right.val:
            # right left
            root.right = self.rotate_right(root.right)
            root = self.rotate_left(root)
        return root 

    def get_balance(self, root):
        return abs(self.get_max_depth(root.right) - self.get_max_depth(root.left))
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def rotate_right(self, root):
        if not root:
            return root
        if root.right is None and root.left is None:
            return root
        y = root.left
        root.left = y.right
        y.right = root
        # adjust the height
        y.height = self.get_max_depth(y)
        return y

    def rotate_left(self, root):
        if not root:
            return root
        if root.right is None and root.left is None:
            return root
        y = root.right
        root.right = y.left
        y.left = root
        # adjust the height
        y.height = self.get_max_depth(y)
        return y

    def get_max_depth(self, root):
        if root is None:
            return 0
        return 1 + max(self.get_max_depth(root.left), self.get_max_depth(root.right))

    def level_order_traversal(self, root):
        if not root:
            return
        q = deque()
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                current = q.popleft()
                level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            print(level)

    

array = [1,2,3,4,5]
tree = AvlTree(array)
# tree.level_order_traversal(tree.root)
# tree.inorder(tree.root)

print("*****")

array1 = [2, 6, 5, None, None, 1, 3]
tree = AvlTree(array1)
# tree.level_order_traversal(tree.root)
# tree.inorder(tree.root)