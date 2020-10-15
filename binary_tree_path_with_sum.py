from binary_tree import BinaryTree

# broot force algorithm 
# sum the path received from all the sub trees
# this solution is no optimized for better runtime
def path_with_sum(root, value):
    if root is None:
        return 0
    path_from_root = count_path_with_sum(root, 0, value)
    path_from_left = count_path_with_sum(root.left, 0, value)
    path_from_right = count_path_with_sum(root.right, 0, value)
    return path_from_root + path_from_left + path_from_right
    
def count_path_with_sum(root, current, target):
    if not root:
        return 0
    current += root.val
    total_path = 0
    if current == target:
        total_path = 1
    total_path += count_path_with_sum(root.left, current, target)
    total_path += count_path_with_sum(root.right, current, target)
    return total_path
    

array = [2, 6, 5,None, None, 1, 3]
bst = BinaryTree(array)
bst.inorder()
print(path_with_sum(bst.root, 8))
