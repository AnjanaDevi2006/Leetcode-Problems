1class Solution:
2    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
3        ans = ""
4        n = len(s)
5
6        for i in range(n):
7
8            oneCnt = 0
9            cur = ""
10
11            for j in range(i, n):
12
13                cur += s[j]
14
15                if s[j] == '1':
16                    oneCnt += 1
17
18                # More than k ones can never become valid again
19                if oneCnt > k:
20                    break
21
22                if oneCnt == k:
23                    if ans == "" or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
24                        ans = cur
25
26        return ans