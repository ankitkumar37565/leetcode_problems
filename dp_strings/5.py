# 1092. Shortest Common Supersequence
class Solution(object):
    def shortestCommonSupersequence(self, s1, s2):
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
        i=n
        j=m
        lcsLength=dp[n][m]
        sequence=""
        while i>0 and j>0:
            if s1[i-1]==s2[j-1]:
                sequence+=s1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                sequence+=s1[i-1]
                i-=1
            else:
                sequence+=s2[j-1]
                j-=1
        while i>0:
            sequence+=s1[i-1]
            i-=1
        while j>0:
            sequence+=s2[j-1]
            j-=1
        sequence=sequence[::-1]
        return sequence
        
# s=Solution()
# ans=s.shortestCommonSupersequence("abac","cab")
# print(ans)