#  96. Unique Binary Search Trees (medium)
#  https://leetcode.com/problems/unique-binary-search-trees/
#
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        https://www.youtube.com/watch?v=OIc0mHgHUww
        
        n = 1        n=2                     n=3 
        
                 1       2     1      1       2        3     3
          1       \     /       \      \     / \      /     /
                   2   1         2      3   1   3    2     1
                                  \    /            /       \
                                   3  2            1         2
                                   
                            if n=3                            n_BST
                  root         root = 1, left = 0, right = 2,  1*2
                  /  \         root = 2, left = 1, right = 1,  1*1
               left   right    root = 3, left = 2, right = 0,  2*1
                                                        total   5
        '''
        dp = {0:1, 1:1, 2: 2}
        
        i = 3
        while i <= n:
            
            num_BST = 0
            for root in range(i):
                root += 1
                
                left, right = root-1, i - root
                num_BST += dp[left]*dp[right]
                
            dp[i] = num_BST 
            i += 1
            
        return dp[n]