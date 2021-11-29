class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1


solution = Solution()
x = int(input())
target = int(input())
my_list = []
while x:
    x -= 1
    my_list.append(int(input()))

print(solution.twoSum(my_list, target))
