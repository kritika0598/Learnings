class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        s = s[::-1]
        count = 0
        prev = 0
        for x in s:
            if prev > d[x]:
                count = count - d[x]
            else:
                count = count + d[x]
            prev = d[x]
        return count


solution = Solution()
x = input()
print(solution.romanToInt(str(x)))
