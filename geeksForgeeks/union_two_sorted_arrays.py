# Union of two sorted arrays
#
#
def unionSortedArray(nums1, nums2):
    
    m, n = len(nums1), len(nums2)
    
    union = []
    i, j = 0, 0
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            union.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            union.append(nums2[j])
            j += 1
        else:
            union.append(nums1[i])
            i += 1
    
    if j == n:
        union += nums1[i:]
    else:
        union += nums2[j:]

    return union
        
        
    