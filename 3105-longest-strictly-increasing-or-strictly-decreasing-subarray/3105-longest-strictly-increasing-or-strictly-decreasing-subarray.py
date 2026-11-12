class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        incr = decr = longest = 1
        for a, b in pairwise(nums):
            incr = incr + 1 if a < b else 1
            decr = decr + 1 if a > b else 1
            longest = max(incr, decr, longest)

        return longest