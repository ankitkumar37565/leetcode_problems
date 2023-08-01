# 130. Surrounded Regions
class Solution(object):
    def dfs(self, row, col, vis, mat, delrow, delcol):
            vis[row][col] = 1
            n = len(mat)
            m = len(mat[0])
            
            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if 0 <= nrow < n and 0 <= ncol < m and not vis[nrow][ncol] and mat[nrow][ncol] == 'O':
                    self.dfs(nrow, ncol, vis, mat, delrow, delcol)

    def solve(self, mat):
        n=len(mat)
        m=len(mat[0])
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        vis = [[0 for _ in range(m)] for _ in range(n)]

        for j in range(m):
            if not vis[0][j] and mat[0][j] == 'O':
                self.dfs(0, j, vis, mat, delrow, delcol)

            if not vis[n - 1][j] and mat[n - 1][j] == 'O':
                self.dfs(n - 1, j, vis, mat, delrow, delcol)

        for i in range(n):
            if not vis[i][0] and mat[i][0] == 'O':
                self.dfs(i, 0, vis, mat, delrow, delcol)

            if not vis[i][m - 1] and mat[i][m - 1] == 'O':
                self.dfs(i, m - 1, vis, mat, delrow, delcol)

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and mat[i][j] == 'O':
                    mat[i][j] = 'X'

        return mat

