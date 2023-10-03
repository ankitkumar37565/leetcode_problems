# 210. Course Schedule II
class Solution:
    def dfsCheck(self, node, adj, vis, pathVis):
        vis[node] = 1
        pathVis[node] = 1

        # traverse for adjacent nodes
        for it in adj[node]:
            # when the node is not visited
            if not vis[it]:
                if self.dfsCheck(it, adj, vis, pathVis):
                    return True
            # if the node has been previously visited
            # but it has to be visited on the same path
            elif pathVis[it]:
                return True

        pathVis[node] = 0
        return False

    # Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        vis = [0] * V
        pathVis = [0] * V

        for i in range(V):
            if not vis[i]:
                if self.dfsCheck(i, adj, vis, pathVis):
                    return True

        return False

if __name__ == "__main__":
    # V = 11, E = 11
    adj = [[], [2], [3], [4, 7], [5], [6], [], [5], [9], [10], [8]]
    V = 11
    obj = Solution()
    ans = obj.isCyclic(V, adj)

    if ans:
        print("True")
    else:
        print("False")
