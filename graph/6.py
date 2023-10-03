# 1020. Number of Enclaves
from queue import Queue
class Solution:
    def numberOfEnclaves(self, grid):
        n = len(grid)
        m = len(grid[0])
        q = Queue()
        vis = [[0 for _ in range(m)] for _ in range(n)]

        # Traverse boundary elements
        for i in range(n):
            for j in range(m):
                # First row, first col, last row, last col
                if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                    # If it is land, store it in the queue
                    if grid[i][j] == 1:
                        q.put((i, j))
                        vis[i][j] = 1

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        while not q.empty():
            row, col = q.get()

            # Traverses all 4 directions
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                # Check for valid coordinates and land cell
                if 0 <= nrow < n and 0 <= ncol < m and vis[nrow][ncol] == 0 and grid[nrow][ncol] == 1:
                    q.put((nrow, ncol))
                    vis[nrow][ncol] = 1

        cnt = 0
        for i in range(n):
            for j in range(m):
                # Check for unvisited land cell
                if grid[i][j] == 1 and vis[i][j] == 0:
                    cnt += 1

        return cnt

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    obj = Solution()
    print(obj.numberOfEnclaves(grid))
