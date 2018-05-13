## [GeeksForGeeks] Combination Sum
#   
#  Uber
#
def combination_sum(arr, target):
    if len(arr) == 0 or len([x for x in arr if x > target]) == len(arr):
        return []
        
    comb_sum = []
    for num in arr:
        if num == target:
            comb_sum.append([num])
        elif num < target:
            poss_comb = combination_sum(arr, target-num)
            if len(poss_comb) > 0:
                for x in poss_comb:
                    x.insert(0, num)
                    x = sorted(x)
                    comb_sum.append(x)

    comb_sum = list(set([tuple(sorted(lst)) for lst in comb_sum]))

    return [[y for y in lst] for lst in comb_sum]


arr = [7,2,6,5]
target = 16


arr = [6, 5, 7, 1, 8, 2, 9, 9, 7, 7, 9]
target = 6

arr = [5, 2, 2, 6]
target = 3
print (combination_sum(arr, target))