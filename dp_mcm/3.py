# Evaluate Boolean Expression to True | Partition DP: DP 52
def evaluateExp(exp):
    mod = 1000000007
    n = len(exp)
    dp = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n):
            if i > j:
                continue
            for isTrue in range(2):
                # Base case:
                if i == j:
                    if isTrue == 1:
                        dp[i][j][isTrue] = 1 if exp[i] == 'T' else 0
                    else:
                        dp[i][j][isTrue] = 1 if exp[i] == 'F' else 0
                    continue

                ways = 0
                for ind in range(i + 1, j, 2):
                    lT = dp[i][ind - 1][1]
                    lF = dp[i][ind - 1][0]
                    rT = dp[ind + 1][j][1]
                    rF = dp[ind + 1][j][0]

                    if exp[ind] == '&':
                        if isTrue:
                            ways = (ways + (lT * rT) % mod) % mod
                        else:
                            ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lF * rF) % mod) % mod
                    elif exp[ind] == '|':
                        if isTrue:
                            ways = (ways + (lF * rT) % mod + (lT * rF) % mod + (lT * rT) % mod) % mod
                        else:
                            ways = (ways + (lF * rF) % mod) % mod
                    else:
                        if isTrue:
                            ways = (ways + (lF * rT) % mod + (lT * rF) % mod) % mod
                        else:
                            ways = (ways + (lF * rF) % mod + (lT * rT) % mod) % mod

                dp[i][j][isTrue] = ways

    return dp[0][n - 1][1]

if __name__ == "__main__":
    # exp = "F|T^F"
    exp = "|(f,f,f,t)"
    ways = evaluateExp(exp)
    print("The total number of ways:", ways)
