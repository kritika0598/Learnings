class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
        return "".join(prefix)


solution = Solution()
x = int(input())
my_list = []
while x:
    x -= 1
    my_list.append(str(input()))

print(solution.longestCommonPrefix(my_list))
