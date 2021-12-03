class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            cnt = 1
            grid[i][j] = 0
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                cnt = cnt + dfs(i - 1, j)
            if i + 1 < n and grid[i + 1][j] == 1:
                cnt = cnt + dfs(i + 1, j)
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                cnt = cnt + dfs(i, j - 1)
            if j + 1 < m and grid[i][j + 1] == 1:
                cnt = cnt + dfs(i, j + 1)
            return cnt

        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area


solution = Solution()
n = int(input())
m = int(input())
# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
for i in range(n):  # A for loop for row entries
    a = []
    for j in range(m):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

print(solution.maxAreaOfIsland(matrix))
