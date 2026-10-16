class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        t = [0] * (4 * n)
        lz = [0] * (4 * n)

        def push(x: int, l: int, r: int) -> None:
            if lz[x]:
                m = (l + r) // 2
                t[2 * x] += lz[x] * (m - l + 1)
                lz[2 * x] += lz[x]
                t[2 * x + 1] += lz[x] * (r - m)
                lz[2 * x + 1] += lz[x]
                lz[x] = 0

        def upd(x: int, l: int, r: int, a: int, b: int) -> None:
            if b < l or r < a:
                return
            if a <= l and r <= b:
                t[x] += r - l + 1
                lz[x] += 1
                return
            push(x, l, r)
            m = (l + r) // 2
            upd(2 * x, l, m, a, b)
            upd(2 * x + 1, m + 1, r, a, b)
            t[x] = t[2 * x] + t[2 * x + 1]

        def qry(x: int, l: int, r: int, a: int, b: int) -> int:
            if b < l or r < a:
                return 0
            if a <= l and r <= b:
                return t[x]
            push(x, l, r)
            m = (l + r) // 2
            return qry(2 * x, l, m, a, b) + qry(2 * x + 1, m + 1, r, a, b)

        mod = 10**9 + 7
        sq = 0
        ans = 0
        last = [-1] * 100001
        for j in range(n):
            p = last[nums[j]]
            s = qry(1, 0, n - 1, p + 1, j)
            sq = (sq + 2 * (s % mod) + (j - p)) % mod
            upd(1, 0, n - 1, p + 1, j)
            ans = (ans + sq) % mod
            last[nums[j]] = j
        return ans