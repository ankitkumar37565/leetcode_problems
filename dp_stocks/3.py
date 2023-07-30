# 123. Best Time to Buy and Sell Stock III
class Solution(object):
    def maxProfit(self, prices):
        size=len(prices)
        dp=[[-1]*2 ]*(size+1)
        dp[size][0]=dp[size][1]=0
        for i in range(size-1,0,-1):
            for j in range(2):
                for cap in range(1,3,-1):
                    profit=0
                    if j==0:
                        profit=max(dp[i+1][0],-prices[i]+dp[i+1][1])
                    if j==1:
                        profit=max(dp[i+1][1],prices[i]+dp[i+1][0])
                    dp[i][j]=profit
            # print(dp)
        return dp[0][0]
s=Solution()
s.maxProfit([7,1,5,3,6,4])
# s.maxProfit([1,2,3,4,5])