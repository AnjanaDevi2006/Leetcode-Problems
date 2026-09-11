1
2class Solution:
3    def maxArea(self, height: List[int]) -> int:
4
5        left = 0
6        right = len(height) - 1
7
8        ans = 0
9
10        while left < right:
11
12            width = right - left
13
14            h = min(height[left], height[right])
15
16            area = width * h
17
18            ans = max(ans, area)
19
20            if height[left] < height[right]:
21                left += 1
22            else:
23                right -= 1
24
25        return ans