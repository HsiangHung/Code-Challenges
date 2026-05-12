# [#744] Find Smallest Letter Greater Than Target
#
# Google
#
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        self.ch = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 
                      'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
                      'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                      's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24,
                      'y': 25, 'z': 26}
        
        return self.search(letters, target)

        
    def search(self, letters, target):
        
        if self.ch[target] >= self.ch[letters[-1]] or self.ch[target] < self.ch[letters[0]]: 
            return letters[0]
        
        if len(letters) == 2: 
            return letters[1]            
        
        mid = len(letters) // 2
        if self.ch[letters[mid]] <= self.ch[target] < self.ch[letters[mid+1]]: 
            return letters[mid+1]
        elif self.ch[letters[mid+1]] <= self.ch[target]:
            return self.search(letters[mid+1:], target)
        elif self.ch[target] <= self.ch[letters[mid]]:
            return self.search(letters[:mid+1], target)
        