# #953. Verifying an Alien Dictionary
#
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        use hashmap to sore Alien letter orders.
        '''
        self.order_dict = {order[i]: i for i in range(len(order))}
        
        for i in range(len(words)-1):
            if not self.order_comparison(words[i], words[i+1]):
                return False
            
        return True
        
        
    def order_comparison(self, s1, s2):
        i = 0
        while i < min(len(s1), len(s2))-1 and s1[i] == s2[i]:
            i += 1
        
        if s1[i] != s2[i]:
            return self.order_dict[s1[i]] < self.order_dict[s2[i]]
        else:
            if len(s2) > len(s1): 
                return True
            else:
                return False
            
        
        