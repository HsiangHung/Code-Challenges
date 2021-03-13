
# Algorithms: sorting

## Bubble Sort
```Python
# Bubble: O(n^2)
def bubble_sort(nums):
    ordered = False
    while not ordered:
        for i in range(1, len(nums)):
            
            if i == 1: ordered = True
            
            ordered = ordered and nums[i] > nums[i-1]
            if nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                         
    return nums
          
print (bubble_sort([4, 54, 26, 93, 17, 77, 31, 44, 1, 0]))
print (bubble_sort([32, 13, 17, 2, 8, 19, 100, 1]))
```

##  Selection Sort
```Python
## Selection sort: O(n^2)
def selection_sort(nums):
    compare_len = len(nums)
    while compare_len > 0:
        max_val, max_idx = nums[0], 0
        for i in range(1, compare_len):
            if nums[i] > max_val:
                max_val, max_idx = nums[i], i
        
        nums[compare_len-1], nums[max_idx] = nums[max_idx], nums[compare_len-1]
        compare_len -= 1
        
    return nums
     
print (selection_sort([4, 54, 26, 93, 17, 77, 31, 44, 1, 0]))
print (selection_sort([32, 13, 17, 2, 8, 19, 100, 1]))
```

## Insertion Sort
```Python
## Insertion sort: O(n^2)
def insertion_sort(nums):
    sorted_nums = [nums[0]]
    nums.remove(nums[0])
    while len(nums) > 0:
        
        target = nums[0]
        if target < sorted_nums[0]:
            i = 0
        elif target > sorted_nums[-1]:
            i = len(sorted_nums)
        else:
            for i in range(1, len(sorted_nums)):
                if sorted_nums[i] > target > sorted_nums[i-1]:
                    break
        
        sorted_nums.insert(i, target)
        nums.remove(target)
        
    return sorted_nums
                 
print (insertion_sort([4, 54, 26, 93, 17, 77, 31, 44, 1, 0]))
print (insertion_sort([32, 13, 17, 2, 8, 19, 100, 1]))
```

## Merge Sort
```Python
## Merge Sort: O(n*logn)
def mergeSort(arr):
    arr_len = len(arr)
    if arr_len <= 1: return arr
    left = arr[:int(arr_len/2)]
    right = arr[int(arr_len/2):]
    print (left,right)
    left = mergeSort(left)
    right = mergeSort(right)
    #print ('----')
    return insertionSort(left+right)
    
    
arr = [54, 26, 93, 17, 77, 31, 44, 1, 0]      
print(mergeSort(arr))
````
The merge sort can be written more concisely using helper function 'merge_list':
```Python
def merge_sort(nums):
    if len(nums) == 1: return nums
    
    middle = len(nums) // 2
    left, right = nums[:middle], nums[middle:]
    
    return merge_list(merge_sort(left), merge_sort(right))


def merge_list(num1, num2):
    '''This fucntion is used to merge two sorted arrays as one sorted array'''
    sorted_nums = []
    idx1, idx2 = 0, 0
    while idx1 < len(num1) or idx2 < len(num2):
        
        if num1[idx1] <= num2[idx2]:
            sorted_nums.append(num1[idx1])
            idx1 += 1
        else:
            sorted_nums.append(num2[idx2])
            idx2 += 1
            
        if idx1 == len(num1):
            sorted_nums += num2[idx2:]
            idx2 = len(num2)
        elif idx2 == len(num2): 
            sorted_nums += num1[idx1:]
            idx1 = len(num1)
            
    return sorted_nums
    
    
print (merge_sort([32, 13, 17, 2, 8, 19, 100, 1]))
```


## Quick Sort
```Python
# O(nlogn), worst O(n^2)
'''
https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm
https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html (code source)
https://www.youtube.com/watch?v=SLauY6PpjW4
'''
def quickSort(arr, first, last):
   if first < last:
       splitpoint = partition(arr, first, last)
       quickSort(arr, first, splitpoint-1)
       quickSort(arr, splitpoint+1, last)

def partition(arr, first, last):
    pivot = arr[first]
    L, R = first+1, last
    done = False
    while not done:
        while L <= R and arr[L] <= pivot:
            L += 1
        while L <= R and arr[R] >= pivot:
            R -= 1

        if R < L:
            done = True
        else:
            arr[L], arr[R] = arr[R], arr[L]

    arr[first], arr[R] = arr[R], arr[first]
    return R


arr = [54,26,20,17,55,31,44,77]
# arr = [6,3,1,8,5,2,7,9,15]
arr = [35,33,42,10,14,19,27,44,26,31]
quickSort(arr, 0, len(arr)-1)
print(arr)
```

# Algorithms: Search Median

## Quick Select 
```Python
'''
find k-smallest element, help median value

https://www.geeksforgeeks.org/quickselect-algorithm/  (code source)
https://www.youtube.com/watch?v=BP7GCALO2v8 

the partition module comes from 
https://runestone.academy/runestone/books/published/pythonds/SortSearch/TheQuickSort.html 
which is easier to understand
'''
def partition(arr, first, last):
    pivot = arr[first]
    L, R = first+1, last
    done = False
    while not done:
        while L <= R and arr[L] <= pivot:
            L += 1
        while L <= R and arr[R] >= pivot:
            R -= 1

        if R < L:
            done = True
        else:
            arr[L], arr[R] = arr[R], arr[L]

    arr[first], arr[R] = arr[R], arr[first]

    return R

def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1: # if k is smaller than number of elements in array
        # Partition the array around last element and get position of pivot element in sorted array
        index = partition(arr, l, r)
 
        if (index - l == k - 1): # if position is same as k
            return arr[index]
        elif (index - l > k - 1): # If position is more, recur for left subarray 
            return kthSmallest(arr, l, index - 1, k)
        else: # Else recur for right subarray 
            return kthSmallest(arr, index + 1, r, k - index + l - 1)

    return INT_MAX


arr = [ 10, 4, 5, 8, 6, 11, 26 ]
# arr = [35,33,42,10,14,19,27,44,26,31]
n = len(arr)
k = 6
print(str(k)+"-th smallest element is ", end = "")
print(kthSmallest(arr, 0, n - 1, k))
print (arr)
```