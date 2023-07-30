# 673. Number of Longest Increasing Subsequence
class Solution(object):
    def findNumberOfLIS(self, arr):
        n = len(arr)
        dp = [1] * n
        ct = [1] * n
        maxi = 1

        for i in range(n):
            for prev_index in range(i):
                if arr[prev_index] < arr[i] and dp[prev_index] + 1 > dp[i]:
                    dp[i] = dp[prev_index] + 1
                    # inherit
                    ct[i] = ct[prev_index]
                elif arr[prev_index] < arr[i] and dp[prev_index] + 1 == dp[i]:
                    # increase the count
                    ct[i] += ct[prev_index]
            maxi = max(maxi, dp[i])

        nos = 0

        for i in range(n):
            if dp[i] == maxi:
                nos += ct[i]

        return nos