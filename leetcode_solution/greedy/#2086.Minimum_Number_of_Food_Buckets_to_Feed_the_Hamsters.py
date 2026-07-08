#
#  2086. Minimum Number of Food Buckets to Feed the Hamsters
#
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        """
        ref: https://www.youtube.com/watch?v=jvPUA3QpR5A
        since loop through from left to right
        first try to fill right (larger chance be shared) 
        and then fill the left. If "H" has no "." nearby, return -1
        """
        n = len(hamsters)

        ans = 0
        i = 0
        while i < n:
            if hamsters[i] == "H":
                if i < n-1 and hamsters[i+1] == ".":
                    ans += 1
                    i += 2
                elif i > 0 and hamsters[i-1] == ".":
                    ans += 1
                else:
                    return -1

            i += 1
        
        return ans

