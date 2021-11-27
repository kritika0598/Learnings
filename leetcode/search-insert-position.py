class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l =0
        r = len(nums)-1
        while(l<=r):
            m = l + (r-l)//2
            if nums[m] > target:
                r=m-1
            if nums[m] < target:
                l = m+1
            if nums[m] == target:
                return m
        return l

solution = Solution()
x = int(input())
target = int(input())
my_list = []
while x:
    x -= 1
    my_list.append(int(input()))

print(solution.searchInsert(my_list, target))
