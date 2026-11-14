class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        best = inf
        for k in range(l, r + 1):
            s = sum(nums[:k - 1])
            for i in range(k - 1, len(nums)):
                s += nums[i]  # the window nums[i - k + 1 .. i]
                if 0 < s < best:
                    best = s
                s -= nums[i - k + 1]
        return -1 if best == inf else best