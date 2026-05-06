# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        """
        * [5, 2, -3] has subtree: [2], [-3], and [5, 2, -3] 
           so subtree_sum = [2, -3, 5+2-3 = 4], so [2, -3, 4]
        * [5, 2, -5] has subtree: [2], [-5], and [5, 2, -5] 
           so subtree-sum = [2, -5, 2], so [2] only
        """
        if not root:
            return []

        self.freq_dict, self.max_freq = {}, 0
        def DFS(root):
            if not root:
                return 0
    
            if root.left is None and root.right is None: # if root is a leaf node only
                self.freq_dict[root.val] = self.freq_dict.get(root.val, 0) + 1
                self.max_freq = max(self.max_freq, self.freq_dict[root.val])
                return root.val
            else:            
                # mean the root at least has left or right branch.
                subtree_sum = DFS(root.left) + DFS(root.right) + root.val
                self.freq_dict[subtree_sum] = self.freq_dict.get(subtree_sum, 0) + 1
                self.max_freq = max(self.max_freq, self.freq_dict[subtree_sum])
                return subtree_sum

        _ = DFS(root)
        return [x for x in self.freq_dict if self.freq_dict[x] == self.max_freq]
