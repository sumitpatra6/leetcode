# another solution is to cjeck for the pre order traversals for the binary trees
# the smallest subtree will be a sub string of the bigger tree
from binary_tree import BinaryTree


def check_similarity(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return check_similarity(root1.left, root2.left) and check_similarity(root1.right, root2.right)
    

def check_subtree(root1, root2):
    """
    Root 1 is the bigger subtree
    
    """
    # step 1: find out if tree rooted at root 1 contains root2

    c = root1.find_node(root1.root, root2.root.val)
    if not c:
        return False
    
    return check_similarity(c, root2.root)

parent_tree = BinaryTree([2,6,5,None, None, 1, 3])
parent_tree.inorder()
child_tree = BinaryTree([5, 3, 1])
child_tree.inorder()
print(check_subtree(parent_tree, child_tree))