1class Solution:
2    def maximumLengthSubstring(self, s: str) -> int:
3        count = {}
4        i = res = 0
5        for j, c in enumerate(s):
6            count[c] = count.get(c, 0) + 1
7            while count[c] > 2:
8                count[s[i]] -= 1
9                i += 1
10            res = max(res, j - i + 1)
11        return res