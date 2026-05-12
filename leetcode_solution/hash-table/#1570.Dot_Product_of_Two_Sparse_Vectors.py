# 1570. Dot Product of Two Sparse Vectors
#
class SparseVector:
    def __init__(self, nums: List[int]):
        
        vector = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                vector[i] = nums[i]
        
        self.vector = vector

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        return sum([self.vector[i]*vec.vector[i] for i in self.vector if i in vec.vector])
   
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)