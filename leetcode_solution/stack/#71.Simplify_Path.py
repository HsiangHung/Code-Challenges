#  71. Simplify Path (medium)
#  https://leetcode.com/problems/simplify-path/
#
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        Using stack, when "..", pop out last element.
        '''
        path = path.split("/")
        
        stack = []
        for i in range(len(path)):
            if path[i] == ".": # skip
                continue
            elif path[i] == "..":
                if len(stack) > 0: stack.pop()
            elif path[i] != "":
                stack.append(path[i])

        return "/" + "/".join(stack)
 