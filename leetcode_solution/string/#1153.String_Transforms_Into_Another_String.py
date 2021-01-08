#  1153. String Transforms Into Another String (hard)
#  https://leetcode.com/problems/string-transforms-into-another-string/
#
class Solution:
    '''
    https://www.shangmayuan.com/a/aa8080f6a9bc4e46b9713cfb.html
    '''
    def canConvert(self, str1: str, str2: str) -> bool:
        
        convert = {}
        for i in range(len(str1)):
            if str1[i] in convert:
                if convert[str1[i]] != str2[i]:
                    return False
            else:
                convert[str1[i]] = str2[i]
        
        if len(set(list(str2))) == 26:
            return True if str1==str2 else False
        
        return True