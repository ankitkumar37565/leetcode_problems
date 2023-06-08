# 63.unique path II
class Solution(object):
    def main(self,m,n,grid,dp):
        for i in range(m):
            for j in range(n):
                if grid[i][j]== 1:
                    dp[i][j]=0
                    continue;
                if i==0 and j==0:
                    dp[i][j]=1
                    continue
                up,left=0,0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        print(dp)
        return dp[m-1][n-1]
    def uniquePathsWithObstacles(self, grid):
        m,n=len(grid), len(grid[0])
        dp=dp=[[0]*n]*m
        return self.main(m,n,grid,dp)
s=Solution()
s.uniquePathsWithObstacles([[0,1],[0,0]])

s.uniquePathsWithObstacles([[0,1]])