class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        ls = 0
        j = 0
        for i in range(len(s)):
            if s[i] in d:
                j = max(j, d[s[i]])

            ls = max(ls, i - j + 1)
            d[s[i]] = i + 1
        return ls


solution = Solution()
x = int(input())
my_list = []
while x:
    x -= 1
    s = str(input())
    print(solution.lengthOfLongestSubstring(s))
