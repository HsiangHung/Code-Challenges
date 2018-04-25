## [#819] Most Common Word
#
#  Amazon
#
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.replace('!', '').replace('?','').replace(',','').replace('.','').replace(';','').replace("'", "")
        paragraph = paragraph.split(" ")
        
        banned = set(banned)
        
        letters = {}
        for word in paragraph:
            word = word.lower()
            if word not in banned:
                letters[word] = letters.get(word, 0) + 1
        
        max_freq, max_freq_word = 0, None
        for word in letters:
            if letters[word] > max_freq:
                max_freq, max_freq_word = letters[word], word
                
        return max_freq_word
                