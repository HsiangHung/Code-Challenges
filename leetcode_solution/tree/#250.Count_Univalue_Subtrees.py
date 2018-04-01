# [# 250] Count Univalue Subtrees
#  
#
#
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.traversal(root)[1]
    
    def traversal(self, root):
        if not root.left and not root.right:
            return True, 1
        
        is_tree_uni, num_unisubtree = True, 0
        if root.left:
            isUni, num_tree = self.traversal(root.left)
            is_tree_uni = is_tree_uni and root.val == root.left.val and isUni
            num_unisubtree += num_tree
            
        if root.right:
            isUni, num_tree = self.traversal(root.right)
            is_tree_uni = is_tree_uni and root.val == root.right.val and isUni
            num_unisubtree += num_tree
            
        if is_tree_uni: num_unisubtree += 1
            
        return is_tree_uni, num_unisubtree