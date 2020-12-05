#  96. Unique Binary Search Trees (medium)
#  https://leetcode.com/problems/unique-binary-search-trees/description/
#
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        https://www.youtube.com/watch?v=OIc0mHgHUww
        
        Given a root and left/right sub BST, the number of various combination is
        
        C = C_l*C_r
        
        e.g. n=4, root can be 1,2,3,4
        root = 1: C_l = [];  C_r = [2,3,4].....
        root = 2: C_l = [1]; C_r = [3,4].....
        root = 3: C_l = [1,2]; C_r = [4].....
        root = 4: C_l = [1,2,3]; C_r = [].....
        '''
        
        dp = {0: 1, 1: 1}
        
        i = 2
        while i <= n:
            
            dp[i] = 0
            for x in range(i):
                root = x + 1
                
                left, right = root-1, i - root  # left and right are the number of nodes of subtree. 
                print (left, right)
                dp[i] += dp[left]*dp[right]
            
            i += 1
                
        return dp[n]
                