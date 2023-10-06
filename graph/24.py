# course schedule 1,2
from collections import defaultdict, deque

class Solution:
    def findOrder(self, V, m, prerequisites):
        adj = [[] for _ in range(V)]
        for it in prerequisites:
            adj[it[1]].append(it[0])

        indegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1

        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    queue.append(it)

        if len(topo) == V:
            return topo
        return []

    def isPossible(self, V, prerequisites):
        adj = [[] for _ in range(V)]
        for it in prerequisites:
            adj[it[0]].append(it[1])

        indegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1

        queue = deque()
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    queue.append(it)

        if len(topo) == V:
            return True
        return False


if __name__ == "__main__":
    N = 4
    M = 3

    prerequisites = [[0, 1], [1, 2], [2, 3]]

    obj = Solution()
    ans = obj.findOrder(N, M, prerequisites)

    for task in ans:
        print(task, end=" ")
    print()

    prerequisites = [(1, 0), (2, 1), (3, 2)]
    N = 4

    obj = Solution()
    ans = obj.isPossible(N, prerequisites)

    if ans:
        print("YES")
    else:
        print("NO")
