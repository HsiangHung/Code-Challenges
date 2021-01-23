#  671. Second Minimum Node In a Binary Tree (easy)
#  https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    since node = min(node.left, node.right). 
    When doing DFS, even node.val != root.val, we still need to continue recursion.
    e.g. tree = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1], sec-min is on leave.
    '''
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        self.sec_min = [root.val]
        self.DFS(root)
        return max(self.sec_min) if len(self.sec_min) == 2 else -1
    
    
    def DFS(self, root):
         
        if root.left and root.right: 
            val = max(root.left.val, root.right.val) 
            if len(self.sec_min) == 1:
                if val != self.sec_min[0]: self.sec_min.append(val)
            else:
                if self.sec_min[0] < val < self.sec_min[-1]: self.sec_min[-1] = val
                
            self.DFS(root.left), self.DFS(root.right)
                
        
            
                
        