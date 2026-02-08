#  98. Validate Binary Search Tree (medium)
#  https://leetcode.com/problems/validate-binary-search-tree/
#
#  facebook, microsoft, amazon, bloomberg
#
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #
        # to make sure a BST, the mininum of right subtree should be greater than the root
        #                         maximum of left subtree should be less than the root
        #
        if not root: return True
        self.valid = True
        _, _ = self.traversal(root)
        return self.valid

    def traversal(self, root):
        if not root.left and not root.right:
            return root.val, root.val

        if not self.valid: return None, None
        
        if root.left and root.right:
            min_L, max_L = self.traversal(root.left)
            min_R, max_R = self.traversal(root.right)
            if self.valid: self.valid = max_L < root.val < min_R
            return min_L, max_R
        elif root.left:
            min_L, max_L = self.traversal(root.left)
            if self.valid: self.valid = max_L < root.val
            return min_L, root.val
        elif root.right:
            min_R, max_R = self.traversal(root.right)
            if self.valid: self.valid = root.val < min_R
            return root.val, max_R


class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None: return True
        self.stack = -float('inf')
        self.isBST = True
        
        self.BST(root)
        return self.isBST
        
        
    def BST(self, root):
        if root.left == None and root.right == None:
            if root.val <= self.stack: 
                self.isBST = False
            else:
                self.stack = root.val
            return
        
        if root.left != None: self.BST(root.left)
        
        if root.val <= self.stack: 
            self.isBST = False
            return
        else:
            self.stack = root.val
                
        if root.right != None: self.BST(root.right)
        