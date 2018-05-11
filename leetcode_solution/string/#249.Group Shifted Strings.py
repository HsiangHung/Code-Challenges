## [Leetcode#249] Group Shifted Strings
#   
#  Google, Uber
#
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        # trick: find relative distance between two sucessive characters
        # 
        alpha = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
                 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
                 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23,
                 'y': 24, 'z': 25}
        
        str_dict ={}
        for string in strings:
            shift = []
            for i in range(1, len(string)):
                diff = alpha[string[i]] - alpha[string[i-1]]
                if diff < 0: diff += 26
                shift.append(diff)
                
            shift = tuple(shift)
            
            if shift not in str_dict:
                str_dict[shift] = [string]
            else:
                str_dict[shift].append(string)
                
        return [str_dict[x] for x in str_dict]
                
                