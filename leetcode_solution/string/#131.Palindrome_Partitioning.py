#  131. Palindrome Partitioning (medium)
#  https://leetcode.com/problems/palindrome-partitioning/
#
class Solution:
    def __init__(self):
        self.panlindrome_strings = set({})
        
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        if self.isPanlindrome(s): 
            self.panlindrome_strings.add(s)
            ans.append([s])

        for i in range(1, len(s)):
            subs1, subs2 = s[:i], s[i:]
            if (subs1 in self.panlindrome_strings) or self.isPanlindrome(subs1):
                self.panlindrome_strings.add(subs1)
                for x in self.partition(subs2):
                    ans.append([subs1] + x)

        return ans
            
        
    def isPanlindrome(self, s):
        if len(s) <= 1: return True
        mid = len(s) // 2
        i = 0
        while i <= mid:
            if s[i] != s[len(s)-1-i]: return False
            i += 1
        return True 