class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10 ** 4
        BIG = 10 ** 9
        cost = [[BIG] * (n + 1) for _ in range(n + 1)]

        for d in range(1, n // 2 + 1):
            tmp = [[0] * (n + 1) for _ in range(n + 1)]
            for length in range(2 * d, n + 1, d):
                for idx in range(n - length + 1):
                    ops = 0
                    for o in range(d):
                        if s[idx + o] != s[idx + length - d + o]:
                            ops += 1
                    tmp[idx][length] = ops + tmp[idx + d][length - 2 * d]
                    if tmp[idx][length] < cost[idx][length]:
                        cost[idx][length] = tmp[idx][length]

        @lru_cache(maxsize=None)
        def solve(idx: int, parts: int) -> int:
            if idx == n or parts == 0:
                return 0 if (idx == n and parts == 0) else INF
            res = INF
            for length in range(2, n - idx + 1):
                res = min(res, cost[idx][length] + solve(idx + length, parts - 1))
            return res

        return solve(0, k)