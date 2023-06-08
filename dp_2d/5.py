# (931) Minimum Falling Path Sum¶
class Solution(object):
    def minFallingPathSum(self, mat):
        mInt=int(1e9)
        m=n=len(mat)
        dp=[[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[m-1][i]=mat[m-1][i]
        for i in range(m-2,-1,-1):
            for j in range(n):
                dleft,d,dright=mat[i][j],mat[i][j]+dp[i+1][j],mat[i][j]
                if j==0:
                    dleft +=mInt
                else:
                    dleft +=dp[i+1][j-1]
                if j==n-1:
                    dright +=mInt
                else:
                    dright +=dp[i+1][j+1]
                dp[i][j]=min(dleft,d,dright)
        for i in range(n):
            mInt=min(mInt,dp[0][i])
        return mInt
s=Solution()
s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])