# # 611. Valid Triangle Number
#
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        consider side1_+side_2 > side_3 to form a triangle, where side > 0
        the possible combination could be
        [side, side, side]    n*(n-1)*(n-2)/3!
        [side_1, side_1, side_2]  n1*(n1-1)/2! * n2
        [side_1, side_2, side_2]  n1 * n2*(n2-1)/2!
        [side_1, side_2, side_3]  n1 * n2 * n3
        '''
        count = {}
        for num in nums:
            if num > 0:
                count[num] = count.get(num, 0) + 1

        sides = sorted(count.keys())
        
        num_tri = 0
        for i in range(len(sides)):

            if count[sides[i]] >= 3: 
                num_tri += self.get_three_side(count[sides[i]])
            
            j = i+1
            while j <= len(sides)-1:
                
                if count[sides[i]] >= 2 and 2*sides[i] > sides[j]:   # NOTE s1+s1 > s2
                    num_tri += self.get_two_side(count[sides[i]])*count[sides[j]]
                
                if count[sides[j]] >= 2:
                    num_tri += count[sides[i]]*self.get_two_side(count[sides[j]])
            
                k = j+1                
                while k <= len(sides)-1 and sides[i] + sides[j] > sides[k]: # s1+s2>s3
                    num_tri += count[sides[i]]*count[sides[j]]*count[sides[k]]
                    k += 1
                
                j += 1
        
        return num_tri
    
    def get_three_side(self, n):
        return n*(n-1)*(n-2) // 6
    
    def get_two_side(self, n):
        return n*(n-1) // 2