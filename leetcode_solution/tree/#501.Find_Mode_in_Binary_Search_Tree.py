#  501. Find Mode in Binary Search Tree (easy)
#  https://leetcode.com/problems/find-mode-in-binary-search-tree/
#
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        self.freq = {}
        self.DFS(root)
        max_freq = max([self.freq[x] for x in self.freq])        
        return [x for x in self.freq if self.freq[x] == max_freq]
        
    def DFS(self, root): 
        
        self.freq[root.val] = self.freq.get(root.val, 0) + 1
        
        if not root.left and not root.right: return
        
        if root.left:
            self.DFS(root.left)
            
        if root.right:
            self.DFS(root.right)