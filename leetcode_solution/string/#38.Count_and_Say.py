## [Leetcode#38] Count and Say
##
##  
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        sq = {1: "1"}
        term = 2
        while term <= n:
            
            new_string = ""
            string = sq[term-1]
            count = 1
            for i in range(1, len(string)):
                if string[i] != string[i-1]:
                    new_string += str(count) + string[i-1]
                    count = 1
                else:
                    count += 1
                    
            new_string += str(count) + string[-1]
            sq[term] = new_string
            
            term += 1
            
        return sq[n]