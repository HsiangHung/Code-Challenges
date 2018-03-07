# [#520] Detect Capital 
#
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1: return True
        
        isCaptial = (word[1] == word[1].upper())
        isLittle  = (word[1] == word[1].lower())
        for i in range(2, len(word)):
            isCaptial = isCaptial and (word[i] == word[i].upper())
            isLittle  = isLittle  and (word[i] == word[i].lower())
           
        if isLittle: return True
        
        if isCaptial and word[0] == word[0].upper():
            return True
        
        return False