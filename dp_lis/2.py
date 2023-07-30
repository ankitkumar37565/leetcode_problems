class Solution(object):
    def largestDivisibleSubset(self, arr):
        n = len(arr)
        arr.sort()

        dp = [1] * n
        hash_map = [i for i in range(n)]

        for i in range(n):
            for prev_index in range(i):
                if arr[i] % arr[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    hash_map[i] = prev_index

        ans = -1
        last_index = -1

        for i in range(n):
            if dp[i] > ans:
                ans = dp[i]
                last_index = i

        result = [arr[last_index]]
        while hash_map[last_index] != last_index:
            last_index = hash_map[last_index]
            result.append(arr[last_index])

        result.reverse()
        return result
            