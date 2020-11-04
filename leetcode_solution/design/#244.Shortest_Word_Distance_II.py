# 244. Shortest Word Distance II
#
class WordDistance:

    def __init__(self, words: List[str]):
        
        self.words = {}
        for i, word in enumerate(words):
            self.words[word] = self.words.get(word, []) + [i]

    def shortest(self, word1: str, word2: str) -> int:
        if self.words[word1][-1] < self.words[word2][0]:
            return abs(self.words[word1][-1] - self.words[word2][0])
        elif self.words[word2][-1] < self.words[word1][0]:
            return abs(self.words[word2][-1] - self.words[word1][0])
        else:
            min_dist = 2**31
            for x in self.words[word1]:
                for y in self.words[word2]:
                    min_dist = min(min_dist,  abs(x-y))
            return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)