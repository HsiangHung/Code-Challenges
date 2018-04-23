## [#758] Bold Words in String
#
#  Google
#
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        bold_index = set({})
        
        for word in words:
            #print word
            for i in range(len(S)-len(word)+1):
                #print i, i+len(word), S[i: i+len(word)]
                if S[i: i+len(word)] == word: 
                    for j in range(i, i+len(word)):
                        bold_index.add(j)
        
        bold_string = ''
        for i in range(len(S)):
            if i in bold_index:
                if i == 0:
                    bold_string += '<b>'+S[0]
                elif len(S)-1 >= i > 0 and i-1 not in bold_index:
                    bold_string += '<b>'+S[i]
                else:
                    bold_string += S[i]
            else:
                if i - 1 in bold_index:
                    bold_string += '</b>' + S[i]
                else:
                    bold_string += S[i]
                    
        if len(S)-1 in bold_index:
            bold_string += '</b>'
        
        return bold_string
                