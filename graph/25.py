from collections import deque

class Solution:
    def eventualSafeNodes(self, V, adj):
        adjRev = [[] for _ in range(V)]
        indegree = [0] * V

        for i in range(V):
            for it in adj[i]:
                adjRev[it].append(i)
                indegree[i] += 1

        q = deque()
        safeNodes = []

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            safeNodes.append(node)

            for it in adjRev[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        safeNodes.sort()
        return safeNodes

if __name__ == "__main__":
    adj = [[1], [2], [3, 4], [4, 5], [6], [6], [7], [], [1, 9], [10], [8], [9]]
    V = 12

    obj = Solution()
    safeNodes = obj.eventualSafeNodes(V, adj)

    for node in safeNodes:
        print(node, end=" ")
    print()
