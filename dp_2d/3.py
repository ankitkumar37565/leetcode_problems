# minimum path sum(64)
class Solution(object):
    def minPathSum(self,grid):
        m,n=len(grid),len(grid[0])
        dp=[[0]*n]*m
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up=left=grid[i][j]
                    if i>0:
                        up +=dp[i-1][j]
                    else:
                        up +=int(1e9)
                    if j>0:
                        left +=dp[i][j-1]
                    else:
                        left +=int(1e9)
                    print(up,left)
                    dp[i][j]=min(up,left)
        return dp[m-1][n-1]

s=Solution()
s.minPathSum([[1,2,3],[4,5,6]])