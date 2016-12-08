## Q 4.1 Check if a tree is balanced

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        
        self.isBalanced = True

        self.getHeight(root)
        return self.isBalanced
        
        
    def getHeight(self, root):
        
        if root.left == None and root.right == None: return 0
        
        depth_L = 0
        if root.left != None:
            depth_L = depth_L+self.getHeight(root.left)+1
            
        depth_R = 0
        if root.right != None:
            depth_R = depth_R+self.getHeight(root.right)+1
        
        if abs(depth_L-depth_R) > 1: self.isBalanced = False
        
        return max(depth_L, depth_R)