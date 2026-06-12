#
#  15. 3Sum
#  
class Solution:
    def twoSum(self, nums_dict: Dict[int, int], target: int) -> List[List[int]]:
        res = []
        for x in nums_dict:
            if target - x != x:
                if target - x in nums_dict:
                    res.append(sorted([x, target - x]))
            else: # e.g. [-1, -1] target = 2
                if nums_dict[x] > 1:
                    res.append([x, target - x])
        return res

        
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pos, neg, zero_ct = {}, {}, 0
        for num in nums:
            if num > 0:
                pos[num] = pos.get(num, 0) + 1
            elif num < 0:
                neg[num] = neg.get(num, 0) + 1
            else:
                zero_ct += 1
        
        if len(neg) == 0 and zero_ct < 3:
            return []

        # 3 sum has the following scenarios:
        # 1. 3 zeros
        # 2. 1 zero + 1 pos + 1 neg
        # 3. 0 zeros + 1(2) pos + 2(1) neg

        res = set({})
        if zero_ct >= 3:
            res.add((0, 0, 0))
        
        # now 1 zero + 1 pos + 1 neg
        if zero_ct >= 1:
            for x in pos:
                if -x in neg:
                    res.add((-x, 0, x))
        
        # now 0 zeros + 1 (2) pos + 1 (1) neg
        for x in pos:
            is_two_sum = self.twoSum(neg, -x)
            if len(is_two_sum) > 0:
                for y in is_two_sum:
                    res.add(tuple(y + [x]))
        
        for x in neg:
            is_two_sum = self.twoSum(pos, -x)
            if len(is_two_sum) > 0:
                for y in is_two_sum:
                    res.add(tuple([x] + y))

        return [list(x) for x in res]
