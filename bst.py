from collections import deque
from binary_tree import Node, BinaryTree
class BST(BinaryTree):
    def __init__(self, array):
        self.root = None 
        self.build_from_array(array)
    def build_from_array(self, array):
        for a in array:
            self.root = self.insert_into_binarty_tree(self.root, a)
    def insert_into_binarty_tree(self, root, val):
        if root is None:
            new_node = Node(val)
            return new_node
        if val <= root.val:
            root.left = self.insert_into_binarty_tree(root.left, val)
        if val > root.val:
            root.right = self.insert_into_binarty_tree(root.right, val)
        return root
    def inorder_iterative(self):
        pass
    def preorder_iterative(self):
        if self.root is None:
            return []
        result = deque()
        stack = []
        stack.append(self.root)
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            # print(result)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        print(result)
    def postorder_iterative(self):
        if self.root is None:
            return []
        result = deque()
        stack = []
        stack.append(self.root)
        while len(stack) > 0:
            node = stack.pop()
            result.appendleft(node.val)
            # print(result)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        print(result)

    def level_order_traversal(self):
        q = deque()
        visited = []
        q.append(self.root)
        while len(q):
            node = q.popleft()
            visited.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        print(visited)
    
    def delete_node(self, root, val):
        if root is None:
            return None

        elif val <= root.val:
            root.left = self.delete_node(root.left, val)
        elif val > root.val:
            root.right = self.delete_node(root.right, val)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                tmp = self.get_min_element(root.right)
                root.val = tmp
                self.delete_node(root.right, tmp)
        return root


# BST
# array = [10, 5, 14, 12, 15]
# bst = BST(array)
# print("******")
# bst.inorder()
# bst.inorder_iterative()
# print("=====")
# bst.postorder()
# bst.postorder_iterative()
# print("=====")
# bst.preorder()
# bst.preorder_iterative()
# print("Level Order")
# bst.level_order_traversal()