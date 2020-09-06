# #93. Restore IP Addresses
#
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        looping through positions of ".", and also make sure no "001" exists, 
        so do str(int(s[i:j])) == s[i:j] 
        '''
        if len(s) <= 3 or len(s) > 12: return []
        
        ips = set({})
        for i in range(1, 4):
            if i <= len(s)-3 and int(s[:i]) <= 255 and str(int(s[:i])) == s[:i]:
                for j in range(i+1, i+4):
                    if j <= len(s)-2 and int(s[i:j]) <= 255 and str(int(s[i:j])) == s[i:j]:
                        for k in range(j+1, j+4):
                            if k<= len(s)-1 and int(s[j:k]) <= 255 and int(s[k:]) <= 255 and str(int(s[j:k])) == s[j:k] and str(int(s[k:])) == s[k:]:
                                ips.add(s[:i]+"."+s[i:j]+"."+s[j:k]+"."+s[k:])
        return ips
