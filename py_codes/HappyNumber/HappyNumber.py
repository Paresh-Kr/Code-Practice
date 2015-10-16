class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = 0
        while n:
            num += pow(n % 10, 2)
            n = n / 10
        if num < 10:
            return num == 1
        else:
            return self.isHappy(num)

test = Solution()
print test.isHappy(14)
