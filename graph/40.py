import heapq

class Solution:
    def countPaths(self, n, roads):
        # Creating an adjacency list for the given graph.
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Defining a priority queue (min heap).
        pq = [(0, 0)]

        # Initializing the dist array and the ways array
        # along with their first indices.
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        # Define modulo value
        mod = 10**9 + 7

        # Iterate through the graph with the help of a priority queue
        # just as we do in Dijkstra's Algorithm.
        while pq:
            dis, node = heapq.heappop(pq)

            for adjNode, edW in adj[node]:
                # This ‘if’ condition signifies that this is the first
                # time we’re coming with this short distance, so we push
                # in PQ and keep the number of ways the same.
                if dis + edW < dist[adjNode]:
                    dist[adjNode] = dis + edW
                    heapq.heappush(pq, (dis + edW, adjNode))
                    ways[adjNode] = ways[node]

                # If we again encounter a node with the same short distance
                # as before, we simply increment the number of ways.
                elif dis + edW == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod

        # Finally, we return the number of ways to reach
        # (n-1)th node modulo 10^9+7.
        return ways[n - 1] % mod

# Driver code
n = 7
edges = [
    [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], 
    [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]
]

obj = Solution()
ans = obj.countPaths(n, edges)

print(ans)
