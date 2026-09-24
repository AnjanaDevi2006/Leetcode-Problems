1class Solution:
2    def maxProduct(self, nums: list[int]) -> int:
3        prefix=0
4        suffix=0
5        ans=float('-inf')
6        n=len(nums)
7        for i in range(n):
8            if prefix==0:
9                prefix=1
10            if suffix==0:
11                suffix=1
12            prefix *= nums[i]
13            suffix *= nums[n-1-i]
14            ans=max(ans,prefix,suffix)
15        return ans