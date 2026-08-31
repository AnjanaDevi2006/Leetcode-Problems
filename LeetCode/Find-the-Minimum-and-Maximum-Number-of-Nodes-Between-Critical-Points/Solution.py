1class Solution:
2    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
3        def is_crit(x, y, z):
4            return (y.val - x.val) * (y.val - z.val) > 0
5
6        c = [0, 0]
7        Min, i = inf, 1
8
9        prev, curr, nxt = head, head.next, head.next.next        
10
11        while nxt:
12            if is_crit(prev, curr, nxt):
13                if c[0]: Min = min(Min, i - c[c[1] > 0])
14                c[c[0] > 0] = i
15
16            prev, curr, nxt = curr, nxt, nxt.next
17            i += 1
18
19        return [[Min, c[1] - c[0]], [-1, -1]][not c[1]]