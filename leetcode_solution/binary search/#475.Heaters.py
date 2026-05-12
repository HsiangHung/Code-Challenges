class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """
        https://www.youtube.com/watch?v=K-Jz5eB1NIw&t=231s
        houses = [3,12,20,21,22,31]
        heaters = [1,4,6,10,15,16,23,24,29]

        * house = 3 : heaters = [1,4], dist = [2,1], radius = 1
        * house = 12: heaters = [10,15], dist = [2,3], radius = max(1,2) = 2
        * house = 20: heaters = [16,23], dist = [4,3], radius = max(2,3) = 3
        * house = 21: heaters = [16,23], dist = [5,2], radius = max(3,2) = 3
        * house = 22: heaters = [16,23], dist = [6,1], radius = max(3,1) = 3
        * house = 31: heaters = [29], dist = [2], radius = max(3,2) = 3
        * rasius = 3
        """

        # NOTE, heaters and houses are not gauranteed to be sorted
        heaters = sorted(heaters)
        houses = sorted(houses)

        def search(arr, house_num):
            if len(arr) <= 2:
                return min([abs(arr[i] - house_num) for i in range(len(arr))])

            mid = len(arr) // 2
            if house_num == arr[mid]:
                return 0
            elif house_num > arr[mid]:
                return search(arr[mid:], house_num) 
                # NOTE, we need to use arr[mid:], rather than arr[mid+1:]
                # since we need to consider arr[mid] closer to house than arr[mid+1]
            else:
                return search(arr[:mid+1], house_num)

        ans = 0
        for i in range(len(houses)):
            min_radius = search(heaters, houses[i])
            print(i, min_radius)
            ans = max(ans, min_radius)
        return ans
