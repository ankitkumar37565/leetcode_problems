# 1.(70) Climbing Stairs
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<1):
            return 1
        dp=[1]*2
        for i in range (2,n+1):
            dp[1],dp[0]=dp[1]+dp[0],dp[1]
        return dp[1]
s=Solution()
s.climbStairs(10)