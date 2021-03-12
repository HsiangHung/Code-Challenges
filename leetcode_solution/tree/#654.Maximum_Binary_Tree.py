#  654. Maximum Binary Tree (medium)
#  https://leetcode.com/problems/maximum-binary-tree/
#
class Solution(object):
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0: return
        max_val, idx = self.get_maximum(nums)
        if max_val is not None:
            root = TreeNode(val=max_val)
            root.left = self.constructMaximumBinaryTree(nums[:idx])
            root.right = self.constructMaximumBinaryTree(nums[idx+1:])
            return root
        
    def get_maximum(self, nums):
        max_val, idx = None, None
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i] > max_val):
                max_val, idx = nums[i], i
        return max_val, idx