from collections import defaultdict, deque

class Solution:
    def CheapestFlight(self, n, flights, src, dst, K):
        # Create the adjacency list to depict airports and flights in
        # the form of a graph.
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))

        # Create a queue which stores the node and their distances from the
        # source in the form of (stops, (node, cost)) with ‘stops’ indicating 
        # the no. of nodes between src and current node.
        q = deque([(0, (src, 0))])

        # Distance array to store the updated distances from the source.
        dist = [float('inf')] * n
        dist[src] = 0

        # Iterate through the graph using a queue like in Dijkstra with 
        # popping out the element with min stops first.
        while q:
            stops, (node, cost) = q.popleft()

            # We stop the process as soon as the limit for the stops reaches.
            if stops > K:
                continue

            for adjNode, edW in adj[node]:
                # We only update the queue if the new calculated dist is
                # less than the prev and the stops are also within limits.
                if cost + edW < dist[adjNode]:
                    dist[adjNode] = cost + edW
                    q.append((stops + 1, (adjNode, cost + edW)))

        # If the destination node is unreachable return ‘-1’
        # else return the calculated dist from src to dst.
        if dist[dst] == float('inf'):
            return -1
        return dist[dst]

# Driver code
n = 4
src = 0
dst = 3
K = 1

flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]

obj = Solution()
ans = obj.CheapestFlight(n, flights, src, dst, K)

print(ans)
