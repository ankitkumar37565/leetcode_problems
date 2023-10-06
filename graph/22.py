# topo sort using bfs
from collections import defaultdict, deque

class Solution:
    def topoSort(self, V, adj):
        indegree = [0] * V
        for i in range(V):
            for neighbor in adj[i]:
                indegree[neighbor] += 1

        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return topo

if __name__ == "__main__":
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    V = 6
    obj = Solution()
    ans = obj.topoSort(V, adj)

    for node in ans:
        print(node, end=" ")
    print()
