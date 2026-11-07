class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res, unavailable = [], []
        available = [(weight, id) for id, weight in enumerate(servers)]
        heapify(available)

        for time, task in enumerate(tasks):
            while unavailable and unavailable[0][0] == time:
                _, weight, id = heappop(unavailable)
                heappush(available, (weight, id))

            if len(available) > 0:
                weight, id = heappop(available)
                heappush(unavailable, (time + task, weight, id))
                res.append(id)
            else:
                finishTime, weight, id = heappop(unavailable)
                heappush(unavailable, (finishTime + task, weight, id))
                res.append(id)

        return res