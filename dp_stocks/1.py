# 121. Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        maxProfit=0
        minimum=prices[0]
        size=len(prices)
        for i in range(1,size):
            currProfit=prices[i]-minimum
            maxProfit=max(maxProfit,currProfit)
            minimum=min(minimum,prices[i])
        # print(maxProfit)
        return maxProfit
# s=Solution()
# s.maxProfit([7,1,5,3,6,4])
# s.maxProfit([7,6,4,3,1])