class Solution(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],1+dp[j])

        return max(dp)