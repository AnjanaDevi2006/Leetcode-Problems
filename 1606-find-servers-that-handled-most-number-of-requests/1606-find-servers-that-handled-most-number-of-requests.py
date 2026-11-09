class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq
        from sortedcontainers import SortedList

        free_servers = SortedList(range(k))  # List of available servers
        busy_servers = []  # Min-heap for busy servers
        handled_requests = [0] * k  # Count of handled requests per server

        for i in range(len(arrival)):
            # Free up servers that have completed their tasks by the current arrival time
            while busy_servers and busy_servers[0][0] <= arrival[i]:
                _, server_index = heapq.heappop(busy_servers)
                free_servers.add(server_index)  # Add back to available servers

            # Determine the server to handle the current request
            server_index = i % k
            
            # If the preferred server is busy, find the next available one
            if server_index not in free_servers:
                # Find the next available server in a circular manner
                idx = free_servers.bisect_right(server_index)  # Get index of the next available server
                if idx == len(free_servers):  # If no servers available after the preferred one
                    if not free_servers:  # Check if there are any free servers at all
                        continue  # No server available, drop the request
                    server_index = free_servers[0]  # Wrap around to the first available server
                else:
                    server_index = free_servers[idx]  # Assign the next available server

            # If we found a valid server
            if server_index in free_servers:
                # Mark the server as busy until the request is complete
                finish_time = arrival[i] + load[i]
                heapq.heappush(busy_servers, (finish_time, server_index))
                handled_requests[server_index] += 1
                free_servers.remove(server_index)  # Remove from free servers

        # Find the maximum number of handled requests
        max_requests = max(handled_requests)
        # Return the list of servers that handled the max number of requests
        return [i for i in range(k) if handled_requests[i] == max_requests]