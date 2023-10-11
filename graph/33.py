import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        # Create a list for storing the nodes as a tuple (dist, node)
        # where dist is the distance from source to the node.
        # We'll use a min-heap to maintain nodes in ascending order of distances.
        st = [(0, S)]
        
        # Initializing dist list with a large number to
        # indicate the nodes are unvisited initially.
        # This list contains distance from source to the nodes.
        dist = [float('inf')] * V
        dist[S] = 0
        
        while st:
            # Pop the node with the minimum distance from the heap
            dis, node = heapq.heappop(st)
            
            # Check all adjacent nodes of the popped element
            for adjNode, edgW in adj[node]:
                if dis + edgW < dist[adjNode]:
                    # If the current distance is smaller, update it
                    dist[adjNode] = dis + edgW
                    heapq.heappush(st, (dist[adjNode], adjNode))
        
        return dist

# Driver code
V = 3
S = 2
adj = [[] for _ in range(V)]
edges = [(1, 1), (2, 6), (2, 3), (0, 1), (1, 3), (0, 6)]

for u, v in edges:
    adj[u].append((v, 0))

obj = Solution()
res = obj.dijkstra(V, adj, S)

for i in range(V):
    print(res[i], end=" ")

print()