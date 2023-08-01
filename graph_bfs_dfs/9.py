from collections import deque

class Solution:
    def bfs(self, row, col, vis, grid):
        # mark it visited
        vis[row][col] = 1
        q = deque([(row, col)])
        n, m = len(grid), len(grid[0])

        # until the queue becomes empty
        while q:
            row, col = q.popleft()

            # traverse in the neighbors and mark them if it's land
            for delrow, delcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nrow, ncol = row + delrow, col + delcol
                # neighbor row and column is valid, and is an unvisited land
                if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == '1' and not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol))

    # Function to find the number of islands.
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        # create visited array and initialize to 0
        vis = [[0 for _ in range(m)] for _ in range(n)]
        cnt = 0
        for row in range(n):
            for col in range(m):
                # if not visited and is a land
                if not vis[row][col] and grid[row][col] == '1':
                    cnt += 1
                    self.bfs(row, col, vis, grid)
        return cnt

if __name__ == "__main__":
    # n: row, m: column
    grid = [
        ['0', '1', '1', '1', '0', '0', '0'],
        ['0', '0', '1', '1', '0', '1', '0']
    ]

    obj = Solution()
    print(obj.numIslands(grid))
