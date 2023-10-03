# 785. Is Graph Bipartite?
class Solution(object):
    def dfs(self, node, col, color, adj):
        color[node] = col

        # Traverse adjacent nodes
        for it in adj[node]:
            # If uncoloured
            if color[it] == -1:
                if not self.dfs(it, not col, color, adj):
                    return False
            # If previously coloured and have the same colour
            elif color[it] == col:
                return False

        return True

    def isBipartite(self, adj):
        V=len(adj)
        color = [-1] * V

        # For connected components
        for i in range(V):
            if color[i] == -1:
                if not self.dfs(i, 0, color, adj):
                    return False

        return True
