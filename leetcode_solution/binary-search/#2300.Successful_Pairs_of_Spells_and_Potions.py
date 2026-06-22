#
# 2300. Successful Pairs of Spells and Potions
#
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    
        def search(target, arr):
            """
            This func looks for index where arr[i] < target but arr[i+1] >= target
            """
            if arr[0] >= target:
                return 0
            elif arr[-1] < target:
                return -1 

            l, r = 0, len(arr)-1

            while l <= r:
                mid = (r + l) // 2
                if arr[mid-1] < target and arr[mid] >= target:
                    return mid
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        potions = sorted(potions)
        n, m = len(spells), len(potions)

        res = []
        for i in range(len(spells)):

            min_req = float(success/spells[i])

            n_success = 0
            if potions[-1] < min_req:
                res.append(0)
            elif potions[0] > min_req:
                res.append(m)
            else:
                idx = search(min_req, potions)
                res.append(m - idx)
        return res