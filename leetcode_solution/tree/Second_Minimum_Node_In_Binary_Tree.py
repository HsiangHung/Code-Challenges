## [Leetcode#671] Second Minimum Node In a Binary Tree
##

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root.left and not root.right: return -1
        
        values = self.traverse(root)
        if len(values) <= 1: return -1
        return values[1]
    
    def traverse(self, root):
        if not root.left and not root.right: return [root.val]
        
        left = self.traverse(root.left)    
        right = self.traverse(root.right)
        
        print root.val, left, right
        
        values = [left[0], right[0], root.val]

        if len(left) > 1: values.append(left[1])
        if len(right) > 1: values.append(right[1])
            
        values = sorted(set(values))
        
        ## to find second minimum node, we need to consider second minimum
        ## from each branch, and compare to root node. Also consider repeated
        ## values, put set first and then sort.
        
        if len(values) == 1: return [values[0]]
            
        return [values[0], values[1]]