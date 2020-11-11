# # 270. Closest Binary Search Tree Value
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def closestValue(self, root: TreeNode, target: float) -> int:
        '''
        need to go through entire tree. If use the criterion < min_diff to stop,
        then we will miss another closer node under the node.
        '''
        if not root.left and not root.right: return root.val
        
        output = root.val
        
        if root.left:
            val = self.closestValue(root.left, target)
            if abs(val-target) < abs(output-target): output = val                
        
        if root.right:
            val = self.closestValue(root.right, target)
            if abs(val-target) < abs(output-target): output = val  
                
        
        return output