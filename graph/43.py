class Solution:
    def findCity(self, n, m, edges, distanceThreshold):
        dist = [[float('inf')] * n for _ in range(n)]
        
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                        continue
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        minCities = n
        cityNo = -1
        
        for city in range(n):
            reachableCities = 0
            for adjCity in range(n):
                if dist[city][adjCity] <= distanceThreshold:
                    reachableCities += 1

            if reachableCities <= minCities:
                minCities = reachableCities
                cityNo = city
        
        return cityNo

# Driver code
n = 4
m = 4
edges = [
    [0, 1, 3],
    [1, 2, 1],
    [1, 3, 4],
    [2, 3, 1]
]
distanceThreshold = 4

obj = Solution()
cityNo = obj.findCity(n, m, edges, distanceThreshold)
print(f"The answer is node: {cityNo}")
