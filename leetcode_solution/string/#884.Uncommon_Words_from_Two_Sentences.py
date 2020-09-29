# #884. Uncommon Words from Two Sentences
#
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        word_dict = {}
        for word in A.split(" ")+B.split(" "):
            word_dict[word] = word_dict.get(word, 0) + 1
                                
        return [word for word in word_dict if word_dict[word] == 1]