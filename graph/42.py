class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        
        # Initialize the matrix: -1 to infinity and diagonal to 0
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
                if i == j:
                    matrix[i][j] = 0
        
        # Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        # Convert infinity back to -1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = -1

# Driver code
V = 4
matrix = [
    [-1, 2, -1, -1],
    [1, -1, 3, -1],
    [-1, -1, -1, -1],
    [3, 5, 4, -1]
]

obj = Solution()
obj.shortest_distance(matrix)

for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()
