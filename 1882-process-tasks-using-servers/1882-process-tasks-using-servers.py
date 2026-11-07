from heapq import heapify, heappush, heappop

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        t = 0
        j = 0
        available = [(w, i) for i, w in enumerate(servers)]
        returns = []
        heapify(available)
        assignments = [None] * len(tasks)
        for j, d in enumerate(tasks):
            if len(available) == 0 or (len(returns) > 0 and returns[0][0] <= j):
                t = returns[0][0]
                while len(returns) > 0 and returns[0][0] == t:
                    _, i = heappop(returns)
                    heappush(available, (servers[i], i))
            if t < j:
                t = j
            end = t + d
            _, i = heappop(available)
            assignments[j] = i
            heappush(returns, (end, i))
        return assignments