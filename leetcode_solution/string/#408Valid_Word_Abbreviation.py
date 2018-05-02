# [#408] Valid Word Abbreviation
#
#
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        if len(word) < len(abbr): return False
        word += ' '
        abbr += ' '
        
        digits = set([str(x) for x in range(10)])
        i, j = 0, 0
        while i < len(abbr) and j < len(word):
            if abbr[i] not in digits:
                i += 1
                j += 1
            elif abbr[i] in digits:
                num = ''
                while i < len(abbr) and abbr[i] in digits:
                    num += abbr[i]
                    i += 1
                    
                if num[0] == '0': return False  ## very trick, to test word="word", abbr="w02d". Make sure this False
                num = int(num)
                
                if j+num > len(word):
                    return False
                elif j+num == len(word):
                    if i != len(abbr):
                        return False
                    else:
                        return True
                elif j+num < len(word) and word[j+num] != abbr[i]:
                    return False

                j += num
                
        return True
   