class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        asc = list(range(n))
        desc = asc[::-1]
        rev = nums[::-1]
        best = float('inf')

        def test(a, target, goal, cost):
            nonlocal best
            j = a.index(target)
            if a[j:] + a[:j] == goal:
                best = min(best, cost + j)

        test(nums, 0, asc, 0)
        test(rev, 0, asc, 1)
        test(nums, n - 1, desc, 1)
        test(rev, n - 1, desc, 2)

        return -1 if best == float('inf') else best