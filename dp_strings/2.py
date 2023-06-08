# 516. Longest Palindromic Subsequence
def lcs(s1):
    s2=s1[::-1]
    n=len(s1)
    dp=[[-1 for i in range(n+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
        dp[0][i]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=0+max(dp[i-1][j],dp[i][j-1])
    return dp[n][n]
ans=lcs("bbabcbcab")
print(ans)