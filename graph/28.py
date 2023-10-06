from collections import deque

class Solution:
    def shortestPath(self, edges, N, M, src):
        # Create an adjacency list of size N for storing the undirected graph.
        adj = [[] for _ in range(N)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # A dist array of size N initialized with a large number to
        # indicate that initially all the nodes are untraversed.
        dist = [float('inf')] * N
        
        # BFS Implementation.
        dist[src] = 0
        q = deque()
        q.append(src)
        
        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if dist[node] + 1 < dist[neighbor]:
                    dist[neighbor] = 1 + dist[node]
                    q.append(neighbor)

        # Updated shortest distances are stored in the resultant array 'ans'.
        # Unreachable nodes are marked as -1.
        ans = [-1 if dist[i] == float('inf') else dist[i] for i in range(N)]
        return ans

N = 9
M = 10
edges = [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6], [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]]

obj = Solution()
ans = obj.shortestPath(edges, N, M, 0)

for i in range(len(ans)):
    print(ans[i], end=" ")
