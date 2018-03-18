## [Leetcode#453] Minimum Moves to Equal Array Elements
#
#  add 1 for n-1 elements equivalent to minus 1 for 1 element
#
#  to equal all, each of them needs to be decrease as the minimum number.
#
#  e.g. [5,3,7]->[6,4,7] ~ [5,3,7]->[5,3,6]
#              ->[7,5,7] ~        ->[5,3,5]
#              ->[8,6,7] ~        ->[5,3,4]
#              ->[8,7,8] ~        ->[4,3,4]
#              ->[8,8,9] ~        ->[3,3,4]
#              ->[9,9,9] ~        ->[3,3,3]
#
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        return sum(nums)-min(nums)*len(nums)