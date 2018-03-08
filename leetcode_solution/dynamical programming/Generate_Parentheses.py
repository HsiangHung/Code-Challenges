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
        import copy
        dp = {1: set({'()'})}
        
        i =2
        while i <= n:
            dp[i] = set({})
            sets = dp[i-1]
            for pare_set in sets:
                lst = list(pare_set)
                #print lst
                for k in range(len(lst)):
                    new_pare = copy.deepcopy(lst)
                    new_pare.insert(k+1,'(')
                    new_pare.append(')')
                    dp[i].add(''.join(new_pare))
            print dp[i]
            i +=1
            
        return list(dp[n])