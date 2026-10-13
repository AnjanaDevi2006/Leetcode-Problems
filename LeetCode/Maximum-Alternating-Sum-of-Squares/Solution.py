1class Solution:
2    def maxAlternatingSum(self, nums: List[int]) -> int:
3        A = sorted(a * a for a in nums)
4        return sum(A) - sum(A[:len(A) // 2]) * 2