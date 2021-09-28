#  124. Binary Tree Maximum Path Sum (hard)
#  https://leetcode.com/problems/binary-tree-maximum-path-sum/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Good explanation: https://www.youtube.com/watch?v=TO5zsKtc1Ic
    For each root (node), check:
      1. path_sum (along a path only, max(l, r, l+root, r+root, root)) 
      2. cross_root_sum (sum over left and right paths across root, l+root+r)
      3. compare global result 
    and return current max path_sum (including current root node)
    e.g. a sub-tree like:
               -1
               / \
              1   2
             / \
            4   5
           / \   \
          3   8  -10
          
    (1) for leaves 3 and 8: 
          path_sum = 3 and 8, return 8
          max_sum = 8
    (2) for node 4: 
          path_sum = max(3, 3+4, 8, 8+4, 4) = 12, return 12
          cross_root_sum = 3 + 4 + 8 = 15
          max_sum = max(8, 15) = 15
    (3) for node 1:
          path_sum = max(12, 12+1, 5, 5+1, 1), return 13
          cross_root_sum = 12 + 1 + 5 = 18
          max_sum = max(15, 18) = 18
    (4) for node -1:
          path_sum = max(13, 13+(-1), 2, 2+(-1), -1) = 13, but return 13+(-1)
          cross_root_sum = 13 + (-1) + 2 = 14
          max_sum = max(14, 18) = 18
    ......
    '''
    def maxPathSum(self, root: TreeNode) -> int:
        return self.DFS(root)[1]
        
    def DFS(self, root):
        if not root: return -2**31, -2**31
        
        curr = root.val
        l, l_max = self.DFS(root.left) 
        r, r_max = self.DFS(root.right)
        
        local_max = max(curr, curr + r, curr + l, curr + l + r)  # local means curr node through
        global_max = max(local_max, l_max, r_max)       # global means curr node may not through
        
        return max(curr, curr + r, curr + l), global_max
            