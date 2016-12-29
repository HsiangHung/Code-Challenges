##  [Leetcode#270] Closest Binary Search Tree Value
##
##  idea: always find minimum difference
##
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        self.closestVal = None
        self.min_dist = float('inf')
        self.traverse(root, target)
        return self.closestVal

        
    def traverse(self, root, target):
        if target == float(root.val): 
            self.min_dist =0
            self.closestVal = root.val
            return
    
        if abs(float(root.val)-target) < self.min_dist:
            self.closestVal = root.val
            self.min_dist = abs(float(root.val)-target)
    
        if not root.left and not root.right: return
    
        if target < float(root.val) and root.left != None: self.traverse(root.left, target)
        if target > float(root.val) and root.right != None: self.traverse(root.right, target)
        