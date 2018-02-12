#[Leetcode#606] Construct String from Binary Tree
#
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ""
        
        return self.traverse(t)
    
    
    def traverse(self, root):
        if not root.left and not root.right:
            return str(root.val)
        
        tree_string = "("
        if root.left:
            tree_string += self.traverse(root.left)
            
        tree_string += ")"
        
        if root.right:
            tree_string += "("+self.traverse(root.right)+")"
        
        return str(root.val)+tree_string