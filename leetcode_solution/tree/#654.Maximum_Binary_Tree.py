# [#654] Maximum Binary Tree
#
# 
#
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []: return None
        
        max_val, max_idx = self.get_maximal(nums)
        root = TreeNode(max_val)
        
        if len(nums) == 1: return root
        
        left = self.constructMaximumBinaryTree(nums[:max_idx])
        right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        
        root.left, root.right = left, right
        return root
    
    def get_maximal(self, nums):
        max_val, max_idx = nums[0], 0
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val, max_idx = nums[i], i
        return max_val, max_idx
        prev = None
        node = head
        while node.next != None:
            nextNode = node.next
            node.next = prev
            prev = node
            node = nextNode
    
        node.next = prev
        return node