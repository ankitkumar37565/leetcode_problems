import heapq

class Solution:
    def MinimumEffort(self, heights):
        n = len(heights)
        m = len(heights[0]

        # Create a priority queue containing pairs of cells 
        # and their respective distance from the source cell in the 
        # form (diff, (row of cell, col of cell)).
        pq = [(0, (0, 0))]

        # Create a distance matrix with initially all the cells marked as
        # unvisited and the dist for the source cell (0,0) as 0.
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 0

        # The following delta rows and delta columns arrays are created such that
        # each index represents each adjacent node that a cell may have 
        # in a direction.
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        # Iterate through the matrix by popping the elements out of the queue
        # and pushing whenever a shorter distance to a cell is found.
        while pq:
            diff, (row, col) = heapq.heappop(pq)

            # Check if we have reached the destination cell,
            # return the current value of difference (which will be min).
            if row == n - 1 and col == m - 1:
                return diff

            for i in range(4):
                # row - 1, col
                # row, col + 1
                # row + 1, col
                # row, col - 1
                newr = row + dr[i]
                newc = col + dc[i]

                # Checking the validity of the cell.
                if 0 <= newr < n and 0 <= newc < m:
                    # Effort can be calculated as the max value of differences 
                    # between the heights of the node and its adjacent nodes.
                    newEffort = max(abs(heights[row][col] - heights[newr][newc]), diff)

                    # If the calculated effort is less than the previous value
                    # we update as we need the minimum effort.
                    if newEffort < dist[newr][newc]:
                        dist[newr][newc] = newEffort
                        heapq.heappush(pq, (newEffort, (newr, newc)))

        return 0  # if unreachable

# Driver code
heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]

obj = Solution()
ans = obj.MinimumEffort(heights)

print(ans)
