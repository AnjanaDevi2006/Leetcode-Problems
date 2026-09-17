1from collections import deque
2class Solution:
3    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
4        n=len(nums)
5        result=[0]*(n-k+1)
6        dq=deque()
7        for right in range(n):
8            while dq and dq[0]<=right-k:
9                dq.popleft()
10            while dq and nums[dq[-1]]<nums[right]:
11                dq.pop()
12            dq.append(right)
13            if right>=k-1:
14                result[right-k+1]=nums[dq[0]]
15        return result