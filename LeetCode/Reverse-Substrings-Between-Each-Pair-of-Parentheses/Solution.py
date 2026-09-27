1class Solution:
2    def reverseParentheses(self, s: str) -> str:
3        n = len(s)
4        link = [0] * n
5        stk = res = []
6
7        for i, c in enumerate(s):
8            if c == '(':
9                stk.append(i)
10            elif c == ')':
11                j = stk.pop()
12                link[i] = j
13                link[j] = i
14
15        dr, i = 1, 0
16        while i < n:
17            if s[i] >= 'a':
18                res.append(s[i])
19            else:
20                i = link[i]
21                dr = -dr
22
23            i += dr
24
25        return ''.join(res)