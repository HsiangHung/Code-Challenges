# #844. Backspace String Compare
#
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:    
        return self.empty_text(S) == self.empty_text(T)
        
    def empty_text(self, s):
        
        stack = []
        i = len(s)-1
        while i >= 0:
            if stack == []:
                stack.append(s[i])
            else:
                if s[i] == "#":
                    stack.append(s[i])
                else:
                    if stack[-1] == "#":
                        stack.pop()
                    else:
                        stack.append(s[i])
            i -= 1
        
        return "".join([x for x in stack[::-1] if x != "#"])