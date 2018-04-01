# [# 437] Path Sum III
#  
#
#
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0
        self.num_sum = 0
        self.traversal(root, [root.val], sum)
        
        return self.num_sum

        
    def traversal(self, root, sumList, sum):
        
        for i in range(len(sumList)-1):  ## note here only sum the preious paths
            sumList[i] += root.val
            if sumList[i] == sum:
                self.num_sum += 1
            
        if sumList[-1] == sum:
            self.num_sum += 1
        
        if not root.left and not root.right: return
        
        if root.left:
            self.traversal(root.left, sumList+[root.left.val], sum)
            
        if root.right:       
            self.traversal(root.right, sumList+[root.right.val], sum)