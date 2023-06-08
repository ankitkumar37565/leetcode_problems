# 518. Coin Change II
class Solution(object):
    def change(self, amount, coins):
        n=len(coins)
        dp=[[0 for i in range(amount+1)] for j in range(n)]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i]=1
        for i in range(1,n):
            for j in range(amount+1):
                nt=dp[i-1][j]
                t=0
                if coins[i] <=j:
                    t=dp[i][j-coins[i]]
                dp[i][j]=nt+t
        return dp[n-1][amount]