# 494. Target Sum
class Solution(object):
    def findTargetSumWays(self, nums, target):
        totalsum=0
        n=len(nums)
        for i in range(n):
            totalsum +=nums[i]
        if(totalsum-target) <0 or ((totalsum-target)%2):
            return 0
        target=(totalsum-target)//2
        dp=[[0 for i in range(target+1)] for j in range (n)]
        if nums[0]==0:
            dp[0][0]=2
        else:
            dp[0][0]=1
        if nums[0] !=0 and nums[0] <=target:
            dp[0][nums[0]]=1
        max=int(1e9+7)
        for i in range(1,n):
            for j in range(target+1):
                nt=dp[i-1][j]
                t=0
                if nums[i] <=j:
                    t=dp[i-1][j-nums[i]]
                dp[i][j]=(nt+t)%max
        return dp[n-1][target]