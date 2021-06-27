#  572. Subtree of Another Tree
#  https://leetcode.com/problems/subtree-of-another-tree/
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.subTree = False
        
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and subRoot: return False
        
        if root.val == subRoot.val:
            self.subTree = self.subTree or self.isSameTree(root, subRoot)
            
        if self.subTree: return True # if found subtree, no need to keep DFS
        
        self.isSubtree(root.left, subRoot)
        self.isSubtree(root.right, subRoot)
        
        return self.subTree
    
    
    def isSameTree(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        
        if t1.val != t2.val: return False
        
        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        