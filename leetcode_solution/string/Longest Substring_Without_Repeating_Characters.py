## [Leetcode#3] Longest Substring Without Repeating Characters
##
## good interpretation how to do this problem:
## http://blog.csdn.net/likecool21/article/details/10858799 
##
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return 0
        n =len(s)
        
        start = 0 
        pos_dict = {s[0]: 0}
        max_len = 1
        while start < n-1:
            end = start+1
            while end <= n-1:
                if s[end] not in pos_dict:
                    pos_dict[s[end]] = end
                    end += 1
                else:
                    if len(pos_dict) > max_len: max_len = len(pos_dict)
                    start = pos_dict[s[end]]+1
                    pos_dict = {s[start]: start}
                    break
            if len(pos_dict) > max_len: max_len = len(pos_dict)
            if end == n: break
                    
                
        return max_len
