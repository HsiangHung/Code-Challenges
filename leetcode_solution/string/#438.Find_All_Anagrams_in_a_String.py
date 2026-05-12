# 438. Find All Anagrams in a String
#
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        looping s as s[:3], s[1:4], s[1:5], ......
        when new letter comes in, add it in dict, and remove the oldest letter.
        and check s_dict == p_dict
        '''
        p_dict = self.get_word_dict(p)
        s_dict = self.get_word_dict(s[:len(p)])
        
        print (p_dict, s_dict)
        
        indices = []
        for i in range(len(s)-len(p)+1):
            if s_dict == p_dict:
                indices.append(i)
            
            if i < len(s)-len(p) and s[i] != s[i+len(p)]:
                s_dict[s[i+len(p)]] = s_dict.get(s[i+len(p)], 0) + 1
                if s[i] in s_dict and s_dict[s[i]] > 1: 
                    s_dict[s[i]] -= 1
                elif s[i] in s_dict and s_dict[s[i]] == 1:
                    del s_dict[s[i]]
                
        return indices        
        
    def get_word_dict(self, s):
        word_dict = {}
        for i in range(len(s)):
            word_dict[s[i]] = word_dict.get(s[i], 0) + 1
        return word_dict