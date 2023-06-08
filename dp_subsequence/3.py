# (322). Coin Change
class Solution(object):
    def coinChange(self, coins, amount):
        size=len(coins)
        dp=[[0 for i in range(amount+1)] for j in range(size)]
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = int(1e9)
        for i in range(1,size):
            for j in range(amount+1):
                notTaken = 0+dp[i-1][j]
                taken=int(1e9)
                if coins[i]<=j:
                    taken=1+dp[i][j-coins[i]]
                dp[i][j]=min(notTaken,taken)
        if dp[size-1][amount]>=int(1e9):
            return -1
        else:
            return dp[size-1][amount]
        
s=Solution()
s.coinChange([1,2,5],11)