## Q4.3 (also leetcode)Convert Sorted Array to Binary Search Tree
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def generate_BST(arr):
    if len(arr) == 0: return None
    if len(arr) == 1: return TreeNode(arr[0])
    
    mid = int(len(arr)/2)
    root = TreeNode(arr[mid])
    
    Left = arr[:mid]
    Right = arr[mid+1:]
    root.left = generate_BST(Left)
    root.right = generate_BST(Right)
    return root

root = generate_BST([1,2,5,10,20,21,46,100])

## check with inorder:
inOrder(root)