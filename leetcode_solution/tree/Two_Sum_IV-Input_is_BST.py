## [Leetcode#653] Two Sum IV - Input is a BST
##

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if self.traverse(k, root) == True:
            return True
        else:
            return False
    
    def traverse(self, k, root):
        if not root.left and not root.right: return set({root.val})
        
        node_set = set({root.val})
        if root.left :
            left = self.traverse(k, root.left)
            if left == True:
                return True
            else:
                if k - root.val in left: return True
                node_set.update(left)
        
        if root.right:
            right = self.traverse(k, root.right)
            if right == True:
                return True
            else:
                for x in right:
                    if k - x in node_set: return True
                node_set.update(right)
            
        return node_set