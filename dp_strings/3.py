# 1312. Minimum Insertion Steps to Make a String Palindrome
# abcaa aacba
# aba aca aaa
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any insertions.
class Solution(object):
    def minInsertions(self, s1):
        s2=s1[::-1]
        n=len(s1)
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        for i in range(n+1):
            dp[0][i]=0
            dp[i][0]=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][n]
s=Solution()
ans=s.minInsertions("abcaa")
print(ans)
ans=s.minInsertions("zzazz")
print(ans)
ans=s.minInsertions("mbadm")
print(ans)
ans=s.minInsertions("leetcode")
print(ans)
