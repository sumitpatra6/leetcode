from collections import deque

class ListNode(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.next = None

class Node(object):
    def __init__(self, val):
        super().__init__()
        self.val = val
        self.parent = None
        self.right = None
        self.left = None
    def __repr__(self):
        return str(self.val)

class BinaryTree(object):
    def __init__(self, array):
        super().__init__()
        self.root = self.build_from_array(array)

    def build_from_array(self, array):
        def build_array_util(array, root_index, parent):
            if root_index >= len(array) or array[root_index] is None:
                return None
            node = Node(array[root_index])
            node.left = build_array_util(array, 2*root_index + 1, node)
            node.right = build_array_util(array, 2*root_index + 2, node)
            node.parent = parent
            return node

        if len(array) == 0:
            return
        return build_array_util(array, 0, None)

    def inorder(self):
        """
        left -> root -> right
        For a bst it will be a sorted array
        """
        result  = []
        def inorder_util(node):
            if node is None:
                return
            inorder_util(node.left)
            result.append(node.val)
            inorder_util(node.right)
        inorder_util(self.root)
        print(result)

    def preorder(self):
        result = []
        def util(node):
            if node is None:
                return
            result.append(node.val)
            util(node.left)
            util(node.right)
        util(self.root)
        print(result)
    
    def postorder(self):
        result = []
        def util(node):
            if node is None:
                return 
            util(node.left)
            util(node.right)
            result.append(node.val)
        util(self.root)
        print(result)

    def get_min_element(self, root):
        """
        returns the minimum element of a BST
        """
        def min_elem_util(node):
            if node.left is None:
                return node.val
            return min_elem_util(node.left)
            
        return min_elem_util(root)

    def get_max_element(self, root):
        """
        returns the max element of the BST
        """
        def max_elem_util(node):
            if node.right is None:
                return node.val
            return max_elem_util(node.right)
        return max_elem_util(root)
    
    def is_valid_bst(self, root):
        if root is None:
         return True
        if root.left is not None and root.val < self.get_max_element(root.left):
            return False
        if root.right is not None and root.val >self.get_min_element(root.right):
            return False
        return self.is_valid_bst(root.left) and self.is_valid_bst(root.right)
    
    def isvalid_bst_2nd_approach(self, root):
        def valid_util(node, mini, maxi):
            if node is None:
                return True
            if node.val < mini or node.val > maxi:
                return False
            return valid_util(node.left, mini, node.val) and valid_util(node.right, node.val, maxi)
        return valid_util(root, float('-inf'), float('inf'))
    
    def is_leaf(self, node):
        if node.left is None and node.right is None:
            return True

    def isSymmetry(self, root):
        q = deque()
        q.append(root)
        while q:
            tmp = []
            for i in range(len(q)):
                node = q.popleft()
                if node is None:
                    tmp.append(None)
                    continue
                tmp.append(node.val)
                if node is not None:
                    if node.left is not None:
                        q.append(node.left)
                    else:
                        q.append(None)
                    if node.right is not None:
                        q.append(node.right)
                    else:
                        q.append(None)
            j = 0
            k = len(tmp) - 1
            while  j<=k:
                print(j, k, tmp)
                if tmp[j] != tmp[k]:
                    return False
                j += 1
                k -= 1
        return True
    
    def isSymetryRecursive(self, root):
        """
        Recursive solution for checking if a tree is symmetric or not.
        """
        def util(l, r):
            print(l, r)
            if not l and not r:
                return True
            if not l or not r:
                return False
            return l.val == r.val and util(l.left, r.right) and util(r.left and l.right)
        if root is None:
            return True
        return util(root.left, root.right)
    
    def hasPathSum(self, root, sum):
        def util(node, total):
            if node is None:
                return False
            total += node.val
            print(total)
            if not node.right and not node.left and total==sum:
                return True
            if not node.right and not node.left and total!=sum:
                return False
            return util(node.left, total) or util(node.right, total)
        return util(root, 0)

    def create_linked_list(self, root):
        dummy_node = ListNode(0)
        c = dummy_node
        q = deque()
        q.append(root)
        while q:
            current = q.popleft()
            new_node = ListNode(current.val)
            c.next = new_node
            c = c.next
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
        return dummy_node.next
    
    def find_node(self, root, val):
        """
        Finds and returns the node
        """
        if root is None or root.val == val:
            return root
        return self.find_node(root.left, val) or self.find_node(root.right, val)
            
    




# Binary Tree
array = [1, 2, 3, 4, 5, 6, 7]
my_bst = BinaryTree(array)
print("Binary tree created")
my_bst.inorder()
# l = my_bst.create_linked_list(my_bst.root)
# while l:
#     print(l.val)
#     l = l.next
# print(my_bst.isSymetryRecursive(my_bst.root))
# my_bst.preorder()
# my_bst.postorder()
# print("-----")
# print(my_bst.get_min_element(my_bst.root))
# print(my_bst.get_max_element(my_bst.root))
# print("******")
# print(my_bst.is_valid_bst(my_bst.root))
# print("======")
# print(my_bst.isvalid_bst_2nd_approach(my_bst.root))
