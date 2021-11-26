class Solution:
    def isPalindrome(self, x: int) -> bool:
        num =x
        if x<0:
            return False
        rev = 0
        while(num!=0):
            rem = num %10
            rev = (rev * 10 ) + (rem)
            num = int(num / 10)

        if x == rev:
            return True
        return False


solution = Solution()
x= input()
print(solution.isPalindrome(int(x)))
