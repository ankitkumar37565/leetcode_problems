def count_squares(n, m, arr):
    dp = [[0] * m for _ in range(n)]

    for j in range(m):
        dp[0][j] = arr[0][j]
    for i in range(n):
        dp[i][0] = arr[i][0]

    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], min(dp[i - 1][j - 1], dp[i][j - 1]))

    total_sum = sum(sum(row) for row in dp)
    return total_sum

if __name__ == "__main__":
    arr = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 0]
    ]
    n, m = 3, 4
    squares = count_squares(n, m, arr)
    print(f"The number of squares: {squares}")
