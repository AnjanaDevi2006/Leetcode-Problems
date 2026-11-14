class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        pre = [0, *accumulate(nums)]
        best, starts = inf, SortedList()  # pre[i] for every start i that fits the end j
        for j in range(l, len(pre)):
            starts.add(pre[j - l])  # start j - l: length l
            if j > r:
                starts.remove(pre[j - r - 1])  # start j - r - 1: length r + 1, too long
            k = starts.bisect_left(pre[j])  # the largest pre[i] < pre[j] sits right before k
            if k:
                best = min(best, pre[j] - starts[k - 1])
        return -1 if best == inf else best