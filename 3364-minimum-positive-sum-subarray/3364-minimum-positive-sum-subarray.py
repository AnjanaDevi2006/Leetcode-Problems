class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float('inf')

        for i in range(n - l + 1):
            total = 0

            for j in range(i, min(n, i + r)):
                total += nums[j]

                size = j - i + 1

                if size >= l and total > 0:
                    ans = min(ans, total)

        if ans == float('inf'):
            return -1

        return ans