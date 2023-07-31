# mcm tabulation
def matrixMultiplication(arr):
    N = len(arr)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(1, N):
        dp[i][i] = 0

    for l in range(2, N):
        for i in range(1, N - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i-1]*arr[k]*arr[j])

    return dp[1][N-1]

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print("The minimum number of operations are", matrixMultiplication(arr))
