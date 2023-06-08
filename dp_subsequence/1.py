# 416. Partition Equal Subset Sum
class Solution(object):
    def canPartition(self, nums):
        size=len(nums)
        target=sum(nums)
        if target%2== 1:
            return False
        else:
            target=target//2
#             print(target)
            dp=[[False for i in range(target+1)] for j in range(size)]
            for i in range(size):
                dp[i][0]=True
#                 for first num its always true
            if nums[0]<=target:
                dp[0][nums[0]]=True
#                 check if first value equals target
            for i in range(1,size):
                for j in range(1,target+1):
                    notTaken=dp[i-1][j]
                    taken=False
                    if nums[i]<=j:
                        taken=dp[i-1][j-nums[i]]
                    dp[i][j]=taken or notTaken
            print(dp)
            return dp[size-1][target]
s=Solution()
s.canPartition([1,2,3,6,6,6])