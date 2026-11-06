class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0 
        arr2.sort()
        left = 0
        right = len(arr2) - 1

        for i in range(len(arr1)):
            left = 0
            right = len(arr2) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if abs(arr1[i] - arr2[mid]) <= d:
                    count += 1
                    break
                elif arr1[i] < arr2[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return len(arr1) - count
        