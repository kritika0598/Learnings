class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pr = strs[0]
        for s in strs:
            i = 0
            while True:
                if i == len(pr):
                    break
                if i == len(s):
                    pr = s
                    break
                if s[i] == pr[i]:
                    i += 1
                else:
                    pr = pr[:i]
                    break
        return pr


solution = Solution()
x=int(input())
my_list = []
while x:
    x -=1
    my_list.append(str(input()))

print(solution.longestCommonPrefix(my_list))
