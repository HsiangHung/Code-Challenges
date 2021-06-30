#  443. String Compression (medium)
#  https://leetcode.com/problems/string-compression/
#  
class Solution(object):
    def compress(self, chars: List[str]) -> int:
        '''
        NOTE: the problems requies to modify chars in-place
        '''
        if len(chars) == 0: return 0
        
        ans = [chars[0]]
        repeat = 1
        i = 1
        while i < len(chars):
            if chars[i] == chars[i-1]:
                repeat += 1
                chars.pop(i)
            else:
                if repeat > 1:
                    self.insert_nums(i, chars, repeat)
                    i += 1
                repeat = 1
                i += 1
            
        if repeat > 1: self.insert_nums(i, chars, repeat)
            
        return len(chars)
    
    def insert_nums(self, i, chars, num):
        '''
        e.g. 130 -> "130" -> ["1", "3", "0"]
        '''
        num = str(num)
        for j in range(len(num)):
            chars.insert(i+j, num[j])
                    