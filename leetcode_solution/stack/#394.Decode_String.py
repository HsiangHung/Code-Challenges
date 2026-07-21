#
# 394. Decode String
# 
class Solution:
    def decodeString(self, s: str) -> str:
        """
        Using stack, good sol: https://www.youtube.com/watch?v=qB0zZpBJlh8
        """
        stack = []
        nums = set([str(x) for x in range(10)])     
    
        for i in range(len(s)):
            print(i, s[i], stack)
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1] in nums:
                    k = stack.pop() + k
                stack.append(int(k) * substr)

        return "".join(stack)
                
