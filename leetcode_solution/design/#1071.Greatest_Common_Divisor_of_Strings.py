#
# 2502. Design Memory Allocator
#
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        three scenarios:
                str1       str2   remainder  GCD
        1. "ABCABC"       "ABC"     "ABC"    "ABC"
        2. "ABABAB"       "ABAB"    "AB"     "AB"
        3. "AAAAAB"       "AAA"     "AAB"    ""
        4. "AABBAABBAA"   "AABB"    "AA"     "" 
        """
        long_s, short_s = str1, str2
        if len(str1) < len(str2):
            long_s, short_s = str2, str1
        m, n = len(long_s), len(short_s)

        i, j = 0, 0
        # find string remainder
        while i < m:
            if long_s[i] == short_s[j]:
                i += 1
                j += 1
                if j == n:
                    j = 0
            else: # e.g. str1 = "LEET", str2 = "LEAT", return ""
                return ""

        if i == m and j == 0:
            # e.g. str1 = "ABCABC", str2 = "ABC", both i, j end. return "ABC"
            return short_s
        elif i == m and j != n:
            # str1 = "AABBAABBAA", str2 = 'AABB', re = "AA", return ""
            # str1 = "ABABAB", str2 = "ABAB", re = "AB", return "AB"
            remainder = long_s[m-j:]
            return self.gcdOfStrings(remainder, short_s)  
