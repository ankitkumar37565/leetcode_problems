from collections import deque

class Solution:
    def shortestPath(self, grid, source, destination):
        # Edge Case: if the source is only the destination.
        if source == destination:
            return 0

        n, m = len(grid), len(grid[0])

        # Create a distance matrix with initially all the cells marked as
        # unvisited and the source cell as 0.
        dist = [[float('inf')] * m for _ in range(n)]
        dist[source[0]][source[1]] = 0

        # Create a queue for storing cells with their distances from source
        # in the form (dist, (cell coordinates pair)).
        q = deque([(0, source])

        # The following delta rows and delta columns arrays are created such that
        # each index represents each adjacent node that a cell may have 
        # in a direction.
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        # Iterate through the grid by popping the elements out of the queue
        # and pushing whenever a shorter distance to a cell is found.
        while q:
            dis, (r, c) = q.popleft()

            # Through this loop, we check the 4 direction adjacent nodes
            # for a shorter path to the destination.
            for i in range(4):
                newr = r + dr[i]
                newc = c + dc[i]

                # Checking the validity of the cell and updating if the distance is shorter.
                if 0 <= newr < n and 0 <= newc < m and grid[newr][newc] == 1 and dis + 1 < dist[newr][newc]:
                    dist[newr][newc] = 1 + dis

                    # Return the distance when we encounter the destination cell.
                    if (newr, newc) == destination:
                        return dis + 1

                    q.append((1 + dis, (newr, newc)))

        # If no path is found from source to destination.
        return -1

# Driver code
source = (0, 1)
destination = (2, 2)

grid = [[1, 1, 1, 1],
        [1, 1, 0, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [1, 0, 0, 1]]

obj = Solution()
res = obj.shortestPath(grid, source, destination)

print(res)
