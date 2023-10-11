from collections import deque

class Solution:
    def minimumMultiplications(self, arr, start, end):
        # Create a queue for storing the numbers as a result of multiplication
        # of the numbers in the array and the start number.
        q = deque([(start, 0])

        # Create a dist array to store the number of multiplications to reach
        # a particular number from the start number.
        dist = [float('inf')] * 100000
        dist[start] = 0
        mod = 100000

        # Multiply the start number with each of the numbers in the array
        # until we reach the end number.
        while q:
            node, steps = q.popleft()

            for num in arr:
                new_num = (num * node) % mod

                # If the number of multiplications is less than before
                # to reach a number, update the dist array.
                if steps + 1 < dist[new_num]:
                    dist[new_num] = steps + 1

                    # Whenever we reach the end number, return the calculated steps.
                    if new_num == end:
                        return steps + 1
                    q.append((new_num, steps + 1))

        # If the end number is unattainable.
        return -1

# Driver code
start = 3
end = 30

arr = [2, 5, 7]

obj = Solution()
ans = obj.minimumMultiplications(arr, start, end)

print(ans)
