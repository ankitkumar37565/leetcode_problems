# 62.unique path
class Solution(object):
    def uniquePath_main(self,m,n,dp):
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                    continue;
                up,left=0,0
                if i>0:
                    up=dp[i-1][j]
                if j>0:
                    left=dp[i][j-1]
                dp[i][j]=up+left
        return dp[m-1][n-1]
    def uniquePaths(self,m, n):
        dp=[[-1 for j in range(n)] for i in range(m)]
        ans= self.uniquePath_main(m,n,dp)
        print(ans)
sol=Solution()
sol.uniquePaths(4,5)