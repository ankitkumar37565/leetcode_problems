# Traingle minm path sum(120)
class Solution(object):
    def minimumTotal(self, triangle):
        m=len(triangle)
        n=len(triangle[m-1])
        dp=[[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[m-1][i]=triangle[m-1][i]
        for i in range(m-2,-1,-1):
            for j in range(i,-1,-1):
                    down=triangle[i][j]+dp[i+1][j]
                    downLeft=triangle[i][j]+dp[i+1][j+1]
                    dp[i][j]=min(down,downLeft)
        return dp[0][0]
s=Solution()
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])