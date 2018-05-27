## [GeeksforGees] Sum Tree
#   
#   Write a function that returns true if the given Binary Tree is SumTree else false. 
#   A SumTree is a Binary Tree where value of every node x is equal to sum of nodes 
#   present in its left subtree and right subtree of x. An empty tree is SumTree and sum 
#   of an empty tree can be considered as 0. A leaf node is also considered as SumTree.  
#
#   https://practice.geeksforgeeks.org/problems/sum-tree/1 
#
class Solution(object):
    def isSumTree(self, root:
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """ 
        if not root: return False
        return self.SumSubTree(root) != -1
        
        
    def SumSubTree(self, root):
        if not root.left and not root.right:
            return root.val
    
        sumSubTree = 0
        if root.left and root.right:
            sumSubTree += self.SumSubTree(root.left) + self.SumSubTree(root.right)
        elif root.left:
            sumSubTree += self.SumSubTree(root.left)
        elif root.right:
            sumSubTree += self.SumSubTree(root.right)
            
        if sumSubTree != root.val:
            return -1
        else:
            return sumSubTree + root.val