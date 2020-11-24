#  1047. Remove All Adjacent Duplicates In String (easy)
#  https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
#
class Solution:
    def removeDuplicates(self, S: str) -> str:
        '''
        Note here "accav" = > "v", but "acccav" => "acav"
        '''
        stack = []
        
        for i in range(len(S)):
            if stack == []:
                stack.append(S[i])
            else:
                if S[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(S[i])
            
        return "".join(stack)