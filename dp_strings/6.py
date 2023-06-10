# 115. Distinct Subsequences
class Solution(object):
    def numDistinct(self, s1, s2):
        n=len(s1)
        m=len(s2)
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(1,m+1):
            dp[0][i]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]== s2[j-1]:
                    dp[i][j] = (dp[i-1][j-1]+dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        print(dp)
        return dp[n][m]
s=Solution()
ans=s.numDistinct("babgbag","bag")
print(ans)