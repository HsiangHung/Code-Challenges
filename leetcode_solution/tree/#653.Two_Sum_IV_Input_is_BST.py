## [Leetcode#653] Two Sum IV - Input is a BST
##

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        
        return self.traverse({}, root, k)
        
    def traverse(self, node_dict, root, k):
        
        node_dict[root.val] = node_dict.get(root.val, 0) + 1
        if k - root.val in node_dict:
            if k - root.val != root.val: 
                return True
            else:
                if node_dict[root.val] == 2: return True

        if not root.left and not root.right: return False
        
        isSumExist = False
        if root.left:
            print root.left.val
            isSumExist = isSumExist or self.traverse(node_dict, root.left, k)
            
        if root.right:
            isSumExist = isSumExist or self.traverse(node_dict, root.right, k)
        
        return isSumExist  