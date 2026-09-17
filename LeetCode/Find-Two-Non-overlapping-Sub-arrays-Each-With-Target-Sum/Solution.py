def minSumOfLengths(self, A: List[int], target: int) -> int:
    n = len(A)
    res, tot, j = n + 1, 0, 0

    # dp[i] = min len of a valid subarray ending before index i
    dp = [n] * (n + 1)
    for i in range(n):
        tot += A[i]

        # Move right while the sum is below target. move down while it exceeds target.
        while tot > target:
            tot -= A[j]
            j += 1
        dp[i + 1] = dp[i]
        if tot == target:
            Len = i - j + 1

            # dp[j] is the min len in the box before j, so it cannot overlap.
            res = min(res, Len + dp[j])
            dp[i + 1] = min(dp[i], Len)
            
    return -1 if res == n + 1 else res