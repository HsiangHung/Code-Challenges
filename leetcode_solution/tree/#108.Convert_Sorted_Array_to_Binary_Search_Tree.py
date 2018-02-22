## [Leetcode#108] Convert Sorted Array to Binary Search Tree
#
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
        
        middle = len(nums) // 2
        
        root = TreeNode(nums[middle])
        
        if len(nums) == 1: return root
        
        left = nums[:middle]
        right = nums[middle+1:]
        
        root.left  = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        
        return root