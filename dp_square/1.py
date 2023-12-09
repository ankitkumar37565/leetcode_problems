# Maximum Rectangle Area with all 1’s
#  Given a row X cols binary matrix filled with 0’s and 1’s, find the largest rectangle containing only 1’s and return its area.
# Input: matrix = [[1,0,1,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,0,0,1,0]]

class Solution(object):
    def largest_rectangle_area(self,histo):
        stack = []
        max_area = 0
        n = len(histo)
        for i in range(n + 1):
            while stack and (i == n or histo[stack[-1]] >= histo[i]):
                height = histo[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, width * height)
            stack.append(i)
        return max_area

    def countSquares(self,mat):
        n,m=len(mat),len(mat[0])
        max_area = 0
        height = [0] * m
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0
            area = self.largest_rectangle_area(height)
            max_area = max(max_area, area)
        return max_area
        
        

if __name__ == "__main__":
    mat = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0]
    ]
    n, m = 4, 5
    s=Solution()
    # max_area = s.countSquares(mat, n, m)
    max_area = s.countSquares(mat)
    print(f"The maximum area is: {max_area}")
