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
    

    # solution - 2: totally consider string
    def intToRoman2(self, num: int) -> str:
        sub_dict = {
            0: {"4": "IV", "9": "IX"}, # 4, 9
            1: {"4": "XL", "9": "XC"}, # 40, 90
            2: {"4": "CD", "9": "CM"}, # 400, 900
        }

        add_dict = {0: "I", 1: "X", 2: "C", 3: "M"}
        five_dict = {0: "V", 1: "L", 2: "D"}

        num_str = str(num)

        ans = []
        i = len(num_str)-1
        digit = 0
        while i >= 0:
            if num_str[i] in ("4", "9"):
                ans.append(sub_dict[digit][num_str[i]])
            else:
                if int(num_str[i]) >= 5: # 5, 6, 7, 8
                    # 70 -> five_dict[1] + add_dict[1] * (7-5)
                    ans.append(
                        five_dict[digit] + add_dict[digit]*(int(num_str[i])-5)
                    )
                else: # 0, 1, 2, 3
                    # 300 -> add_dict[2] * 3
                    ans.append(
                        add_dict[digit] * int(num_str[i])
                    )
            i -= 1
            digit += 1
        
        return "".join(ans[::-1])
