# 389. Find the Difference

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        def helper(s: str) -> dict:
            s_dict = {}
            for ch in s:
                s_dict[ch] = s_dict.get(ch, 0) + 1
            return s_dict

        s_dict, t_dict = helper(s), helper(t)
        if len(s_dict) == len(t_dict):
            for ch in s_dict:
                if s_dict[ch] != t_dict[ch]:
                    return ch
        else:
            for ch in t_dict:
                if ch not in s_dict:
                    return ch
