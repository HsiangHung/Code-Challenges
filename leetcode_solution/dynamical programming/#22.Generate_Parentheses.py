## [Leetcode#22] Generate Parentheses
#   
#  i.e. n=3, we have ["((()))","(()())","(())()","()(())","()()()"]
#
#  Here I used dynamic programming.
#
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = {0: [], 1: ["()"]}
        if n <= 1: return dp[n]
        
        step = 2
        while step <= n:
            
            dp[step] = set({})
            for pare in dp[step-1]:
                pare = "(" + pare
                for i in range(1, len(pare)):
                    dp[step].add(pare[:i]+")"+pare[i:])

            step += 1
            
        return list(dp[n])