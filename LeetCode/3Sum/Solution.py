1
2class Solution:
3    def threeSum(self, nums: List[int]) -> List[List[int]]:
4        nums.sort()
5        ans = []
6
7        n = len(nums)
8
9        for i in range(n - 2):
10
11            if i > 0 and nums[i] == nums[i - 1]:
12                continue
13
14            left = i + 1
15            right = n - 1
16
17            while left < right:
18
19                total = nums[i] + nums[left] + nums[right]
20
21                if total == 0:
22                    ans.append([nums[i], nums[left], nums[right]])
23
24                    while left < right and nums[left] == nums[left + 1]:
25                        left += 1
26
27                    while left < right and nums[right] == nums[right - 1]:
28                        right -= 1
29
30                    left += 1
31                    right -= 1
32
33                elif total < 0:
34                    left += 1
35
36                else:
37                    right -= 1
38
39        return ans