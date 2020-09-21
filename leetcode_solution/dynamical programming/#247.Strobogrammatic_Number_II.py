# #247. Strobogrammatic Number II
#
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        '''
        when n is odd, always insert the middle with "0", "1", "8" only
        when n is even, always insert both sides, but "6" and "9" together
        also NOTE "00" for n = 2, otherwise cannot get numbers like "1001".
        '''
        rotate = {"0": "0", "1": "1", "8": "8", "9": "6", "6": "9"}
        
        dp = {1: set(["1", "0", "8"]), 2: set(["00", "11", "88", "69", "96"])} 
                
        i = 3
        while i <= n:
            
            dp[i] = set({})
            
            if i % 2 == 1:
                for subset in dp[i-1]:
                    len_s = int(len(subset)/2)
                    for x in ["0", "1", "8"]:
                        new_s = subset[:len_s] + x + subset[len_s:]
                        dp[i].add(new_s)
                        
            elif i % 2 == 0:
                for subset in dp[i-2]:
                    len_s = int(len(subset)/2)
                    for x in ["0", "1", "8", "6", "9"]:
                        for j in range(len_s):
                            new_s = subset[:j] + x + subset[j:]
                            new_s = new_s[:len(new_s)-j] + rotate[x] + new_s[len(new_s)-j:] 
                            dp[i].add(new_s)

            i += 1
            
        return [x for x in dp[n] if len(x) == len(str(int(x)))]