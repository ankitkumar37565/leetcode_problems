# mcm
def matrixMultiplication(arr):
    N = len(arr)
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    
    def f(i, j):
        # base condition
        if i == j:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
        
        mini = float('inf')
        
        # partitioning loop
        for k in range(i, j):
            ans = f(i, k) + f(k+1, j) + arr[i-1]*arr[k]*arr[j]
            mini = min(mini, ans)
            
        dp[i][j] = mini
        return mini

    i = 1
    j = N - 1

    return f(i, j)

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    print("The minimum number of operations is", matrixMultiplication(arr))
