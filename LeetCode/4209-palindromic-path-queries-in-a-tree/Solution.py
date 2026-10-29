class Solution:
    def palindromePath(self, n, edges, s, queries):
        from collections import deque

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = 17
        tin, tout, dep = [0]*n, [0]*n, [0]*n
        up = [[0]*n for _ in range(LOG)]
        bit = [0]*(n+2)
        timer = 0

        def dfs(u, p):
            nonlocal timer
            timer += 1
            tin[u] = timer
            up[0][u] = p

            for j in range(1, LOG):
                up[j][u] = up[j-1][up[j-1][u]]

            for v in g[u]:
                if v != p:
                    dep[v] = dep[u] + 1
                    dfs(v, u)
            tout[u] = timer

        def add(i, x):
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def update(u, x):
            add(tin[u], x)
            add(tout[u]+1, x)

        def summ(i):
            x = 0
            while i:
                x ^= bit[i]
                i -= i & -i
            return x

        def lca(u, v):
            if dep[u] < dep[v]:
                u, v = v, u

            for j in range(LOG-1, -1, -1):
                if dep[u] - (1 << j) >= dep[v]:
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG-1, -1, -1):
                if up[j][u] != up[j][v]:
                    u, v = up[j][u], up[j][v]
            return up[0][u]

        dfs(0, 0)
        s = list(s)

        for u in range(n):
            update(u, 1 << (ord(s[u])-97))

        ans = []
        for q in queries:
            a = q.split()
            u = int(a[1])

            if a[0] == "update":
                c = a[2]
                update(u, (1 << (ord(s[u])-97)) ^
                          (1 << (ord(c)-97)))
                s[u] = c
            else:
                v = int(a[2])
                w = lca(u, v)
                m = summ(tin[u]) ^ summ(tin[v]) ^ (1 << (ord(s[w])-97))
                ans.append((m & (m-1)) == 0)

        return ans