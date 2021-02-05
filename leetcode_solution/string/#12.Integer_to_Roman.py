#  12. Integer to Roman (medium)
#  https://leetcode.com/problems/integer-to-roman/
#
class Solution:
    '''
    check through 1000, 100, 10, 1. 
    if > 9, insert "I"+Roman(val*10); if > 4 but < 5, insert "I"+Roman(val*5)
    if >= 5 but < 9, insert Roman(val*5) + "I"/"II"/"III"
    '''
    def intToRoman(self, num: int) -> str:
        symbols = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

        ans = ""
        for val in [1000, 100, 10, 1]:
            i = num // val
            if i > 0:
                
                if i == 4:
                    ans += symbols[val] + symbols[5*val]
                elif i == 9:
                    ans += symbols[val] + symbols[10*val]
                elif i in (5, 6, 7, 8):
                    ans += symbols[5*val] + symbols[val]*(i-5)
                else:
                    ans += symbols[val]*i                    
            
                num -= i* val
            
        return ans
        