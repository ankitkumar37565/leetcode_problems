# (2035). Partition Array Into Two Arrays to Minimize Sum Difference
# Input: nums = [3,9,7,3]
# Output: 2
# Explanation: One optimal partition is: [3,9] and [7,3].
# The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
class Solution(object):
    def minimumDifference(self, arr):
        size=len(arr)
        totSum=0
        for i in range(size):
            totSum +=abs(arr[i])
        dp=[[False for i in range(totSum+1)] for j in range(size+1)]
        for i in range(size):
            dp[i][0]=True
        dp[0][abs(arr[0])]=True
        for i in range(1,size):
            for j in range(1,totSum+1):
                notTaken=dp[i-1][j]
                taken=False
                if abs(arr[i])<=j:
                    taken=dp[i-1][j-abs(arr[i])]
                dp[i][j]=taken or notTaken
        mini=int(1e9)
        for i in range(totSum+1):
            if dp[size-1][i]==True:
                diff=(i-(totSum-i))
                mini=min(diff,mini)
        return mini
s=Solution()
ans=s.minimumDifference([3,9,7,3])
# ans=s.minimumDifference([-3,3])
# ans=s.minimumDifference([2,-1,0,4,-2,-9])
print(ans)