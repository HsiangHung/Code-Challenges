## [Leetcode#108] Convert Sorted Array to Binary Search Tree
#
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []: return None
        
        return self.root(nums)
        
    def root(self, nums):
        n = len(nums)
        if n == 1: return TreeNode(nums[0])
        
        half = nums[int(n/2)]
        node = TreeNode(half)
        node.left = self.root(nums[:int(n/2)])
        if  int(n/2)+1 < n:
            node.right = self.root(nums[int(n/2)+1:])
        return node