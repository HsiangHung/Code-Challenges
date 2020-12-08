#  250. Count Univalue Subtrees (medium)
#  https://leetcode.com/problems/count-univalue-subtrees/
#
#
class Solution(object):
    def countUnivalSubtrees(self, root):
        '''
        given a root, the child returns set of possibles value of the subtree
        a uniqie subtree only exists only if 
           len(left_set) = len(right_set) = 1 and root = root.left = root.right
        '''
        if not root: return 0
        self.uni_subtree = 0
        _ = self.DFS(root)
        return self.uni_subtree

    def DFS(self, root):
        if not root.left and not root.right:
            self.uni_subtree += 1
            return set([root.val])
        
        curr = set([root.val])
        if root.left and root.right:
            curr = curr.union(self.DFS(root.left)).union(self.DFS(root.right))
        elif root.left:
            curr = curr.union(self.DFS(root.left))
        elif root.right:
            curr = curr.union(self.DFS(root.right))
            
        if len(curr) == 1: self.uni_subtree += 1
        return curr