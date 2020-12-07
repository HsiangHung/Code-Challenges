#  791. Custom Sort String (medium)
#  https://leetcode.com/problems/custom-sort-string/
#
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        '''
        NOTE letters in T can be repeated, so using dictionary to store the frequency
        loop through S by order, and insert the remaning letters of T not showing in S anywhere.
        '''
        t_dict = self.str_dict(T)
        
        string = []
        for letter in S:
            if letter in t_dict:
                string.append(letter*t_dict[letter])
                del t_dict[letter]
        
        if len(t_dict) > 0:
            for x in t_dict:
                string.append(x*t_dict[x])
                
        return "".join(string)
        
    def str_dict(self, s):
        s_dict = {}
        for i, letter in enumerate(s):
            s_dict[letter] = s_dict.get(letter, 0) + 1
        return s_dict
    
            