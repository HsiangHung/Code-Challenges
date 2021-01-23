#  652. Find Duplicate Subtrees (medium)
#  https://leetcode.com/problems/find-duplicate-subtrees/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    We save tree pattern in a set. Only duplication, and save to self.ans
    NOTE for 28-th line the last "," and 31-th lin ",," are important, 
         to distinguish [1,2,null] and [1,null,2]
    '''
    def __init__(self):
        self.pattern_set = set({})
        self.ans = {}
        
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root: return []
        _ = self.DFS(root)
        return [self.ans[pattern] for pattern in self.ans]
        
    def DFS(self, root):
        
        if root.left and root.right:
            pattern = str(root.val) +',' + self.DFS(root.left) + ',' + self.DFS(root.right)
        elif root.left:
            pattern = str(root.val) + ','+ self.DFS(root.left) + ',' # <= the last "," is important. 
        elif root.right:
            pattern = str(root.val) + ',,'+ self.DFS(root.right)
        else:
            pattern = str(root.val)
            
        if pattern in self.pattern_set:
            if pattern not in self.ans: self.ans[pattern] = root
        
        self.pattern_set.add(pattern)
            
        return pattern
         