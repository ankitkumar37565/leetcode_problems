# 547. Number of Provinces
class Solution(object):
    def dfs(self, node, adjLs, vis):
        vis[node] = 1
        for it in adjLs[node]:
            if not vis[it]:
                self.dfs(it, adjLs, vis)
    def findCircleNum(self, adj):
        V=len(adj)
        adjLs = [[] for _ in range(V)]

        # Convert adjacency matrix to adjacency list
        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)

        vis = [0] * V
        cnt = 0
        for i in range(V):
            if not vis[i]:
                cnt += 1
                self.dfs(i, adjLs, vis)

        return cnt
