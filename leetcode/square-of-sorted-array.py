class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squares = [x*x for x in nums]
        squares.sort()
        return squares


solution = Solution()
x = int(input())
my_list = []
while x:
    x -= 1
    my_list.append(int(input()))

print(solution.sortedSquares(my_list))
