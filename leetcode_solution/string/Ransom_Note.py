## [Leetcode#383] Ransom Note
## 
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote == magazine: return True
        
        n = len(ransomNote)
        
        ## if ransomNote can be constructed by magazine, each letter can be found in magazine
        ## but the pointer need to move through the magazine string
        
        s_dict = {}
        for i in range(len(magazine)):
            if magazine[i] not in s_dict:
                s_dict[magazine[i]] = [i]
            else:
                s_dict[magazine[i]].append(i)
                
        point = 0
        for i in range(n):
            if ransomNote[i] not in s_dict: return False
            first_pos = s_dict[ransomNote[i]][0]
            if first_pos < point: 
                return False
            else:
                s_dict[ransomNote[i]].remove(first_pos)
                if s_dict[ransomNote[i]] == []: del s_dict[ransomNote[i]]
            
        return True