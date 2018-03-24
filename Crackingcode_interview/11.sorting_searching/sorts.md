
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
def insertionSort(arr):
    arr_len = len(arr)
    subArr = [arr[0]]
    arr.pop(0)
    for i in range(arr_len-1):
        #print (i, len(subArr))
        isInsert = False
        for j in range(len(subArr)):
            if subArr[j] > arr[0]:
                #print (j, subArr[j], arr[0])
                subArr.insert(j, arr[0])
                arr.pop(0)
                isInsert = True
                break  ## Note!! this break is super important !!!!
        if isInsert == False: 
            subArr.append(arr[0])
            arr.pop(0)
        print (len(subArr), subArr, arr)
    return subArr
            
arr = [4, 54, 26, 93, 17, 77, 31, 44, 1, 0]      
print (insertionSort(arr))
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






