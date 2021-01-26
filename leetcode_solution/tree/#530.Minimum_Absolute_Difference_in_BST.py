#  530. Minimum Absolute Difference in BST (easy)
#  https://leetcode.com/problems/minimum-absolute-difference-in-bst/
#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    given a root, always find max of left and min of right, not just compare root-left and root-right
    e.g. [0,null,2236,1277,2776,519] is a example.
    '''
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.min = 2**31-1
        self.DFS(root)
        return self.min
        
    def DFS(self, root):
        
        if root.left and root.right:
            min_l, max_l = self.DFS(root.left)
            min_r, max_r = self.DFS(root.right)
            self.min = min(self.min, abs(root.val-max_l), abs(min_r-root.val))
            return min_l, max_r
        elif root.left:
            min_l, max_l = self.DFS(root.left)
            self.min = min(self.min, abs(root.val-max_l))
            return min_l, root.val
        elif root.right:
            min_r, max_r = self.DFS(root.right)
            self.min = min(self.min, abs(min_r-root.val))
            return root.val, max_r
        else:
            return root.val, root.val
    