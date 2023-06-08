# 583. Delete Operation for Two Strings
class Solution(object):
    def minDistance(self, s1, s2):
        n=len(s1)
        m=len(s2)
        dp=[[-1 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[i][0]=0
        for i in range(m+1):
            dp[0][i]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return (n-dp[n][m] +m-dp[n][m])
s=Solution()
ans=s.minDistance("sea","eat")
print(ans)
ans=s.minDistance("leetcode","etco")
print(ans)


