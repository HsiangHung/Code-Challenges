#  678. Valid Parenthesis String (medium)
#  https://leetcode.com/problems/valid-parenthesis-string/
#
#
class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        http://bookshadow.com/weblog/2017/09/17/leetcode-valid-parenthesis-string/
        '''
        v_set = set([0])
        for i in range(len(s)):            
            new_set = set()
            if s[i] == "(":
                for x in v_set:
                    new_set.add(x+1)
            elif s[i] == ")":
                for x in v_set:
                    if x >= 1: new_set.add(x-1)
            elif s[i] == "*":
                for x in v_set:
                    new_set.add(x+1)
                    new_set.add(x)
                    if x >= 1: new_set.add(x-1)
        
            v_set = new_set
        
        return 0 in v_set
#
#  * this verison has issue on time exceeds.
#
class Solution2:
    def checkValidString(self, s: str) -> bool:
        '''
        https://www.cnblogs.com/grandyang/p/7617017.html
        DFS on insert "*" = "(", ")", "" and see if return True (doesn't pass all test cases)
        '''
        return self.DFS(0, s)
        
        
    def DFS(self, ct, s):     
        
        for i in range(len(s)):
            
            if ct < 0: return False
            
            if s[i] == "(":
                ct += 1
            elif s[i] == ")":
                if i == ct == 0: return False
                ct -= 1
            elif s[i] == "*":
                return self.DFS(ct+1, s[i+1:]) or self.DFS(ct, s[i+1:]) or self.DFS(ct-1, s[i+1:])
                
        return ct == 0
                
    