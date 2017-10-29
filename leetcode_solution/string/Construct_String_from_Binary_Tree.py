## [Leetcode#606] Construct String from Binary Tree
##

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ''
        return self.traverse(t)
    
    def traverse(self, root):
        if not root.left and not root.right: return str(root.val)
        
        left_s = ''
        if root.left:
            left_s = self.traverse(root.left)
            
        string = str(root.val) + '(' + left_s + ')'   
        
        
        if root.right:
            right_s = self.traverse(root.right)
            return str(root.val) + '(' + left_s + ')'  + '(' + right_s + ')'
        else:
            return string
