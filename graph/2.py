# 994. Rotting Oranges
from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        days = 0
        tot = 0
        cnt = 0
        rotten = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    tot += 1
                if grid[i][j] == 2:
                    rotten.append((i, j))

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while rotten:
            k = len(rotten)
            cnt += k
            while k > 0:
                x, y = rotten.popleft()
                k -= 1
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != 1:
                        continue
                    grid[nx][ny] = 2
                    rotten.append((nx, ny))

            if rotten:
                days += 1

        return days if tot == cnt else -1
