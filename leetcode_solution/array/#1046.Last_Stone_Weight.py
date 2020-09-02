# 1046. Last Stone Weight
#
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 0: return 0
        if len(stones) == 1: return stones[0]
        
        stones = sorted(stones)
        
        while len(stones) > 1:
            x = stones.pop(-1)
            y = stones.pop(-1)
            diff = abs(x-y)
            if x != y:
                if len(stones) == 0:
                    stones.append(diff)
                else:
                    stones = self.insert_elem(diff, stones)

        if len(stones) == 0: return 0
        return stones[0]
            
    def insert_elem(self, diff, stones):
        
        if diff <= stones[0]:
            stones.insert(0, diff)
        elif diff >= stones[-1]:
            stones.append(diff)
        else:
            i = 0
            while stones[i] <= diff:
                i += 1
            stones.insert(i, diff)
        return stones
        