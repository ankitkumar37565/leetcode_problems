# 733. Flood Fill
class Solution:
    def dfs(self, row, col, ans, image, newColor, delRow, delCol, iniColor):
        ans[row][col] = newColor
        n = len(image)
        m = len(image[0])
        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]
            if 0 <= nrow < n and 0 <= ncol < m and image[nrow][ncol] == iniColor and ans[nrow][ncol] != newColor:
                self.dfs(nrow, ncol, ans, image, newColor, delRow, delCol, iniColor)

    def floodFill(self, image, sr, sc, newColor):
        iniColor = image[sr][sc]
        ans = [row[:] for row in image]  # Create a copy of the image
        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]
        self.dfs(sr, sc, ans, image, newColor, delRow, delCol, iniColor)
        return ans

if __name__ == "__main__":
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]
    sr, sc, newColor = 1, 1, 2
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)
    for row in ans:
        print(*row)
