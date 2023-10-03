# 542. 01 Matrix
from collections import deque
class Solution(object):
    def updateMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        dist = [[0 for _ in range(m)] for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append(((i, j), 0))
                    vis[i][j] = 1
                else:
                    vis[i][j] = 0

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        while q:
            row, col = q[0][0]
            steps = q[0][1]
            q.popleft()
            dist[row][col] = steps

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0:
                    vis[nrow][ncol] = 1
                    q.append(((nrow, ncol), steps + 1))

        return dist


