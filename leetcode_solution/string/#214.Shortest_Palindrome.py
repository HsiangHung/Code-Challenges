#  214. Shortest Palindrome (hard)
#  https://leetcode.com/problems/shortest-palindrome/
#
class Solution:
    '''
    https://wdxtub.com/interview/14520595479135.html
    Run checking from middle site moving to left

    NOTE: this code passed 119/220 test cases, cannot get through all.
    '''
    def shortestPalindrome(self, s: str) -> str:        
        rev_s = s[::-1]
                
        mid = len(s) // 2 + 1
        min_palind = rev_s[:-1] + s
        i = mid
        while i >= 0:
            check = self.check(i, i, s, rev_s)  # check mid is a single char
            if check:
                if len(check) < len(min_palind): 
                    min_palind = check
            
            if i+1 <= len(s)-1 and s[i] == s[i+1]: # check mid is two chars (if equal)
                check = self.check(i, i+1, s, rev_s)
                if check and len(check) < len(min_palind): 
                    min_palind = check
            
            i -= 1       
        
        return min_palind
    
    def check(self, i, j, s, rev_s):
        a, b = i-1, j+1
        while a >= 0 and b <= len(s)-1 and s[a] == s[b]:
            a -= 1
            b += 1
        
        if a < 0:
            return rev_s[:len(s)-b] + s
            # return s[b:][::-1] + s
        else:
            return None
    