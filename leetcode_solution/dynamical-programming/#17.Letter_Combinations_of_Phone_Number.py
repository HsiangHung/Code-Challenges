## [Leetcode#17] Letter Combinations of a Phone Number
##
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        import copy
        if digits == '': 
            return []
        
        d_map = {"2": set(["a", "b", "c"]), "3": set(["d", "e", "f"]), 
                "4": set(["g", "h", "i"]), "5": set(["j", "k", "l"]), 
                "6": set(["m", "n", "o"]), "7": set(["p", "q", "r", "s"]), 
                "8": set(["t", "u", "v"]), "9": set(["w", "x", "y", "z"]) 
                }
            
        dp = {0: d_map[digits[0]]}
        i = 1
        while i < len(digits):

            combination = set({})
            for x in dp[i-1]:
                for y in d_map[digits[i]]:
                    combination.add(x+y)
            
            dp[i] = combination
            i += 1
        
        return list(dp[len(digits)-1])
