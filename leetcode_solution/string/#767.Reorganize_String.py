#  767. Reorganize String (medium)
#  https://leetcode.com/problems/reorganize-string/
#
class Solution:
    '''
    find count for each char, and find the char to have max freq
    e.g. char having max freq is "a"
    ans = ['a','a','a',...,'a']
    if the remaining count < the number of 'a': return ''
    else, insert as ['ab', 'ab', 'ac', ...'al'] => ['abk', 'abm',...'al'], 
          to gaurantee 'a' not next to each other
    '''
    def reorganizeString(self, S: str) -> str:
        
        s_dict = {}
        for char in S:
            s_dict[char] = s_dict.get(char, 0) + 1
            
        max_freq, max_char = 0, None
        for char in s_dict:
            if s_dict[char] > max_freq:
                max_freq, max_char = s_dict[char], char
                
        if sum([s_dict[char] for char in s_dict if char != max_char]) < max_freq-1:
            return ""
        else:
            s_dict = sorted(s_dict.items(), key = lambda x: x[1], reverse = True)
            
            char, freq = s_dict.pop(0)
            ans = [char]*freq
            
            i = 0
            while len(s_dict) > 0:
                char, freq = s_dict.pop(0)                
                for _ in range(freq):
                    if i == len(ans): i = 0  # insert with a cycle of len(ans)
                    ans[i] = ans[i] + char
                    i += 1
                    
            return "".join(ans)
            
            