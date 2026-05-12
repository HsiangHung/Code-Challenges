#  647. Palindromic Substrings (medium)
#  https://leetcode.com/problems/palindromic-substrings/
#
class Solution:
    '''
    This pronlem is similar to # 5.
    '''
    def countSubstrings(self, s: str) -> int:
        
        dp = {1: [(i, i) for i in range(len(s))], 
              2: [(i, i+1) for i in range(len(s)-1) if s[i]==s[i+1]]}
        
        sub_len, search = 3, True
        while sub_len <= len(s) and search:
            
            if sub_len-2 in dp:
                dp[sub_len] = []
                for m, n in dp[sub_len-2]:
                    if m-1 >= 0 and n + 1 < len(s) and s[m-1] == s[n+1]:
                        dp[sub_len].append((m-1, n+1))
            else:
                if sub_len-1 not in dp: search = False
    
            sub_len += 1
        
        
        return sum([len(dp[sub_len]) for sub_len in dp])               