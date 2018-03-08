# Intersect of two sorted arrays
#
#
def intersectSortedArray(nums1, nums2):
    
    m, n = len(nums1), len(nums2)
    
    intersect = []
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            intersect.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1

    return intersect
    
        
        
    