1class Solution:
2    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
3        max_count=0
4        current_count=0
5        for num in nums:
6            if num==1:
7                current_count+=1
8            else:
9                max_count=max(max_count,current_count)
10                current_count=0
11        return max(max_count,current_count)