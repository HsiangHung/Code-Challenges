# [#647] Palindromic Substrings
#
#  s = "addaefe"
#  always consider len-2 pali string, and add first and end, and first == end
#  e.g. "adda" should be from "a"+"dd"+"a", "aef" = "a"+"e"+"f", "a" != "f" so not pali
#
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {1: [(i,i) for i in range(len(s))]}
        if len(s) == 1: return len(dp[1])
        
        dp[2] = [(i,i+1) for i in range(len(s)-1) if s[i] == s[i+1]]
        if len(s) == 2: return len(dp[1]+dp[2])
        
        str_len = 3
        while str_len <= len(s):
            dp[str_len] = []
            
            pali_list = dp[str_len-2]
            for pair in pali_list:
                start, end = pair[0], pair[1]
                if start-1 >= 0 and end+1 <= len(s)-1 and s[start-1] == s[end+1]:
                    dp[str_len].append((start-1, end+1))
                    
            str_len += 1
                 
        return sum([len(dp[str_len]) for str_len in dp])
               