# # 272. Closest Binary Search Tree Value II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diff = []
        
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        '''
        data structure used is self.diff = [(diff1, sign1), (diff2, sign2),.....]
        self.diff is order by diff
        '''
        self.DFS(root, target, k)
        return [int(target+x[0]*x[1]) for x in self.diff]
    
    def DFS(self, root, target, k):
        self.insert(root.val, target, k)
        if root.left: self.closestKValues(root.left, target, k)
        if root.right: self.closestKValues(root.right, target, k)

    def insert(self, val, target, k):
        
        if len(self.diff) == 0: 
            sgn = 1 if val > target else -1
            self.diff.append((abs(val-target), sgn))
        else:
            sgn = 1 if val > target else -1
            if abs(val-target) <= self.diff[0][0]:
                self.diff.insert(0, (abs(val-target), sgn))
            elif abs(val-target) < self.diff[-1][0]:
                i = 0
                while abs(val-target) >= self.diff[i][0]:
                    i += 1
                self.diff.insert(i, (abs(val-target), sgn))
            else:
                self.diff.append((abs(val-target), sgn))

            self.diff = self.diff[:k]