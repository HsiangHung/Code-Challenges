#[#646] Maximum Length of Pair Chain
#
# If this problem uses dynamical programming to solve, the time will be exceeded.
# What we have to do, is to while constructing the chain, always find the pair whose
# first element > the second element of of the last pair in the chain, and the corresponding
# second element is minimal.
#
#
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        min_val, min_pair = pairs[0][1], pairs[0]
        for pair in pairs:
            if pair[1] <= min_val:
                min_val, min_pair = pair[1], pair
        dp = [min_pair]
        
        while len(dp) < len(pairs):
            min_val, min_pair = None, None
            for pair in pairs:
                if pair != dp[-1] and pair[0] > dp[-1][1]:
                    if min_val is None:
                        min_val, min_pair = pair[1], pair
                    elif min_val is not None and pair[1] < min_val:
                        min_val, min_pair = pair[1], pair
        
            if dp[-1] == min_pair or min_pair is None:
                return len(dp)
            else:
                dp.append(min_pair)

        return len(pairs)