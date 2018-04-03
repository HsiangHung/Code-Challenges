# [# 394] Decode String
#  
#   Google, Yelp, Coupang
#
#
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '': return s
        
        # run two stacks simulanteously: integer and string stacks.
        # only as long as hits "]", mean need to merge substring if 2[a3[d]] => 2[addd]
        # or ef3[d] => efddd and pop out a num in intStack to make a new string
        #
        # example of running the code:  string[i], [num stack], [ch stack], encoded_string
        # string = "3[a]2[b4[F]]cf"
        # '3' [] [] ''
        # '[' [u'3'] [] ''
        # ']' [u'3'] [u'a'] ''
        # '2' [] [] 'aaa'
        # '[' [u'2'] [] 'aaa'
        # '4' [u'2'] [u'b'] 'aaa'
        # '[' [u'2', u'4'] [u'b'] 'aaa'
        # ']' [u'2', u'4'] [u'b', u'F'] 'aaa'
        # ']' [u'2'] [u'bFFFF'] 'aaa'
        # 'c' [] [] 'aaabFFFFbFFFF'
        # 'f' [] [] 'aaabFFFFbFFFFc'
        # outcome:  'aaabFFFFbFFFFcf'       
        #
        integers = set({'0','1','2','3','4','5','6','7','8','9'})
        
        string = list(s)
        
        encoded_string = ""
        
        intStack, chStack = [], []
        while len(string) > 0:
            
            print string[0], intStack, chStack, encoded_string
            
            ch = string.pop(0)
            
            
            if ch in integers:
                num = ch
                while string[0] != "[":
                    num += string.pop(0)
                intStack.append(num)                
            elif ch == "[":
                substring = ""
                while string[0] != "]" and string[0] not in integers:
                    substring += string.pop(0)
                chStack.append(substring)
            elif ch == "]":
                substring = (chStack.pop())*int(intStack.pop())
                ## after making the substring, if there are still strings left in chStack,
                ## means need to merge to the previous character. Otherwise directly added to 
                ## encoded_string
                if len(chStack) > 0:
                    chStack[-1] += substring
                else:
                    encoded_string += substring
            else:
                ## after making the substring, if there are still strings left in chStack,
                ## means need to merge to the previous character. Otherwise directly added to 
                ## encoded_string
                if len(chStack) > 0:
                    chStack[-1] += ch
                else:
                    encoded_string += ch
                
        return encoded_string
                