class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        pre = [0, *accumulate(nums)]
        best, starts, w = inf, [], r - l + 1
        for t, cur in enumerate(pre[l:]):  # cur = pre[j], and the start t = j - l enters
            insort(starts, pre[t])
            if t >= w:
                del starts[bisect_left(starts, pre[t - w])]  # the start j - r - 1 leaves: too long
            k = bisect_left(starts, cur)  # the largest start below cur sits right before k
            if k and cur - starts[k - 1] < best:
                best = cur - starts[k - 1]
        return -1 if best == inf else best