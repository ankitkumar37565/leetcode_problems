def maxSumAfterPartitioning(num, k):
    n = len(num)
    dp = [0] * (n + 1)
    
    for ind in range(n - 1, -1, -1):
        length = 0
        maxi = float('-inf')
        maxAns = float('-inf')
        
        for j in range(ind, min(ind + k, n)):
            length += 1
            maxi = max(maxi, num[j])
            currSum = length * maxi + dp[j + 1]
            maxAns = max(maxAns, currSum)
        
        dp[ind] = maxAns
    
    return dp[0]

if __name__ == "__main__":
    num = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    maxSum = maxSumAfterPartitioning(num, k)
    print("The maximum sum is:", maxSum)
