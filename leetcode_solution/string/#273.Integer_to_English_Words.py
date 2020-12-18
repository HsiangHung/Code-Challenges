#  273. Integer to English Words (hard)
#  https://leetcode.com/problems/integer-to-english-words/
#
#
class Solution:
    def numberToWords(self, num: int) -> str:
        
        if num == 0: return "Zero"
        
        single = {"1": "One", "2": "Two", "3": "Three", "4": "Four", 
                       "5": "Five", "6": "Six", "7": "Seven", "8": "Eight",
                       "9": "Nine"}
        
        digit3 = {1: " Thousand", 2: " Million", 3: " Billion"}
        
        num = str(num)
        
        ans = ""
        while len(num) > 3:
            n_digits = (len(num) -1) // 3 
                        
            if n_digits > 0:
                if int(num[:len(num)-n_digits*3]) > 0:   # only num > 0 to consider thousand, million, billon
                    ans += self.withinHundred(num[:len(num)-n_digits*3]) + digit3[n_digits]
                num = num[len(num)-n_digits*3:]
        
        ans += self.withinHundred(num)
        return ans[1:] if ans[0] == " " else ans

            
    def withinHundred(self, num):    
        tenth_one = {"1": " Eleven", "2": " Twelve", "3": " Thirteen", "4": " Fourteen", 
                     "5": " Fifteen", "6": " Sixteen", "7": " Seventeen", "8": " Eighteen",
                     "9": " Nineteen", "0": " Ten"}

        tenth = {"2": " Twenty", "3": " Thirty", "4": " Forty",  "5": " Fifty", 
                 "6": " Sixty", "7": " Seventy", "8": " Eighty",
                 "9": " Ninety"}

        single = {"1": " One", "2": " Two", "3": " Three", "4": " Four", 
                  "5": " Five", "6": " Six", "7": " Seven", "8": " Eight",
                  "9": " Nine"}        
        
        ans = ""
        
        if int(num) == 0: return ans
        
        if len(num) == 3:
            if num[0] != "0": ans += single[num[0]]+" Hundred"
            num = num[1:]
        
        if int(num) > 0:                             # e.g. 200, then after 2 hundred, we skip
            if len(num) == 2:
                if num[0] == "0":                    # e.g. 03, 05...
                    ans += single[num[1]] 
                elif num[0] == "1":                  # e.g. 13, 15,..
                    ans += tenth_one[num[1]]
                else:                                # e.g. 23, 45, ...
                    ans += tenth[num[0]]
                    if num[1] != "0": ans += single[num[1]]
            else:
                ans += single[num]
        
        return ans
                
