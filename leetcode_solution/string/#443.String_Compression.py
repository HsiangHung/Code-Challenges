## [Leetcode#443] String Compression
##
##  
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) <= 1: 
            return len(chars)
        
        count = 1
        x = 1
        for i in range(1, len(chars)):
            if chars[x] == chars[x-1]:
                count += 1 
                del chars[x]
            elif chars[x] != chars[x-1]:
                if count > 1:
                    count = str(count)
                    for j in range(len(count)):
                        chars.insert(x, count[j])
                        x += 1
                    
                x += 1
                count = 1
        
        if count > 1:
            count = str(count)
            for j in range(len(count)):
                chars.append(count[j])
                
        return len(chars)
