class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf')

        for k in range(l, r + 1):
            window_sum = sum(nums[:k])
            if window_sum > 0:
                min_sum = min(min_sum, window_sum)

            for i in range(k, n):
                window_sum += nums[i] - nums[i - k]
                if window_sum > 0:
                    min_sum = min(min_sum, window_sum)

        return min_sum if min_sum != float('inf') else -1