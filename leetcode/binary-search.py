class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


solution = Solution()
x = int(input())
y = int(input())
my_list = []
while x:
    x -= 1
    my_list.append(int(input()))

print(solution.search(my_list, y))
