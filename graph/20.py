# toposort using dfs
class Solution:
    def dfs(self, node, vis, stack, adj):
        vis[node] = 1
        for neighbor in adj[node]:
            if not vis[neighbor]:
                self.dfs(neighbor, vis, stack, adj)
        stack.append(node)

    def topoSort(self, V, adj):
        vis = [0] * V
        stack = []
        for i in range(V):
            if not vis[i]:
                self.dfs(i, vis, stack, adj)

        ans = []
        while stack:
            ans.append(stack.pop())

        return ans

if __name__ == "__main__":
    adj = [[], [], [3], [1], [0, 1], [0, 2]]
    V = 6
    obj = Solution()
    ans = obj.topoSort(V, adj)

    for node in ans:
        print(node, end=" ")
    print()
