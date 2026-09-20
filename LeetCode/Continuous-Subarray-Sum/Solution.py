1class Solution:
2    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
3        remainder_map = {0:-1}
4        prefixsum = 0
5        for i in range(len(nums)):
6            prefixsum +=nums[i]
7            remainder = prefixsum % k
8            if remainder in remainder_map:
9                if i-remainder_map[remainder]>=2:
10                    return True
11            else:
12                remainder_map[remainder]=i
13        return False