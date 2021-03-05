#  337. House Robber III (medium)
#  https://leetcode.com/problems/house-robber-iii/
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    http://bookshadow.com/weblog/2016/03/13/leetcode-house-robber-iii/
    
    max function: max(left+right, root + left.left + left.right + right.left + right.right)
    
    Needs to save dp function (use path as key), otherwise redudant. 
    e.g. should not compute rob(left) and rob(left.left), rob(left.right) separately
    '''
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        
        self.dp = {}
        return self.DFS(root, '')
        
    def DFS(self, root, path):
        if not root: return 0
                
        if path not in self.dp:
            l, r = root.left, root.right
            if l and r:
                max_val = max(self.DFS(l, path+'l') + self.DFS(r, path+'r'), 
                    root.val + self.DFS(l.left, path+'ll') + self.DFS(l.right, path+'lr')
                             + self.DFS(r.left, path+'rl') + self.DFS(r.right, path+'rr'))
            elif l:
                max_val = max(self.DFS(l, path+'l'), 
                    root.val + self.DFS(l.left, path+'ll') + self.DFS(l.right, path+'lr'))
            elif r:
                max_val = max(self.DFS(r, path+'r'), 
                    root.val + self.DFS(r.left, path+'rl') + self.DFS(r.right, path+'rr'))
            else:
                max_val = root.val
                
            self.dp[path] = max_val
            return max_val
        else:
            return self.dp[path]
        
        