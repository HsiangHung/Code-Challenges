#  461. Hamming Distance (easy)
#  https://leetcode.com/problems/hamming-distance/
#
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a, b = self.get_binary(x), self.get_binary(y)
        
        if len(a) > len(b):
            b = [0]*(len(a)-len(b)) + b
        elif len(a) < len(b):
            a = [0]*(len(b)-len(a)) + a
            
        return sum([1 for x, y in zip(a, b) if x != y])
        
        
    def get_binary(self, x):
        if x <= 1:
            return [x]
        else:
            return self.get_binary(x//2) + [ (x % 2) ]