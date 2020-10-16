# 825. Friends Of Appropriate Ages
#
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        '''
        [16,17,18] no request 18 -> 16 since 18/2+7 = 16 = 16
        [20,30,100,110,120] no request 30->20 since 30/2+7 = 22 > 20
        https://blog.csdn.net/fuxuemingzhu/article/details/83183022
        '''
        
        ages_dict = {}
        for age in ages:
            ages_dict[age] = ages_dict.get(age, 0) + 1

        requests = 0
        
        for A in sorted(ages_dict.keys()):
            for B in range(int(0.5*A) + 7 +1, A+1): # do NOT loop ages, time exceed
                if B in ages_dict:
                    requests += ages_dict[A]*(ages_dict[B] - int(A == B))
                
        return requests