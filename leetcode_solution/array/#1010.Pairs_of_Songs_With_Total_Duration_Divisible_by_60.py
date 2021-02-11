#  1010. Pairs of Songs With Total Durations Divisible by 60 (medium)
#  https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
#
class Solution:
    '''
    prepare a dictionary, keys are minutes to % 60 == 0 and values are indices.
    e.g. time = [30,20,150,100,40] gives lack_time_dict = {30: [0,2], 40:[1], 20:[3,4]}
         time = [60,60,60] gives lack_time_dict = {0: [0,1,2]}
         
    for x+ y % 60 == 0, x remaining + y remaing % 60 == 0.
    iterate i = 0, 1,...n-1, and make sure j from lack_time_dict[60 - i] > i.
    '''
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        lack_time_dict ={}
        for idx, t in enumerate(time):
            i = (t-1) // 60 + 1
            lack_time_dict[i*60-t] = lack_time_dict.get(i*60-t, []) + [idx]
        
        ans = 0
        for idx, t in enumerate(time):
            
            i = (t // 60) + 1
            lack_duration = i*60-t
            
            if 60 - lack_duration in lack_time_dict:
                for jdx in lack_time_dict[60 - lack_duration]:
                    if jdx > idx:
                        ans += 1

        return ans
            
            
        