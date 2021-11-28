class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(x * x for x in nums)


solution = Solution()
x = int(input())
my_list = []
while x:
    x -= 1
    my_list.append(int(input()))

print(solution.sortedSquares(my_list))
