#  187. Repeated DNA Sequences (medium)
#  https://leetcode.com/problems/repeated-dna-sequences/
#
class Solution:
    '''
    https://blog.csdn.net/fuxuemingzhu/article/details/83017233
    http://bookshadow.com/weblog/2015/02/06/leetcode-repeated-dna-sequences/
    '''
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        f = 4**9
        
        mapping = {"A": 0, "C": 1, "G": 2, "T":3}
        DNA = set({})
        ans = set({})
        for i in range(len(s)-10+1):
            if i == 0:
                num = self.get_num(s[:10], mapping)
                hex_s = self.encode(num)
                DNA.add(hex_s)
            else:
                num -= mapping[s[i-1]]
                num = num // 4
                num += mapping[s[i+9]]*f
                hex_s = self.encode(num)

                if hex_s in DNA: 
                    ans.add(s[i:i+10])
                else:
                    DNA.add(hex_s)

        return list(ans)
        
    
    def encode(self, num):
        '''
        convert 
        '''
        return num & 0xFFFFF
    
    def get_num(self, s, mapping):
        sum = 0
        factor = 1
        for i in range(len(s)):
            sum += mapping[s[i]]*factor
            factor *= 4
        return sum