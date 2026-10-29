class ST:
    def __init__(self, arr):
        self.n = len(arr)
        self.st = [0] * (4 * self.n)
        self.build(1, 0, self.n - 1, arr)
    
    def build(self, node, l, r, arr):
        if l == r:
            self.st[node] = arr[l]
            return self.st[node]
        
        mid = l + (r - l) // 2
        self.build(node * 2, l, mid, arr)
        self.build(node * 2 + 1, mid + 1, r, arr)
        self.st[node] = self.st[node * 2] ^ self.st[node * 2 + 1]
        return self.st[node]
    
    def update(self, node, l, r, idx, val):
        if l == r:
            self.st[node] = val
            return self.st[node]
        
        mid = l + (r - l) // 2
        if idx <= mid: self.update(node * 2, l, mid, idx, val)
        else: self.update(node * 2 + 1, mid + 1, r, idx, val)
        self.st[node] = self.st[node * 2] ^ self.st[node * 2 + 1]
        return self.st[node]
    
    def query(self, node, l, r, ql, qr):
        if ql <= l and qr >= r: return self.st[node]
        if qr < l or ql > r: return 0
        mid = l + (r - l) // 2
        lc = self.query(node * 2, l, mid, ql, qr)
        rc = self.query(node * 2 + 1, mid + 1, r, ql, qr)
        return lc ^ rc

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = defaultdict(list)
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        par = [-1] * n
        depth = [0] * n
        order = []
        q = deque([0])
        while q:
            node = q.popleft()
            order.append(node)
            for nei in adj[node]:
                if nei == par[node]: continue
                par[nei] = node
                depth[nei] = depth[node] + 1
                q.append(nei)
        
        size = [1] * n
        heavy = [-1] * n
        def dfs(node):
            largest = 0
            for nei in adj[node]:
                if nei == par[node]: continue
                dfs(nei)
                size[node] += size[nei]
                if size[nei] > largest:
                    largest = size[nei]
                    heavy[node] = nei
        dfs(0)

        head = [0] * n
        pos = [0] * n
        self.curr = 0
        def dfs2(node, h):
            head[node] = h
            pos[node] = self.curr
            self.curr += 1
            if heavy[node] != -1: dfs2(heavy[node], h)
            for nei in adj[node]:
                if nei == par[node] or nei == heavy[node]: continue
                dfs2(nei, nei)
        dfs2(0, 0)
        
        masks = [0] * n
        for node in range(n):
            masks[pos[node]] = 1 << (ord(s[node]) - ord('a'))
        st = ST(masks)

        res = []
        for q in queries:
            parts = q.split()
            if parts[0] == 'update':
                node = int(parts[1])
                c = parts[2]
                i = pos[node]
                nmask = 1 << (ord(c) - ord('a'))
                st.update(1, 0, n - 1, i, nmask)
            else:
                a = int(parts[1])
                b = int(parts[2])
                xor = 0
                while head[a] != head[b]:
                    if depth[head[a]] < depth[head[b]]: a, b = b, a
                    xor ^= st.query(1, 0, n - 1, pos[head[a]], pos[a])
                    a = par[head[a]]
                if depth[a] > depth[b]: a, b = b, a
                xor ^= st.query(1, 0, n - 1, pos[a], pos[b])
                res.append(xor & (xor - 1) == 0)
        
        return res