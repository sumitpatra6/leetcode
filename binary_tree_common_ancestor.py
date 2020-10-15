from binary_tree import BinaryTree
class Solution(BinaryTree):
    
    def find_node(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        l = self.find_node(root.left, val)
        r = self.find_node(root.right, val)
        return l or r

    def get_sibling(self,node):
        if node is None:
            return None
        parent = node.parent
        if parent is None:
            return None
        if parent.left == node:
            return parent.right
        if parent.right == node:
            return parent.left

    def cover(self, root, node):
        """
        Check if the 
        """
        if root is None:
            return False
        if root == node:
            return True
        return self.cover(root.left, node) or self.cover(root.right, node)

    def common_ancestor_with_link_to_parent(self, root, p, q):
        """
        Find the common ancestor
        """
        p = self.find_node(root, p)
        q = self.find_node(root, q)
        if not self.cover(root, p) or not self.cover(root, q):
            return None
        if  self.cover(p, q):
            return p.val
        if self.cover(q, p):
            return q.val

        sibling = self.get_sibling(p)
        parent = p.parent
        while(not self.cover(sibling, q)):
            sibling = self.get_sibling(parent)
            parent = parent.parent
        return parent.val
    
    def common_ancestors_without_link_tp_parent(self, root, p, q):
        def util(root, p, q):
            """
                If p and q ae on the same side then call the function recursively for that sub tree
                else root is the common ancestor
            """
            if root is None or root == p or root == q:
                return root
            p_on_left = self.cover(root.left, p)
            q_on_left = self.cover(root.left, q)
            if p_on_left != q_on_left:
                return root.val
            side = root.left if p_on_left else root.right
            return util(side, p, q)
            

        p = self.find_node(root, p)
        q = self.find_node(root, q)
        if not self.cover(root, p) or not self.cover(root, q):
            return None
        return util(root, p, q)  


            


array = [20, 10, 30, 5, 15, None, None, 3, 7, None, 17]
sol = Solution(array)
sol.preorder()
print(sol.common_ancestor_with_link_to_parent(sol.root, 7, 17))
print(sol.common_ancestors_without_link_tp_parent(sol.root, 7, 17))