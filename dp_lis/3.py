# 1048. Longest String Chain

class Solution(object):
    def compare(self,s1, s2):
        if len(s1) != len(s2) + 1:
            return False
        
        first, second = 0, 0
        
        while first < len(s1):
            if second < len(s2) and s1[first] == s2[second]:
                first += 1
                second += 1
            else:
                first += 1
                
        return first == len(s1) and second == len(s2)

    def longestStrChain(self,arr):
        n = len(arr)
        arr.sort(key=len)
        dp = [1] * n
        maxi = 1
        
        for i in range(n):
            for prev_index in range(i):
                if self.compare(arr[i], arr[prev_index]) and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    
            if dp[i] > maxi:
                maxi = dp[i]
                
        return maxi