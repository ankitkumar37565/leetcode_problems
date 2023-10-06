from collections import deque

class Solution:
    def topoSort(self, V, adj):
        indegree = [0] * V
        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1

        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        return topo

    def findOrder(self, dict, N, K):
        adj = [[] for _ in range(K)]
        for i in range(N - 1):
            s1 = dict[i]
            s2 = dict[i + 1]
            length = min(len(s1), len(s2))
            for ptr in range(length):
                if s1[ptr] != s2[ptr]:
                    adj[ord(s1[ptr]) - ord('a')].append(ord(s2[ptr]) - ord('a'))
                    break

        topo = self.topoSort(K, adj)
        ans = ""
        for it in topo:
            ans += chr(it + ord('a'))
        return ans

if __name__ == "__main__":
    N = 5
    K = 4
    dict = ["baa", "abcd", "abca", "cab", "cad"]
    obj = Solution()
    ans = obj.findOrder(dict, N, K)

    for ch in ans:
        print(ch, end=" ")
    print()
