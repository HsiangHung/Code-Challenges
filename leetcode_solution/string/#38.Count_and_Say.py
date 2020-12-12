#  38. Count and Say (easy)
#  https://leetcode.com/problems/count-and-say/
#  
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        say = "1"
        while i < n:
            
            new_say = []
            for x in say:
                if len(new_say) > 0 and new_say[-1][0] == x:
                    new_say[-1] = (new_say[-1][0], new_say[-1][1] + 1)
                else:
                    new_say.append((x, 1))         
            
            say = ""
            for char, val in new_say:
                say += str(val)+char
            
            i+= 1
        
        return say