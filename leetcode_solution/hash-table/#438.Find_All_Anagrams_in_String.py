# # 438. Find All Anagrams in a String
#
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        if A is anagram of B, then they have same dictionary
        '''
        s_dict, p_dict = self.get_dict(s[:len(p)]), self.get_dict(p)
        
        i, output = 0, []
        while i <= len(s)-len(p):            
            if s_dict == p_dict: output.append(i)
            
            if i != len(s)-len(p):
                s_dict[s[i+len(p)]] = s_dict.get(s[i+len(p)], 0) + 1                
                s_dict[s[i]] = s_dict.get(s[i], 0) - 1
                if s_dict[s[i]] == 0:
                    del s_dict[s[i]]
            
            i += 1            
        
        return output
        
    def get_dict(self, s):
        s_dict = {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        return s_dict