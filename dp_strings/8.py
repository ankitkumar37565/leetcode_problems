# 44. Wildcard Matching
class Solution(object):
    def isAllStars(self,s,i):
        for i in range(1,i+1):
            if s[i-1] !="*":
                return False
        return True
    def isMatch(self, s2,s1):
        n=len(s1)
        m=len(s2)
        dp=[[False for i in range(m+1)] for j in range(n+1)]
        dp[0][0]=True
        for i in range(1,m+1):
            dp[0][i]=False
        for i in range(1,n+1):
            dp[i][0]=self.isAllStars(s1,i)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[i-1]==s2[j-1] or s1[i-1]=="?":
                    dp[i][j]=dp[i-1][j-1]
                else:
                    if s1[i-1]=="*":
                        dp[i][j]=dp[i-1][j] or dp[i][j-1]
                    else:
                        dp[i][j]=False
        return dp[n][m]
s=Solution()
# ans=s.isMatch("ab*cd","abdefcd")
ans=s.isMatch("aa","*")
print(ans)