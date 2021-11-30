class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            start, end = i+1, len(numbers) - 1

            comp = target - numbers[i]
            while start <= end:
                mid = (start + end) // 2
                if comp < numbers[mid]:
                    end = mid - 1
                elif comp > numbers[mid]:
                    start = mid + 1
                elif mid == i:
                    break
                else:
                    return [i + 1, mid + 1]


solution = Solution()
x = int(input())
target = int(input())
my_list = []
while x:
    x -= 1
    my_list.append(int(input()))

print(solution.twoSum(my_list, target))
